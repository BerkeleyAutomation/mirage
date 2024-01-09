import argparse
import json

import numpy as np
import matplotlib.pyplot as plt
import robosuite as suite
import robosuite.utils.transform_utils as T
import robosuite.utils.camera_utils as camera_utils
from robosuite.controllers import load_controller_config
from robosuite.renderers import load_renderer_config
from robosuite.utils.input_utils import *
import robosuite.macros as macros
macros.IMAGE_CONVENTION = "opencv"

def str2bool(v):
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")

def image_to_pointcloud(depth_map, camera_name, camera_height, camera_width, segmask=None):
    """
    Convert depth image to point cloud
    """
    real_depth_map = camera_utils.get_real_depth_map(env.sim, depth_map)
    # Camera transform matrix to project from camera coordinates to world coordinates.
    extrinsic_matrix = camera_utils.get_camera_extrinsic_matrix(env.sim, camera_name=camera_name)
    print('cam name: ', camera_name, ' extrinsic_matrix: ', extrinsic_matrix)
    intrinsic_matrix = camera_utils.get_camera_intrinsic_matrix(env.sim, camera_name=camera_name, camera_height=camera_height, camera_width=camera_width)
    print('cam name: ', camera_name, ' intrinsic_matrix: ', intrinsic_matrix)

    # Convert depth image to point cloud
    points = [] # 3D points in robot frame of shape […, 3]
    for x in range(camera_width):
        for y in range(camera_height):
            if segmask is not None and segmask[y, x] == 0:
                continue
            coord_cam_frame = np.array([(x-intrinsic_matrix[0, -1])/intrinsic_matrix[0, 0], (y-intrinsic_matrix[1, -1])/intrinsic_matrix[1, 1], 1]) * real_depth_map[y, x]
            # points.append(coord_cam_frame)
            
            coord_world_frame = np.dot(extrinsic_matrix, np.concatenate((coord_cam_frame, [1])))
            points.append(coord_world_frame)


    return points



