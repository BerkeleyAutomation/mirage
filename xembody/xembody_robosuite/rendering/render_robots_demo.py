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
    intrinsic_matrix = camera_utils.get_camera_intrinsic_matrix(env.sim, camera_name=camera_name, camera_height=camera_height, camera_width=camera_width)
    # Convert depth image to point cloud
    points = [] # 3D points in robot frame of shape […, 3]
    for x in range(camera_width):
        for y in range(camera_height):
            if segmask is not None and segmask[y, x] == 0:
                continue
            coord_cam_frame = np.array([(x-intrinsic_matrix[0, -1])/intrinsic_matrix[0, 0], (y-intrinsic_matrix[1, -1])/intrinsic_matrix[1, 1], 1]) * real_depth_map[y, x]
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

    env = suite.make(
        **options,
        has_renderer=False if renderer != "mujoco" else True,  # no on-screen renderer
        has_offscreen_renderer=True,  # no off-screen renderer
        ignore_done=True,
        use_camera_obs=True,  # no camera observations
        control_freq=20,
        renderer=renderer,
        camera_names = ["frontview", "sideview"],
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

        # do visualization
        for i in range(10000):
            action = np.random.uniform(low, high)
            action = np.array([0,0,1,1])
            obs, reward, done, _ = env.step(action)
            import pdb; pdb.set_trace()
            print("Joint angles:", obs['robot0_joint_pos'])
            # env.render()
            # plt.imshow(obs['frontview_image']); plt.show()
            # plt.imshow(obs['frontview_segmentation_robot_only']); plt.show() # (256, 256, 1)
            
            # plot point cloud
            depth_map = obs['frontview_depth']
            points = image_to_pointcloud(depth_map, "frontview", 256, 256)
            fig = plt.figure(figsize=(12, 12))
            ax = fig.add_subplot(projection='3d')
            ax.scatter([x[0] for x in points], [x[1] for x in points], [x[2] for x in points], s=1)
            # plot the base
            ax.scatter(*[[float(x)] for x in env.robots[0].robot_model._elements["root_body"].get("pos").split(" ")], s=100, c='r')
            # plot the EE
            robot_eef = obs['robot0_eef_pos']
            ax.scatter(*robot_eef, s=100, c='g')
            # plot axis labels
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')
            # set view angle, with x forward, y right, z up
            ax.view_init(azim=-90, elev=0)
            plt.show()
            
            # plot the robot only
            fig = plt.figure(figsize=(12, 12))
            ax = fig.add_subplot(projection='3d')
            points = image_to_pointcloud(depth_map, "frontview", 256, 256, obs['frontview_segmentation_robot_only'])
            ax.scatter([x[0] for x in points], [x[1] for x in points], [x[2] for x in points], s=1)
            # plot axis labels
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')
            # set view angle, with x forward, y right, z up
            ax.view_init(azim=-90, elev=0)
            plt.show()
            
            # An example point on the gripper (red point)
            x, y = 128, 110
            robot_eef = obs['robot0_eef_pos']
            print("Robot eef world coord:", robot_eef)
            eef_site_name = env.robots[0].controller.eef_name
            curr_pos = np.array(env.sim.data.site_xpos[env.sim.model.site_name2id(eef_site_name)])
            print("Roboot end effector world coordinate:", curr_pos)          
            plt.imshow(obs['frontview_depth']); plt.plot(x, y,'ro'); plt.show() # (256, 256, 1)
            
            joint_angles = obs['robot0_joint_pos']
            real_depth_map = camera_utils.get_real_depth_map(env.sim, depth_map)
            # Camera transform matrix to project from camera coordinates to world coordinates.
            extrinsic_matrix = camera_utils.get_camera_extrinsic_matrix(env.sim, camera_name="frontview")
            intrinsic_matrix = camera_utils.get_camera_intrinsic_matrix(env.sim, camera_name="frontview", camera_height=256, camera_width=256)
            # real_coord = camera_utils.transform_from_pixels_to_world(np.array([128, 128]), depth_map, np.linalg.inv(extrinsic_matrix))
            coord_cam_frame = np.array([(x-intrinsic_matrix[0, -1])/intrinsic_matrix[0, 0], (y-intrinsic_matrix[1, -1])/intrinsic_matrix[1, 1], 1]) * real_depth_map[y, x]
            coord_world_frame = np.dot(extrinsic_matrix, np.concatenate((coord_cam_frame, [1])))
            print("red point world coordinate:", coord_world_frame)
            
            # Robot base
            print("Robot base world coord:", env.robots[0].robot_model._elements["root_body"].get("pos"))
            # pixel position of env.robots[0].robot_model._elements["root_body"].get("pos")
            base_world_coord = np.concatenate(([float(x) for x in env.robots[0].robot_model._elements["root_body"].get("pos").split(" ")], [1]))
            base_cam_coord = np.dot(np.linalg.inv(extrinsic_matrix), base_world_coord)
            base_pixel_coord = np.dot(intrinsic_matrix, base_cam_coord[:-1])
            base_pixel_coord = base_pixel_coord / base_pixel_coord[-1]
            # print(base_pixel_coord)
            plt.imshow(obs['frontview_depth']); plt.plot(base_pixel_coord[0],base_pixel_coord[1], 'bo'); plt.show() # (256, 256, 1)            
            x, y = int(base_pixel_coord[0]), int(base_pixel_coord[1])
            coord_cam_frame = np.array([(x-intrinsic_matrix[0, -1])/intrinsic_matrix[0, 0], (y-intrinsic_matrix[1, -1])/intrinsic_matrix[1, 1], 1]) * real_depth_map[y, x]
            coord_world_frame = np.dot(extrinsic_matrix, np.concatenate((coord_cam_frame, [1])))
            print("Robot base reprojected world coordinate:", coord_world_frame)
            
            
            # breakpoint()
            val = env.sim.render(height=512, width=512, camera_name="frontview")
            # plt.imshow(val); plt.show()

    env.close_renderer()
    print("Done.")
