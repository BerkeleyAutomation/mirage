"""
This demo script demonstrates the various functionalities of each controller available within robosuite.

For a given controller, runs through each dimension and executes a perturbation "test_value" from its
neutral (stationary) value for a certain amount of time "steps_per_action", and then returns to all neutral values
for time "steps_per_rest" before proceeding with the next action dim.

    E.g.: Given that the expected action space of the Pos / Ori (OSC_POSE) controller (without a gripper) is
    (dx, dy, dz, droll, dpitch, dyaw), the testing sequence of actions over time will be:

        ***START OF DEMO***
        ( dx,  0,  0,  0,  0,  0, grip)     <-- Translation in x-direction      for 'steps_per_action' steps
        (  0,  0,  0,  0,  0,  0, grip)     <-- No movement (pause)             for 'steps_per_rest' steps
        (  0, dy,  0,  0,  0,  0, grip)     <-- Translation in y-direction      for 'steps_per_action' steps
        (  0,  0,  0,  0,  0,  0, grip)     <-- No movement (pause)             for 'steps_per_rest' steps
        (  0,  0, dz,  0,  0,  0, grip)     <-- Translation in z-direction      for 'steps_per_action' steps
        (  0,  0,  0,  0,  0,  0, grip)     <-- No movement (pause)             for 'steps_per_rest' steps
        (  0,  0,  0, dr,  0,  0, grip)     <-- Rotation in roll (x) axis       for 'steps_per_action' steps
        (  0,  0,  0,  0,  0,  0, grip)     <-- No movement (pause)             for 'steps_per_rest' steps
        (  0,  0,  0,  0, dp,  0, grip)     <-- Rotation in pitch (y) axis      for 'steps_per_action' steps
        (  0,  0,  0,  0,  0,  0, grip)     <-- No movement (pause)             for 'steps_per_rest' steps
        (  0,  0,  0,  0,  0, dy, grip)     <-- Rotation in yaw (z) axis        for 'steps_per_action' steps
        (  0,  0,  0,  0,  0,  0, grip)     <-- No movement (pause)             for 'steps_per_rest' steps
        ***END OF DEMO***

    Thus the OSC_POSE controller should be expected to sequentially move linearly in the x direction first,
        then the y direction, then the z direction, and then begin sequentially rotating about its x-axis,
        then y-axis, then z-axis.

Please reference the documentation of Controllers in the Modules section for an overview of each controller.
Controllers are expected to behave in a generally controlled manner, according to their control space. The expected
sequential qualitative behavior during the test is described below for each controller:

* OSC_POSE: Gripper moves sequentially and linearly in x, y, z direction, then sequentially rotates in x-axis, y-axis,
            z-axis, relative to the global coordinate frame
* OSC_POSITION: Gripper moves sequentially and linearly in x, y, z direction, relative to the global coordinate frame
* IK_POSE: Gripper moves sequentially and linearly in x, y, z direction, then sequentially rotates in x-axis, y-axis,
            z-axis, relative to the local robot end effector frame
* JOINT_POSITION: Robot Joints move sequentially in a controlled fashion
* JOINT_VELOCITY: Robot Joints move sequentially in a controlled fashion
* JOINT_TORQUE: Unlike other controllers, joint torque controller is expected to act rather lethargic, as the
            "controller" is really just a wrapper for direct torque control of the mujoco actuators. Therefore, a
            "neutral" value of 0 torque will not guarantee a stable robot when it has non-zero velocity!

"""

import robosuite as suite
from robosuite.controllers import load_controller_config
from robosuite.robots import Bimanual
from robosuite.utils.input_utils import *
from robosuite.wrappers import DataCollectionWrapper
import robosuite.macros as macros

import imageio
import argparse
import os
import time
import numpy as np
# import kinpy as kp
import pytorch_kinematics as pk
import glob
from tracikpy import TracIKSolver
import cmath
import robosuite.utils.transform_utils as T