if __name__ == "__main__":

    """
    Registered environments: Lift, Stack, NutAssembly, NutAssemblySingle, NutAssemblySquare, NutAssemblyRound,
                             PickPlace, PickPlaceSingle, PickPlaceMilk, PickPlaceBread, PickPlaceCereal,
                             PickPlaceCan, Door, Wipe, TwoArmLift, TwoArmPegInHole, TwoArmHandover

    Possible robots: Baxter, IIWA, Jaco, Kinova3, Panda, Sawyer, UR5e
    """

    options = {}

    # print welcome info
    print("Welcome to robosuite v{}!".format(suite.__version__))
    print(suite.__logo__)

    parser = argparse.ArgumentParser()
    parser.add_argument("--renderer", type=str, default="mujoco", help="Valid options include mujoco, and nvisii")

    args = parser.parse_args()
    renderer = args.renderer

    options["env_name"] = choose_environment()

    # If a multi-arm environment has been chosen, choose configuration and appropriate robot(s)
    if "TwoArm" in options["env_name"]:
        # Choose env config and add it to options
        options["env_configuration"] = choose_multi_arm_config()

        # If chosen configuration was bimanual, the corresponding robot must be Baxter. Else, have user choose robots
        if options["env_configuration"] == "bimanual":
            options["robots"] = "Baxter"
        else:
            options["robots"] = []

            # Have user choose two robots
            print("A multiple single-arm configuration was chosen.\n")

            for i in range(2):
                print("Please choose Robot {}...\n".format(i))
                options["robots"].append(choose_robots(exclude_bimanual=True))

    # Else, we simply choose a single (single-armed) robot to instantiate in the environment
    else:
        options["robots"] = choose_robots(exclude_bimanual=True)

    # Choose controller
    controller_name = choose_controller()

    # Load the desired controller
    options["controller_configs"] = load_controller_config(default_controller=controller_name)
    breakpoint()
    env = suite.make(
        **options,
        has_renderer=False if renderer != "mujoco" else True,  # no on-screen renderer
        has_offscreen_renderer=True,  # no off-screen renderer
        ignore_done=True,
        use_camera_obs=True,  # no camera observations
        control_freq=20,
        renderer=renderer,
        camera_names = [#"frontview", "sideview", "birdview", "farview", "sidefarview", 
            "agentview"],
        camera_heights = 256,
        camera_widths = 256,
        camera_depths = True,
        camera_segmentations = "robot_only",
    )

    env.reset()

    low, high = env.action_spec

    if renderer == "nvisii":

        timesteps = 300
        for i in range(timesteps):
            action = np.random.uniform(low, high)
            obs, reward, done, _ = env.step(action)

            if i % 100 == 0:
                env.render()

    else:
        if options["robots"] == "Panda":
            joint_angles_list = [
                                # [0, 0, 0, 0, 0, 0, 0],
                                # [np.pi / 6, np.pi / 6, np.pi / 6, np.pi / 6, np.pi / 6, np.pi / 6, np.pi / 6],
                                # [np.pi / 4, np.pi / 4, np.pi / 4, np.pi / 4, np.pi / 4, np.pi / 4, np.pi / 4],
                                # [np.pi / 3, np.pi / 3, np.pi / 3, np.pi / 3, np.pi / 3, np.pi / 3, np.pi / 3],
                                # [np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2, np.pi / 2],
                                # [np.pi, np.pi, np.pi, np.pi, np.pi, np.pi, np.pi],
                                [9.44962915e-03,  2.04028892e-01,  2.27688289e-02, -2.64987059e+00, 1.89505922e-03,  2.91240765e+00,  7.87470020e-01]
                                ]
        elif options["robots"] == "UR5e":
            joint_angles_list = [[0, 0, 0, 0, 0, 0],
                                 [-np.pi / 6, -np.pi / 6, np.pi / 6, -np.pi / 6, -np.pi / 6, -np.pi / 6],
                                 [-np.pi / 4, -np.pi / 4, np.pi / 4, -np.pi / 4, -np.pi / 4, -np.pi / 4],
                                 [-np.pi / 3, -np.pi / 3, np.pi / 3, -np.pi / 3, -np.pi / 3, -np.pi / 3],
                                 [-np.pi / 2, -np.pi / 2, np.pi / 2, -np.pi / 2, -np.pi / 2, -np.pi / 2],
                                 [-np.pi, -np.pi, np.pi, -np.pi, -np.pi, -np.pi],
                                 [-0.46410589, -1.74117144,  2.46527756, -2.26201741, -1.61841739, -1.98669771]
                                ]
        
        all_output = []
        for i, joint_angles in enumerate(joint_angles_list):
            output_dict = {}
            for i in range(50):
                env.robots[0].set_robot_joint_positions(joint_angles)
                env.sim.forward()
                env.sim.step()
                env._update_observables()
            obs = env._get_observations()
            
            # joints
            actual_joint_angles = obs['robot0_joint_pos']
            print("joint_angles: ", joint_angles)
            print("actual_joint_angles: ", actual_joint_angles)
            # EE
            robot_eef_pos = obs['robot0_eef_pos']
            robot_eef_quat = obs['robot0_eef_quat']            
            # base position
            base_pos = np.array([float(x) for x in env.robots[0].robot_model._elements["root_body"].get("pos").split(" ")])
            
            output_dict["joint_angles"] = actual_joint_angles
            output_dict["robot_eef_pos"] = robot_eef_pos
            output_dict["robot_eef_quat"] = robot_eef_quat
            output_dict["base_pos"] = base_pos
            
            views = [#"frontview", "sideview", "birdview", "farview", "sidefarview",
                "agentview"]
            for view in views:
                
                # frontview
                front_rgb_img = obs[f'{view}_image']
                front_seg_img = obs[f'{view}_segmentation_robot_only']
                
                # point cloud
                front_depth_map = obs[f'{view}_depth']
                front_real_depth_map = camera_utils.get_real_depth_map(env.sim, front_depth_map)
                points = image_to_pointcloud(front_depth_map, view, 256, 256)
                
                # Camera transform matrix to project from camera coordinates to world coordinates.
                front_extrinsic_matrix = camera_utils.get_camera_extrinsic_matrix(env.sim, camera_name=view)
                front_intrinsic_matrix = camera_utils.get_camera_intrinsic_matrix(env.sim, camera_name=view, camera_height=256, camera_width=256)
            
                breakpoint()
                """
                84x84
                cam name:  agentview  extrinsic_matrix:  [[ 0.          0.70614784 -0.70806442  0.5       ]
                                                            [ 1.          0.          0.          0.        ]
                                                            [ 0.         -0.70806442 -0.70614784  1.35      ]
                                                            [ 0.          0.          0.          1.        ]]
                cam name:  agentview  intrinsic_matrix:  [[101.39696962   0.          42.        ]
                                                        [  0.         101.39696962  42.        ]
                                                        [  0.           0.           1.        ]]
                256x256
                cam name:  agentview  extrinsic_matrix:  [[ 0.          0.70614784 -0.70806442  0.5       ]
                                                            [ 1.          0.          0.          0.        ]
                                                            [ 0.         -0.70806442 -0.70614784  1.35      ]
                                                            [ 0.          0.          0.          1.        ]]
                cam name:  agentview  intrinsic_matrix:  [[309.01933598   0.         128.        ]
                                                            [  0.         309.01933598 128.        ]
                                                            [  0.           0.           1.        ]]
                512x512
                cam name:  agentview  extrinsic_matrix:  [[ 0.          0.70614784 -0.70806442  0.5       ]
                                                            [ 1.          0.          0.          0.        ]
                                                            [ 0.         -0.70806442 -0.70614784  1.35      ]
                                                            [ 0.          0.          0.          1.        ]]
                cam name:  agentview  intrinsic_matrix:  [[618.03867197   0.         256.        ]
                                                            [  0.         618.03867197 256.        ]
                                                            [  0.           0.        1.        ]]                                       
                """
                # visualize the robot
                # plt.imshow(front_rgb_img); plt.show()
                # plt.imshow(front_seg_img); plt.show()
                import cv2
                cv2.imwrite(f"output/{options['robots']}_output_1img_{view}_rgb_256.png", cv2.cvtColor(front_rgb_img, cv2.COLOR_RGB2BGR))
                cv2.imwrite(f"output/{options['robots']}_output_1img_{view}_seg_256.png", front_seg_img * 255)

                output_dict[view] = {}
                output_dict[view]["rgb"] = front_rgb_img
                output_dict[view]["seg"] = front_seg_img
                output_dict[view]["points"] = points
                output_dict[view]["real_depth_map"] = front_real_depth_map
                output_dict[view]["extrinsic_matrix"] = front_extrinsic_matrix
                output_dict[view]["intrinsic_matrix"] = front_intrinsic_matrix
                
            all_output.append(output_dict)
        
        # save the list to npy file
        np.save(f"output/{options['robots']}_output_1img.npy", all_output)

    env.close_renderer()
    print("Done.")
