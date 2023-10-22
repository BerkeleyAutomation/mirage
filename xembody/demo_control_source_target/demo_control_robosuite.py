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

def setup_robot_environment(environment_name, data_dir, args, delta_pose=False):

    options = {}
    options["env_name"] = environment_name
    options["robots"] = choose_robots(exclude_bimanual=True)

    # Hacky way to grab joint dimension for now
    joint_dim = 6 if options["robots"] == "UR5e" else 7

    # Choose controller
    controller_name = choose_controller()

    # Load the desired controller
    options["controller_configs"] = suite.load_controller_config(default_controller=controller_name)
    # options["controller_configs"] = suite.load_controller_config(custom_fpath)
    options["controller_configs"]["control_delta"] = delta_pose

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
    breakpoint()
    # env = suite.make(
    #     **options,
    #     has_renderer=args.render,
    #     has_offscreen_renderer=True,
    #     ignore_done=True,
    #     use_camera_obs=True,
    #     use_object_obs=False,
    #     horizon=(steps_per_action + steps_per_rest) * num_test_steps,
    #     control_freq=20,
    #     camera_names="sideview",
    #     camera_heights=args.height,
    #     camera_widths=args.width,
    # )
    
    kwargs = {'has_renderer': True, 'has_offscreen_renderer': True, 'ignore_done': True, 'use_object_obs': True, 'use_camera_obs': True, 'control_freq': 20, 'controller_configs': {'type': 'OSC_POSE', 'input_max': 1, 'input_min': -1, 'output_max': [0.05, 0.05, 0.05, 0.5, 0.5, 0.5], 'output_min': [-0.05, -0.05, -0.05, -0.5, -0.5, -0.5], 'kp': 150, 'damping': 1, 'impedance_mode': 'fixed', 'kp_limits': [0, 300], 'damping_limits': [0, 10], 'position_limits': None, 'orientation_limits': None, 'uncouple_pos_ori': True, 'control_delta': True, 'interpolation': None, 'ramp_ratio': 0.2}, 'robots': ['Sawyer'], 'camera_depths': False, 'camera_heights': 84, 'camera_widths': 84, 'reward_shaping': False, 'camera_names': 'sideview', 'render_gpu_device_id': 0}
    kwargs = {'has_renderer': False, 'has_offscreen_renderer': False, 'ignore_done': True, 'use_object_obs': False, 'use_camera_obs': True, 'control_freq': 20, 'controller_configs': {'type': 'OSC_POSE', 'input_max': 1, 'input_min': -1, 'output_max': [0.05, 0.05, 0.05, 0.5, 0.5, 0.5], 'output_min': [-0.05, -0.05, -0.05, -0.5, -0.5, -0.5], 'kp': 150, 'damping': 1, 'impedance_mode': 'fixed', 'kp_limits': [0, 300], 'damping_limits': [0, 10], 'position_limits': None, 'orientation_limits': None, 'uncouple_pos_ori': True, 'control_delta': True, 'interpolation': None, 'ramp_ratio': 0.2}, 'robots': ['Sawyer'], 'camera_depths': False, 'camera_heights': 84, 'camera_widths': 84, 'reward_shaping': False, 'camera_names': 'sideview'}
    
    # env = suite.make('Lift', **kwargs)
    from robomimic.envs.env_robosuite import EnvRobosuite
    env = EnvRobosuite(
        env_name='Lift', 
        render=True, 
        render_offscreen=True, 
        use_image_obs=True,
        postprocess_visual_obs=True,
        **kwargs,
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

    # breakpoint()
    # env.robots[0].set_robot_joint_positions(np.array([0, 0, 0, 0, 0, 0, 0]))
    dof = env.action_dim
    recorded_states = []

    action_history = []
    for t in range(timesteps):
        # breakpoint()
        # action = np.random.randn(dof)
        # action = np.zeros(dof)
        action = np.array([0.01, 0.01, 0.01, 0, 0, 0, 0])
        action[:3] = np.random.uniform(-0.02, 0.02, 3)
        action[3:6] = np.random.uniform(-0.2, 0.2, 3)
        action[-1] = 0
        action_history.append(action)
        # action[3:] = np.array([0,0,0,0])
        # print("Action", action)
        # print("set_ori here", T.quat2mat(np.array([np.sqrt(2)/2,np.sqrt(2)/2,0,0])))
        # action = np.array([ 0.34099258, -0.00757787,  0.99650845, np.sqrt(2)/2,np.sqrt(2)/2,0,0])
        obs, _, _, _ = env.step(action)
        if args.render:
            env.render()
        # obs, _, _, _ = env.step(TARGET_STATE)
        # print(t, obs["robot0_proprio-state"])
        # print(obs.keys()) # ['robot0_joint_pos', 'robot0_joint_vel', 'robot0_eef_pos', 'robot0_eef_quat', 'robot0_gripper_qpos', 'robot0_gripper_qvel', 'sideview_image', 'robot0_proprio-state']
        
        eef_site_name = env.robots[0].controller.eef_name
        curr_pos = np.array(env.sim.data.site_xpos[env.sim.model.site_name2id(eef_site_name)])
        curr_rot = np.array(T.mat2quat(env.sim.data.site_xmat[env.sim.model.site_name2id(eef_site_name)].reshape([3, 3])))
        new_state = np.concatenate((curr_pos, curr_rot))
        recorded_states.append(new_state)
        # new_state = np.concatenate((obs["robot0_eef_pos"], obs["robot0_eef_quat"]))
        print(new_state)
        # print("T Error:", np.linalg.norm((new_state - TARGET_STATE)[:3]))
        # print("R Error:", np.linalg.norm((new_state - TARGET_STATE)[3:]))
        # print(t, obs["robot0_eef_pos"], obs["robot0_eef_quat"])
        # print(t, obs["robot0_joint_pos"])

        # joints = env.robots[0].controller.inverse_kinematics(obs["robot0_eef_pos"], obs["robot0_eef_quat"])
        # print(t, joints)
        # env.robots[0].set_robot_joint_positions(joints)

        # env.robots[0].controller.sync_ik_robot(joints, simulate=True)
        # print(t, env.sim.get_state().flatten())

        # dump a frame from every K frames
        if t % skip_frame == 0:
            frame = obs["sideview_image"]
            writer.append_data(frame)
    # save recorded_states as an npz file
    print("length of trajectory:", len(recorded_states))
    np.savez(os.path.join(data_dir, "recorded_states.npz"), states=np.array(recorded_states))
    writer.close()
    return action_history

# Joints is a list of numbers
def fk(chain, joints):
    print("Made it into fk")
    joint_input = joints
    return chain.forward_kinematics(joint_input)

def playback_trajectory(chain, ep_dir, env, action_history):
    """Playback data from an episode.

    Args:
        env (MujocoEnv): environment instance to playback trajectory in
        ep_dir (str): The path to the directory containing data for an episode.
    """
    recorded_stats = np.load(os.path.join(data_dir, "recorded_states.npz"))
    state_paths = os.path.join(ep_dir, "state_*.npz")
    video_path = os.path.join(data_dir, "target_robot.mp4")
    writer = imageio.get_writer(video_path, fps=20)

    # breakpoint()
    state_file = sorted(glob.glob(state_paths))[0]
    dic = np.load(state_file)
    # print("states (wrong):", dic["states"])
    # print("states (right):", recorded_stats["states"])
    states = recorded_stats["states"]
    for _ in range(100):
        action = np.array([ 0.34099258, -0.00757787,  0.99650845, np.sqrt(2)/2,np.sqrt(2)/2,0,0])
        action[:3] = states[0, :3]
        # action[3:6] = T.quat2axisangle(np.array([np.sqrt(2)/2,np.sqrt(2)/2,0,0]))
        action[3:6] = T.quat2axisangle(states[0, 3:])
        obs, _, _, _ = env.step(action)
    
    # read states back, load them one by one, and render
    t = 0
    # for state_file in sorted(glob.glob(state_paths)):
        # dic = np.load(state_file)
        # print(dic["states"])
        # states = dic["states"]
    states = recorded_stats["states"]
    errors = []
    
    env.robots[0].controller.use_delta = True # change back to delta pose
    for i in range(len(states)):
        state = states[i]
        # print("Target state:", state)
        # print(states)
        # joints = env.robots[0].controller.inverse_kinematics(state[:3], state[3:])
        # joints = env.robots[0].controller.joint_positions_for_eef_command(state[:3], T.quat2mat(state[3:]))
        # print(t, fk(chain, joints))
        # env.robots[0].set_robot_joint_positions(joints)
        # import pdb; pdb.set_trace()
        action = np.array([ 0.34099258, -0.00757787,  0.99650845, np.sqrt(2)/2,np.sqrt(2)/2,0,0])
        action[:3] = state[:3]
        action[3:6] = T.quat2axisangle(state[3:])
        # action[3:6] = T.quat2axisangle(np.array([np.sqrt(2)/2,np.sqrt(2)/2,0,0]))
        
        action = action_history[i]
        # for i in range(10):
        obs, _, _, _ = env.step(action)
        # obs, _, _, _ = env.step(TARGET_STATE)
        # print("Actual state (wrong):",  obs["robot0_eef_pos"], obs["robot0_eef_quat"])
        
        eef_site_name = env.robots[0].controller.eef_name
        curr_pos = np.array(env.sim.data.site_xpos[env.sim.model.site_name2id(eef_site_name)])
        curr_rot = np.array(T.mat2quat(env.sim.data.site_xmat[env.sim.model.site_name2id(eef_site_name)].reshape([3, 3])))
        new_state = np.concatenate((curr_pos, curr_rot))
        # new_state = np.concatenate((obs["robot0_eef_pos"], obs["robot0_eef_quat"]))
        # print("Actual state (correct):", new_state)
        error = state - new_state
        # print("Error:", error)
        errors.append(error)
        
        if np.linalg.norm(error[:3]) > 0.1 or np.linalg.norm(error[3:]) > 0.1:
            print("Target state:", state)
            print("Actual state:", new_state)
            print("Error:", error)
        
        t += 1

        frame = obs["sideview_image"]
        writer.append_data(frame)
    writer.close()
    
    import matplotlib.pyplot as plt
    for i in range(3):
        plt.plot(np.array(errors)[:, i])
    plt.show()
    print("Average error:", np.mean(np.abs(np.array(errors)), axis=0))

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str, default="/home/lawrence/xembody/robosuite/collected_data")
    parser.add_argument("--height", type=int, default=512)
    parser.add_argument("--width", type=int, default=512)
    parser.add_argument("--render", action='store_true')
    args = parser.parse_args()

    unix_time = time.time()
    data_dir = os.path.join(args.directory, str(unix_time))
    os.mkdir(data_dir)

    # print welcome info
    print("Welcome to robosuite v{}!".format(suite.__version__))
    print(suite.__logo__)

    # Choose environment and add it to options
    selected_env = choose_environment()
    
    source_robot_env, source_robot_type = setup_robot_environment(selected_env, data_dir, args, delta_pose=True)  
    
    action_history = collect_random_trajectory(source_robot_env, data_dir)
    
    
    # Shut down this env before starting the next test
    source_robot_env.close()


    target_robot_env, target_robot_type = setup_robot_environment(selected_env, data_dir, args, delta_pose=False)

    # source_robot_mjcf = open(f"/home/lawrence/xembody/robosuite/robosuite/models/assets/robots/{source_robot_type.lower()}/no_texture_robot.xml").read()
    # source_robot_chain = pk.build_chain_from_mjcf(source_robot_mjcf)
    
    # playback_trajectory(source_robot_chain, source_robot_env.ep_directory)
    playback_trajectory(None, source_robot_env.ep_directory, target_robot_env, action_history)

    # # Shut down this env before starting the next test
    target_robot_env.close()