macros.IMAGE_CONVENTION = "opencv"
# TARGET_STATE = np.array([-0.10744946, -0.02256496, 0.99589964, 0.99876111, 0.00145187, 0.047579, 0.01450425])
# TARGET_STATE = np.array([np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, 1])
TARGET_STATE = np.zeros(8)

def setup_robot_environment(environment_name, data_dir, args):

    options = {}
    options["env_name"] = environment_name
    options["robots"] = choose_robots(exclude_bimanual=True)

    # Hacky way to grab joint dimension for now
    joint_dim = 6 if options["robots"] == "UR5e" else 7

    # Choose controller
    controller_name = choose_controller()

    # Load the desired controller
    options["controller_configs"] = suite.load_controller_config(default_controller=controller_name)

    # Define the pre-defined controller actions to use (action_dim, num_test_steps, test_value)
    controller_settings = {
        "OSC_POSE": [6, 6, 0.1],
        "OSC_POSITION": [3, 3, 0.1],
        "IK_POSE": [6, 6, 0.01],
        "JOINT_POSITION": [joint_dim, joint_dim, 0.2],
        "JOINT_VELOCITY": [joint_dim, joint_dim, -0.1],
        "JOINT_TORQUE": [joint_dim, joint_dim, 0.25],
    }

    # Define variables for each controller test
    action_dim = controller_settings[controller_name][0]
    
    num_test_steps = controller_settings[controller_name][1]
    test_value = controller_settings[controller_name][2]

    # Define the number of timesteps to use per controller action as well as timesteps in between actions
    steps_per_action = 75
    steps_per_rest = 75

    env = suite.make(
        **options,
        has_renderer=False,
        has_offscreen_renderer=True,
        ignore_done=True,
        use_camera_obs=True,
        use_object_obs=False,
        horizon=(steps_per_action + steps_per_rest) * num_test_steps,
        control_freq=20,
        camera_names="birdview",
        camera_heights=args.height,
        camera_widths=args.width,
    )


    # To accommodate for multi-arm settings (e.g.: Baxter), we need to make sure to fill any extra action space
    # Get total number of arms being controlled
    n = 0
    gripper_dim = 0
    for robot in env.robots:
        gripper_dim = robot.gripper["right"].dof if isinstance(robot, Bimanual) else robot.gripper.dof
        n += int(robot.action_dim / (action_dim + gripper_dim))
    
    env = DataCollectionWrapper(env, data_dir)
    env.reset()
    return env, options["robots"]

