

"""
# Mode 1: Target robot following the source robot
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 1 --horizon 400 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_lift_low_dim_2.mp4 --robot_name Sawyer --passive --connection

# Mode 2: Target robot querying the source robot for actions
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 1 --horizon 400 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_lift_low_dim_2.mp4 --robot_name Sawyer --connection
"""




import argparse
import json
import h5py
import imageio
import numpy as np
from copy import deepcopy
import socket, pickle
from scipy.spatial.transform import Rotation
import torch
import time
import cv2

import robomimic
import robomimic.utils.file_utils as FileUtils
import robomimic.utils.torch_utils as TorchUtils
import robomimic.utils.tensor_utils as TensorUtils
import robomimic.utils.obs_utils as ObsUtils
from robomimic.envs.env_base import EnvBase
from robomimic.algo import RolloutPolicy
import robosuite.utils.transform_utils as T
from robosuite.utils.mjcf_utils import array_to_string, string_to_array
import robosuite.utils.camera_utils as camera_utils


from evaluate_policy_source_robot_server import Data, Robot

# from xembody.src.general.ros_inpaint_publisher import ROSInpaintPublisher


class TargetRobot(Robot):

    CAMERA_HEIGHT = 84
    CAMERA_WIDTH = 84


    def __init__(self, robot_name=None, ckpt_path=None, render=False, video_path=None, rollout_horizon=None, seed=None, dataset_path=None, connection=None, port = 50007, passive=False):
        super().__init__(robot_name=robot_name, ckpt_path=ckpt_path, render=render, video_path=video_path, rollout_horizon=rollout_horizon, seed=seed, dataset_path=dataset_path)
        
        if connection:
            HOST = 'localhost'
            PORT = port
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((HOST, PORT))
        else:
            self.s = None
            
        self.passive = passive
        # self.ros_inpaint_publisher = ROSInpaintPublisher()


    def image_to_pointcloud(self, depth_map, camera_name, camera_height, camera_width, segmask=None):
        """
        Convert depth image to point cloud
        """
        real_depth_map = camera_utils.get_real_depth_map(self.env.env.sim, depth_map)
        # Camera transform matrix to project from camera coordinates to world coordinates.
        extrinsic_matrix = camera_utils.get_camera_extrinsic_matrix(self.env.env.sim, camera_name=camera_name)
        print('cam name: ', camera_name, ' extrinsic_matrix: ', extrinsic_matrix)
        intrinsic_matrix = camera_utils.get_camera_intrinsic_matrix(self.env.env.sim, camera_name=camera_name, camera_height=camera_height, camera_width=camera_width)
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

    def rollout_robot(self, video_skip=5, return_obs=False, camera_names=None, set_object_state=False, set_robot_pose=False, tracking_error_threshold=0.003, num_iter_max=100, target_robot_delta_action=False):
        
        assert isinstance(self.env, EnvBase)
        
        self.initialize_robot()
        
        if True: #self.passive:
            # the target robot needs to be first initialized to the source object state and source robot pose
            # receive source object state and source robot pose from source robot
            if self.s is not None:
                data = self.s.recv(4096)
                source_env_robot_state = pickle.loads(data)
                print("Receiving source object state and source robot pose from source robot")
                assert source_env_robot_state.message == "Ready"
                
                self.set_object_state(set_to_target_object_state=source_env_robot_state.object_state)
                self.drive_robot_to_target_pose(source_env_robot_state.robot_pose)
                
                # tell the source robot that the target robot is ready
                # Create an instance of Data() to send to client.
                variable = Data()
                variable.message = "Ready"
                variable.rgb_image = ""#obs['agentview_image']
                # Pickle the object and send it to the server
                data_string = pickle.dumps(variable)
                self.s.send(data_string)
        else:
            # the target robot is ready to execute the policy
            if self.s is not None:
                # tell the source robot that the target robot is ready
                # Create an instance of Data() to send to client.
                variable = Data()
                variable.object_state = self.get_object_state()
                variable.robot_pose = self.compute_eef_pose()
                variable.rgb_image = ""#obs['agentview_image']
                variable.message = "Ready"
                # Pickle the object and send it to the server
                data_string = pickle.dumps(variable)
                self.s.send(data_string)     
                
                # confirm that the source robot is ready
                data = self.s.recv(4096)
                source_env_robot_state = pickle.loads(data)
                assert source_env_robot_state.message == "Ready", "The source robot is not ready"
        
        video_count = 0  # video frame counter
        total_reward = 0.
        state_dict = self.env.get_state()
        traj = dict(actions=[], rewards=[], dones=[], states=[], initial_state_dict=state_dict)
        if return_obs:
            # store observations too
            traj.update(dict(obs=[], next_obs=[]))
        
        source_finished_step = None
        has_succeeded = False
        all_data = []
        # try:
        for step_i in range(self.rollout_horizon):
            obs = self.env.env._get_observations()
            print("Target Step: ", step_i)
            # state_dict and obs are before taking the action
            state_dict = self.env.get_state()
            # print("State dict: ", state_dict)
            # obs = deepcopy(self.obs)
            
            joints = obs['robot0_joint_pos']

            segmentation_mask = obs['agentview_segmentation_robot_only']
            segmentation_mask = cv2.flip(segmentation_mask, 0)

            rgb_img = obs['agentview_image']
            rgb_img = cv2.flip(rgb_img, 0)

            depth_normalized = obs['agentview_depth']
            depth_normalized = cv2.flip(depth_normalized, 0)

            depth_img = camera_utils.get_real_depth_map(self.env.env.sim, depth_normalized)

            points = self.image_to_pointcloud(depth_normalized, "agentview", TargetRobot.CAMERA_HEIGHT, TargetRobot.CAMERA_WIDTH, segmask=None)
            output_dict = {
                "agentview": {
                    "rgb": rgb_img,
                    "seg": segmentation_mask,
                    "real_depth_map": depth_img,
                    "points": points,
                    "extrinsic_matrix": camera_utils.get_camera_extrinsic_matrix(self.env.env.sim, camera_name="agentview"),
                    "intrinsic_matrix": camera_utils.get_camera_intrinsic_matrix(self.env.env.sim, camera_name="agentview", camera_height=TargetRobot.CAMERA_HEIGHT, camera_width=TargetRobot.CAMERA_WIDTH),
                },
                "joint_angles": joints,
                "robot_eef_pos": obs['robot0_eef_pos'],
                "robot_eef_quat": obs['robot0_eef_quat'],
                "robot0_gripper_qpos": obs['robot0_gripper_qpos']
            }
            # import matplotlib.pyplot as plt
            # inpainted_image = plt.imread(f"/home/lawrence/xembody/xembody/xembody_robosuite/image_inpainting/data/results_color_threshold_skimage5/inpaint{step_i}.png")
            # np.save(f"inpaint_img.npy", inpainted_image, allow_pickle=True)
            # np.save(f"output.npy", output_dict, allow_pickle=True)

            # self.ros_inpaint_publisher.publish_to_ros_node(rgb_img, points, segmentation_mask, joints)

            # inpainted_img = self.ros_inpaint_publisher.get_inpainted_image(True)
            # obs['agentview_image'] = inpainted_img
            
            if not self.passive:
                # send state_dict and obs to source robot
                # Create an instance of Data() to send to client.
                variable = Data()
                # variable.obs = obs
                variable.object_state = self.get_object_state()
                variable.robot_pose = self.compute_eef_pose()
                variable.rgb_image = ""#obs['agentview_image']
                variable.message = "Request for Action"
                # Pickle the object and send it to the server
                data_string = pickle.dumps(variable)
                if self.s is not None:
                    self.s.send(data_string)
                
                # print("Request for Action")
            
                
            # receive target object state and target robot pose from target robot
            if self.s is not None:
                # breakpoint()
                data = self.s.recv(4096)
                source_env_robot_state = pickle.loads(data)
                assert source_env_robot_state.message == "Respond with Action", "Wrong Synchronization"
                # print("Received actions")
                output_dict["ground_truth_source_robot"] = np.load(source_env_robot_state.rgb_image, allow_pickle=True).item()
                all_data.append(output_dict)
                if source_env_robot_state.done:
                    print("Source robot is done")
                    # break
                if source_env_robot_state.success:
                    print("Source robot is successful")
                    if source_finished_step is None:
                        source_finished_step = step_i
                    # break
            # if set_object_state:
            #     self.set_object_state(set_to_target_object_state=source_env_robot_state.object_state)
            # if set_robot_pose:
            #     self.drive_robot_to_target_pose(source_env_robot_state.robot_pose)
                
            if target_robot_delta_action:
                # print("Executing delta action")
                action = source_env_robot_state.action
                action, r, done, success = self.step(action, use_delta=True, goal_pose=source_env_robot_state.robot_pose)
            else:
                # print("Executing action")
                action = source_env_robot_state.robot_pose # get action from the source robot
                # append gripper action
                action = np.concatenate([action, source_env_robot_state.action[-1:]])
                output_dict["ground_truth_action"] = source_env_robot_state.action
                output_dict["ground_truth_target_robot_pose"] = source_env_robot_state.robot_pose
                action, r, done, success = self.step(action, use_delta=False, blocking=True, tracking_error_threshold=tracking_error_threshold, num_iter_max=num_iter_max)
            if success:
                has_succeeded = True
            next_obs = deepcopy(self.obs)
            total_reward += r
            
            # if the source robot has succeeded, allow 10 more steps for the target robot to finish so we can terminate early
            if source_finished_step is not None and self.passive:
                if step_i - source_finished_step >= 10:
                    done = True
            
            # tell the source robot that the target robot is ready
            # Create an instance of Data() to send to client.
            variable = Data()
            variable.message = "OK"
            variable.done = done
            variable.success = has_succeeded
            variable.rgb_image = ""#obs['agentview_image']
            if done or success:
                print("Done: ", done, "Success: ", success)
            # Pickle the object and send it to the server
            data_string = pickle.dumps(variable)
            self.s.send(data_string)
            
            
            
            # visualization
            if self.render:
                self.env.render(mode="human", camera_name=camera_names[0]) # on-screen rendering can only support one camera
            if self.write_video:
                if video_count % video_skip == 0:
                    video_img = []
                    for cam_name in camera_names:
                        video_img.append(self.env.render(mode="rgb_array", height=512, width=512, camera_name=cam_name))
                    video_img = np.concatenate(video_img, axis=1) # concatenate horizontally
                    self.video_writer.append_data(video_img)

                video_count += 1

            # collect transition
            traj["actions"].append(action)
            traj["rewards"].append(r)
            traj["dones"].append(done)
            traj["states"].append(state_dict["states"])
            if return_obs:
                # Note: We need to "unprocess" the observations to prepare to write them to dataset.
                #       This includes operations like channel swapping and float to uint8 conversion
                #       for saving disk space.
                traj["obs"].append(ObsUtils.unprocess_obs_dict(obs))
                traj["next_obs"].append(ObsUtils.unprocess_obs_dict(next_obs))
                
            
            # break if done or if success
            if not self.passive:
                if done:
                    print("Target robot is done")
                    break
                if success:
                    print("Target robot is successful")
                    break
            else:
                # break if source robot has succeeded and either the target robot has succeeded or it is done (>10 steps after source robot has succeeded)
                # or break if the target robot has succeeded or the source robot is done (>10 steps after target robot has succeeded)
                if source_finished_step is not None:
                    if done:
                        print("Target robot is done")
                        break
                    if has_succeeded:
                        print("Target robot is successful")
                        break
                elif source_env_robot_state.done:
                    if done:
                        print("Target robot is done")
                        break
                    if has_succeeded:
                        print("Target robot is successful")
                        break
        # except:
        #     if self.env.rollout_exceptions:
        #         print("WARNING: got target robot rollout exception {}".format(self.env.rollout_exceptions))

        
        stats = dict(Return=total_reward, Horizon=(step_i + 1), Success_Rate=float(has_succeeded))
            

        if return_obs:
            # convert list of dict to dict of list for obs dictionaries (for convenient writes to hdf5 dataset)
            traj["obs"] = TensorUtils.list_of_flat_dict_to_dict_of_list(traj["obs"])
            traj["next_obs"] = TensorUtils.list_of_flat_dict_to_dict_of_list(traj["next_obs"])
            
            
        # list to numpy array
        for k in traj:
            if k == "initial_state_dict":
                continue
            if isinstance(traj[k], dict):
                for kp in traj[k]:
                    traj[k][kp] = np.array(traj[k][kp])
            else:
                traj[k] = np.array(traj[k])

        np.save(f"one_trajectory_source_target_with_inpainted_{self.task_name}_{self.s.getsockname()[1]}.npy", all_data, allow_pickle=True)
        return stats, traj
    
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Path to trained model
    parser.add_argument(
        "--agent",
        type=str,
        required=True,
        help="path to saved checkpoint pth file",
    )

    # number of rollouts
    parser.add_argument(
        "--n_rollouts",
        type=int,
        default=27,
        help="number of rollouts",
    )

    # maximum horizon of rollout, to override the one stored in the model checkpoint
    parser.add_argument(
        "--horizon",
        type=int,
        default=None,
        help="(optional) override maximum horizon of rollout from the one in the checkpoint",
    )

    # Env Name (to override the one stored in model checkpoint)
    parser.add_argument(
        "--env",
        type=str,
        default=None,
        help="(optional) override name of env from the one in the checkpoint, and use\
            it for rollouts",
    )

    # Whether to render rollouts to screen
    parser.add_argument(
        "--render",
        action='store_true',
        help="on-screen rendering",
    )

    # Dump a video of the rollouts to the specified path
    parser.add_argument(
        "--video_path",
        type=str,
        default=None,
        help="(optional) render rollouts to this video file path",
    )

    # How often to write video frames during the rollout
    parser.add_argument(
        "--video_skip",
        type=int,
        default=5,
        help="render frames to video every n steps",
    )

    # camera names to render
    parser.add_argument(
        "--camera_names",
        type=str,
        nargs='+',
        default=["agentview"],
        help="(optional) camera name(s) to use for rendering on-screen or to video",
    )

    # If provided, an hdf5 file will be written with the rollout data
    parser.add_argument(
        "--dataset_path",
        type=str,
        default=None,
        help="(optional) if provided, an hdf5 file will be written at this path with the rollout data",
    )

    # If True and @dataset_path is supplied, will write possibly high-dimensional observations to dataset.
    parser.add_argument(
        "--dataset_obs",
        action='store_true',
        help="include possibly high-dimensional observations in output dataset hdf5 file (by default,\
            observations are excluded and only simulator states are saved)",
    )

    # for seeding before starting rollouts
    parser.add_argument(
        "--seeds",
        type=int,
        nargs='+',
        default=None,
        help="(optional) set seed for rollouts",
    )

    parser.add_argument(
        "--robot_name",
        type=str,
        default=None,
        help="(optional) if provided, there will be a second robot tracking the panda robot where the policy is executed with,\
            [Sawyer, UR5e, Panda, Kinova3, Jaco, IIWA]",
    )
    
    parser.add_argument(
        "--passive",
        action='store_true',
        help="if True, the source robot will be passive and wait for the target robot to send the target object state and target robot pose",
    )
    parser.add_argument(
        "--connection",
        action='store_true',
        help="if True, the source robot will wait for the target robot to connect to it",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=50007,
        help="(optional) port for socket connection",
    )
    parser.add_argument(
        "--save_stats_path",
        type=str,
        default=None,
        help="(optional) if provided, summary stats of the evaluation will be written at this path",
    )
    parser.add_argument(
        "--tracking_error_threshold",
        type=float,
        default=0.003,
        help="(optional) if provided, the source robot will drive to the target pose with this tracking error threshold",
    )
    parser.add_argument(
        "--num_iter_max",
        type=int,
        default=100,
        help="(optional) if provided, the source robot will drive to the target pose with this maximum number of iterations",
    )
    parser.add_argument(
        "--delta_action",
        action='store_true',
        help="if True, execute the same delta action as the source robot",
    )
    args = parser.parse_args()
    
    
   
    time.sleep(2) # wait for the server to start
    target_robot = TargetRobot(robot_name=args.robot_name, ckpt_path=args.agent, render=args.render, video_path=args.video_path, rollout_horizon=args.horizon, dataset_path=args.dataset_path, passive=args.passive, port=args.port, connection=args.connection)
    target_robot.run_experiments(seeds=args.seeds, rollout_num_episodes=args.n_rollouts, video_skip=args.video_skip, camera_names=args.camera_names, dataset_obs=args.dataset_obs, save_stats_path=args.save_stats_path, tracking_error_threshold=args.tracking_error_threshold, num_iter_max=args.num_iter_max, target_robot_delta_action=args.delta_action)