def collect_random_trajectory(env, data_dir, timesteps=100):
    """Run a random policy to collect trajectories.

    The rollout trajectory is saved to files in npz format.
    Modify the DataCollectionWrapper wrapper to add new fields or change data formats.

    Args:
        env (MujocoEnv): environment instance to collect trajectories from
        timesteps(int): how many environment timesteps to run for a given trajectory
    """
    video_path = os.path.join(data_dir, "source_robot.mp4")
    writer = imageio.get_writer(video_path, fps=20)

    skip_frame = 1

    env.reset()

    env.robots[0].set_robot_joint_positions(np.array([0, 0, 0, 0, 0, 0, 0]))
    dof = env.action_dim
    for t in range(timesteps):
        # action = np.random.randn(dof)
        action = np.zeros(dof)
        # obs, _, _, _ = env.step(action)
        obs, _, _, _ = env.step(TARGET_STATE)
        # print(t, obs["robot0_proprio-state"])
        print(obs.keys())
        new_state = np.concatenate((obs["robot0_eef_pos"], obs["robot0_eef_quat"]))
        print(new_state)
        # print("T Error:", np.linalg.norm((new_state - TARGET_STATE)[:3]))
        # print("R Error:", np.linalg.norm((new_state - TARGET_STATE)[3:]))
        # print(t, obs["robot0_eef_pos"], obs["robot0_eef_quat"])
        print(t, obs["robot0_joint_pos"])
        
        # ik_solver = TracIKSolver(
        #         "/home/lawrence/xembody/robosuite/robosuite/models/assets/bullet_data/panda_description/urdf/panda_arm.urdf",
        #         "panda_link0",
        #         "panda_link8",
        #     )
        
        # ik_solver = TracIKSolver(
        #         "/home/lawrence/xembody/panda_with_gripper_model.xml",
        #         "robot0_base",
        #         "gripper0_grip_site",
        #     )
        # ee_out = ik_solver.fk(obs["robot0_joint_pos"])
        # print("TracIK Predict:", ee_out)
        import kinpy as kp
        chain = kp.build_serial_chain_from_mjcf(open("/home/lawrence/xembody/panda_with_gripper_model.xml").read(), "gripper0_eef")
        print(chain)
        print(chain.get_joint_parameter_names())
        ee_out = chain.forward_kinematics(obs["robot0_joint_pos"], end_only=False)
        
        print("Predict:", ee_out)
        print("Actual:", obs["robot0_eef_pos"])
        
        from dm_control import mjcf
        from dm_control.utils.inverse_kinematics import qpos_from_site_pose
        from dm_robotics.moma.utils import ik_solver
        from dm_robotics.geometry import geometry
        from dm_robotics.geometry import mujoco_physics
        mjcf_model = mjcf.from_path("/home/lawrence/xembody/panda_with_gripper_model.xml")
        print(type(mjcf_model))
        breakpoint()
        ik_site = mjcf_model.find("site", "gripper0_grip_site")
        solver = ik_solver.IkSolver(mjcf_model, mjcf_model.find_all("joint"), ik_site)
        ref_pose = geometry.Pose(new_state[:3], new_state[3:])
        result = qpos_from_site_pose(
                physics=mjcf.Physics.from_mjcf_model(mjcf_model),
                site_name="gripper0_grip_site",
                target_pos=new_state[:3],
                target_quat=new_state[3:],
                # joint_names=self.joint_names,
                tol=1e-7,
                max_steps=300,
                inplace=False,
            )
        
        # Check that we can solve the problem and that the solution is within
        # the joint ranges.
        # Linear and angular tolerance when comparing the end pose and the target pose.
        _LINEAR_TOL = 1e-4
        _ANGULAR_TOL = 1e-4
        qpos_sol = solver.solve(
            ref_pose, linear_tol=_LINEAR_TOL, angular_tol=_ANGULAR_TOL,
            early_stop=True, stop_on_first_successful_attempt=True)
        
        # Check the max linear and angular errors are satisfied.
        geometry_physics = mujoco_physics.wrap(solver._physics)
        solver._joints_binding.qpos[:] = qpos_sol
        end_pose = geometry_physics.world_pose(ik_site)
        linear_error = np.linalg.norm(end_pose.position - ref_pose.position)
        print("Linear error: ", linear_error)
        joints = qpos_sol
        print("IK Solved joints: ", joints)
        # joints = env.robots[0].controller.inverse_kinematics(obs["robot0_eef_pos"], obs["robot0_eef_quat"])
        # print(t, joints)
        # env.robots[0].set_robot_joint_positions(joints)

        # env.robots[0].controller.sync_ik_robot(joints, simulate=True)
        # print(t, env.sim.get_state().flatten())

        # dump a frame from every K frames
        if t % skip_frame == 0:
            frame = obs["birdview_image"]
            writer.append_data(frame)

    writer.close()

# Joints is a list of numbers
def fk(chain, joints):
    print("Made it into fk")
    joint_input = joints
    return chain.forward_kinematics(joint_input)

def playback_trajectory(chain, ep_dir, env):
    """Playback data from an episode.

    Args:
        env (MujocoEnv): environment instance to playback trajectory in
        ep_dir (str): The path to the directory containing data for an episode.
    """
    state_paths = os.path.join(ep_dir, "state_*.npz")
    video_path = os.path.join(data_dir, "target_robot.mp4")
    writer = imageio.get_writer(video_path, fps=20)

    # read states back, load them one by one, and render
    t = 0
    for state_file in sorted(glob.glob(state_paths)):
        dic = np.load(state_file)
        # print(dic["proprio"])
        states = dic["states"]
        for state in states:
            # ik_solver = TracIKSolver(
            #     "/home/lawrence/xembody/robosuite/robosuite/models/assets/bullet_data/panda_description/urdf/panda_arm_hand.urdf",
            #     "panda_link0",
            #     "panda_hand",
            # )
            print(state)
            target_pose = T.quat2mat(state[3:])
            target_pose = np.hstack((np.vstack((target_pose, np.array([[0,0,0]]))),np.array([[state[0]], [state[1]], [state[2]], [1]])))
            print(target_pose)
            # ee_out = ik_solver.fk(obs["robot0_joint_pos"])
            # print(ee_out)
            # sol = ik_solver.ik(target_pose,q_init=obs["robot0_joint_pos"], bx=1e-3,
            #         by=1e-3,
            #         bz=1e-3,
            #         brx=cmath.inf,
            #         bry=cmath.inf,
            #         brz=cmath.inf,)
            # print(sol / np.pi * 180)
            
            from dm_control import mjcf
            from dm_robotics.moma.utils import ik_solver
            from dm_robotics.geometry import geometry
            from dm_robotics.geometry import mujoco_physics
            mjcf_model = mjcf.from_path("/home/lawrence/xembody/robosuite/robosuite/models/assets/robots/panda/no_texture_robot.xml")
            ik_site = mjcf_model.find("site", "right_hand")
            solver = ik_solver.IkSolver(mjcf_model, mjcf_model.find_all("joint"), ik_site)
            ref_pose = geometry.Pose(state[:3], state[3:])

            # Check that we can solve the problem and that the solution is within
            # the joint ranges.
            # Linear and angular tolerance when comparing the end pose and the target pose.
            _LINEAR_TOL = 1e-4
            _ANGULAR_TOL = 1e-4
            qpos_sol = solver.solve(
                ref_pose, linear_tol=_LINEAR_TOL, angular_tol=_ANGULAR_TOL,
                early_stop=True, stop_on_first_successful_attempt=True)
            
            # Check the max linear and angular errors are satisfied.
            geometry_physics = mujoco_physics.wrap(solver._physics)
            solver._joints_binding.qpos[:] = qpos_sol
            end_pose = geometry_physics.world_pose(ik_site)
            linear_error = np.linalg.norm(end_pose.position - ref_pose.position)
            print("Linear error: ", linear_error)
            joints = qpos_sol
            # joints = env.robots[0].controller.inverse_kinematics(state[:3], state[3:])
            # print(t, fk(chain, joints))
            env.robots[0].set_robot_joint_positions(joints)
            # import pdb; pdb.set_trace()
            # obs, _, _, _ = env.step(state)
            obs, _, _, _ = env.step(TARGET_STATE)
            print(t, obs["robot0_eef_pos"], obs["robot0_eef_quat"])
            t += 1

            frame = obs["birdview_image"]
            writer.append_data(frame)
    writer.close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str, default="/home/lawrence/xembody/robosuite/collected_data")
    parser.add_argument("--height", type=int, default=512)
    parser.add_argument("--width", type=int, default=512)
    args = parser.parse_args()

    unix_time = time.time()
    data_dir = os.path.join(args.directory, str(unix_time))
    os.mkdir(data_dir)

    # print welcome info
    print("Welcome to robosuite v{}!".format(suite.__version__))
    print(suite.__logo__)

    # Choose environment and add it to options
    selected_env = choose_environment()

    
    source_robot_env, source_robot_type = setup_robot_environment(selected_env, data_dir, args)  
    collect_random_trajectory(source_robot_env, data_dir)

    # Shut down this env before starting the next test
    source_robot_env.close()


    target_robot_env, target_robot_type = setup_robot_environment(selected_env, data_dir, args)

    # source_robot_mjcf = open(f"/home/lawrence/xembody/robosuite/robosuite/models/assets/robots/{source_robot_type.lower()}/no_texture_robot.xml").read()
    # source_robot_chain = pk.build_chain_from_mjcf(source_robot_mjcf)

    # playback_trajectory(source_robot_chain, source_robot_env.ep_directory)
    playback_trajectory(None, source_robot_env.ep_directory, target_robot_env)

    # # Shut down this env before starting the next test
    target_robot_env.close()