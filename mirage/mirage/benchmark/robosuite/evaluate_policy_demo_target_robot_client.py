from PIL import Image
import argparse
import struct
import numpy as np
from copy import deepcopy
import socket, pickle
import time
import cv2
import os
import robomimic.utils.tensor_utils as TensorUtils
import robomimic.utils.obs_utils as ObsUtils
from robomimic.envs.env_base import EnvBase
import robosuite.utils.transform_utils as T
import robosuite.utils.camera_utils as camera_utils

from evaluate_policy_demo_source_robot_server import Data, Robot

class TargetRobot(Robot):
    def __init__(self, robot_name=None, ckpt_path=None, render=False, video_path=None, rollout_horizon=None, seed=None, dataset_path=None, connection=None, port = 50007, passive=False, demo_path=None, inpaint_enabled=False, offline_eval=False, save_paired_images=False, save_paired_images_folder_path=None, use_diffusion=False, use_ros=False, diffusion_input=None, device=None, save_failed_demos=False, gripper_types=None, naive=None, save_stats_path=None):
        super().__init__(robot_name=robot_name, ckpt_path=ckpt_path, render=render, video_path=video_path, rollout_horizon=rollout_horizon, seed=seed, dataset_path=dataset_path, demo_path=demo_path, inpaint_enabled=inpaint_enabled, save_paired_images=save_paired_images, save_paired_images_folder_path=save_paired_images_folder_path, device=device, save_failed_demos=save_failed_demos, gripper_types=gripper_types, save_stats_path=save_stats_path)
        
        if connection:
            HOST = 'localhost'
            PORT = port
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((HOST, PORT))
        else:
            self.s = None
            
        self.passive = passive
        self.naive = naive
        
        self.offline_eval = offline_eval
        self.use_diffusion = use_diffusion
        self.use_ros = use_ros
        self.diffusion_input = diffusion_input
        if self.inpaint_enabled:
            if not self.offline_eval:
                if self.use_ros:
                    from mirage.infra.ros_inpaint_publisher_sim import ROSInpaintPublisherSim
                    self.ros_inpaint_publisher = ROSInpaintPublisherSim()                    
                if self.use_diffusion:
                    from mirage.mirage.diffusion.controlnet import ControlNet
                    self.controlnet = ControlNet()
                    assert self.diffusion_input is not None, "Please specify diffusion input: analytic/masked/target_robot"
                    assert self.diffusion_input in ["analytic", "masked", "target_robot"], "Unknown diffusion input type. Please specify diffusion input: analytic/masked/target_robot"
                    if self.diffusion_input == "analytic":
                        assert self.use_ros, "Diffusion input analytic requires ROS"
                    elif self.diffusion_input == "masked":
                        if self.use_ros:
                            print("Use the analytic Franka masks")
                        else:
                            print("NOT USING ROS! Will use the groundtruth Franka masks instead")                        
    
    def image_to_pointcloud(self, depth_map, camera_name, camera_height=84, camera_width=84, segmask=None):
        """
        Convert depth image to point cloud
        """
        real_depth_map = camera_utils.get_real_depth_map(self.env.env.sim, depth_map)
        # Camera transform matrix to project from camera coordinates to world coordinates.
        extrinsic_matrix = camera_utils.get_camera_extrinsic_matrix(self.env.env.sim, camera_name=camera_name)
        intrinsic_matrix = camera_utils.get_camera_intrinsic_matrix(self.env.env.sim, camera_name=camera_name, camera_height=camera_height, camera_width=camera_width)

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
    
    def rollout_robot(self, video_skip=5, return_obs=False, camera_names=None, set_object_state=False, set_robot_pose=False, tracking_error_threshold=0.003, num_iter_max=100, target_robot_delta_action=False, demo_index=0):
        
        assert isinstance(self.env, EnvBase)
        
        self.initialize_robot()
        
        if self.save_paired_images:            
            os.makedirs(os.path.join(self.save_paired_images_folder_path, "{}_rgb".format(self.robot_name.lower()), str(demo_index)), exist_ok=True)
            os.makedirs(os.path.join(self.save_paired_images_folder_path, "{}_mask".format(self.robot_name.lower()), str(demo_index)), exist_ok=True)
            os.makedirs(os.path.join(self.save_paired_images_folder_path, "{}_ee_pose".format(self.robot_name.lower()), str(demo_index)), exist_ok=True)
            os.makedirs(os.path.join(self.save_paired_images_folder_path, "{}_joint_gripper_pose".format(self.robot_name.lower()), str(demo_index)), exist_ok=True)
            os.makedirs(os.path.join(self.save_paired_images_folder_path, "{}_depth".format(self.robot_name.lower()), str(demo_index)), exist_ok=True)
        
        # the target robot needs to be first initialized to the source object state and source robot pose
        # receive source object state and source robot pose from source robot
        if self.s is not None:
            pickled_message_size = self._receive_all_bytes(4)
            message_size = struct.unpack("!I", pickled_message_size)[0]
            data = self._receive_all_bytes(message_size)
            source_env_robot_state = pickle.loads(data)
            print("Receiving source object state and source robot pose from source robot")
            assert source_env_robot_state.message == "Ready"
            self.set_object_state(set_to_target_object_state=source_env_robot_state.object_state)
            self.drive_robot_to_target_pose(source_env_robot_state.robot_pose)
            
            # tell the source robot that the target robot is ready
            # Create an instance of Data() to send to client.
            variable = Data()
            variable.message = "Ready"
            # Pickle the object and send it to the server
            data_string = pickle.dumps(variable)
            message_length = struct.pack("!I", len(data_string))
            self.s.send(message_length)
            self.s.send(data_string)
        
        video_count = 0  # video frame counter
        total_reward = 0.
        state_dict = self.env.get_state()
        traj = dict(actions=[], rewards=[], dones=[], states=[], initial_state_dict=state_dict)
        if return_obs:
            # store observations too
            traj.update(dict(obs=[], next_obs=[]))
        
        source_finished_step = None
        has_succeeded = False
        trajectory_timestep_infos = []
        # try:
        for step_i in range(self.rollout_horizon):
            print("Target Step: ", step_i)
            # state_dict and obs are before taking the action
            state_dict = self.env.get_state()
            # print("State dict: ", state_dict)
            obs = deepcopy(self.obs)
            # import matplotlib.pyplot as plt; plt.imshow(obs["agentview_image"]); plt.show()
            if not self.passive:
                # send state_dict and obs to source robot
                # Create an instance of Data() to send to client.
                variable = Data()
                # variable.obs = obs
                variable.object_state = self.get_object_state()
                variable.robot_pose = self.compute_eef_pose()
                variable.message = "Request for Action"
                
                if self.save_paired_images:
                    # save the rgb image and segmentation mask
                    rgb_img = obs['agentview_image']
                    rgb_img = rgb_img.transpose(1, 2, 0)
                    segmentation_mask = obs['agentview_segmentation_robot_only']
                    segmentation_mask = cv2.flip(segmentation_mask, 0)
                    depth_normalized = obs['agentview_depth']
                    depth_normalized = cv2.flip(depth_normalized, 0)
                    depth_img = camera_utils.get_real_depth_map(self.env.env.sim, depth_normalized)
                    # save the rgb image
                    cv2.imwrite(os.path.join(self.save_paired_images_folder_path, "{}_rgb".format(self.robot_name.lower()), str(demo_index), "{}.jpg".format(step_i)), cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR) * 255)
                    # save the segmentation mask
                    cv2.imwrite(os.path.join(self.save_paired_images_folder_path, "{}_mask".format(self.robot_name.lower()), str(demo_index), "{}.jpg".format(step_i)), segmentation_mask * 255)
                    # save the EE pose
                    with open(os.path.join(self.save_paired_images_folder_path, "{}_ee_pose".format(self.robot_name.lower()), str(demo_index), "{}.txt".format(step_i)), "w") as f:
                        f.write(str(np.concatenate([self.compute_eef_pose(), obs['robot0_gripper_qpos']])))
                    # save the joint angles and gripper pose
                    with open(os.path.join(self.save_paired_images_folder_path, "{}_joint_gripper_pose".format(self.robot_name.lower()), str(demo_index), "{}.txt".format(step_i)), "w") as f:
                        f.write(str(np.concatenate([obs['robot0_joint_pos'], obs['robot0_gripper_qpos']])))
                    # save the depth map
                    np.save(os.path.join(self.save_paired_images_folder_path, "{}_depth".format(self.robot_name.lower()), str(demo_index), "{}.npy".format(step_i)), depth_img)

                if self.inpaint_enabled:
                    joint_angles = obs['robot0_joint_pos']
                    # because we've modified `get_observation` (Line 187) of env_robosuite.py such that all rgb images are flipped and channel swapped,
                    # they are now 3, H, W and not upside down (which is what the policy wants), but the segmentation mask is still upside down and H, W, 1
                    rgb_img = obs['agentview_image']
                    rgb_img = rgb_img.transpose(1, 2, 0)
                    segmentation_mask = obs['agentview_segmentation_robot_only']
                    segmentation_mask = cv2.flip(segmentation_mask, 0) # need this (flip vertically) unless we change macros.IMAGE_CONVENTION = "opencv" from "opengl"

                    depth_normalized = obs['agentview_depth']
                    depth_normalized = cv2.flip(depth_normalized, 0)

                    depth_img = camera_utils.get_real_depth_map(self.env.env.sim, depth_normalized)

                    points = self.image_to_pointcloud(depth_normalized, "agentview", 84, 84, segmask=None) # may need to change to 256, 256
                    timestep_info_dict = {
                        "target_robot": {
                            "agentview": {
                                "rgb": rgb_img, #np.array(Image.fromarray((rgb_img * 255).astype(np.uint8)).resize((84, 84))).astype(np.float32) / 255.0,
                                "seg": segmentation_mask,
                                "real_depth_map": depth_img,
                                "points": points,
                                "extrinsic_matrix": camera_utils.get_camera_extrinsic_matrix(self.env.env.sim, camera_name="agentview"),
                                "intrinsic_matrix": camera_utils.get_camera_intrinsic_matrix(self.env.env.sim, camera_name="agentview", camera_height=84, camera_width=84),
                            },
                            "low_dim": {
                                "joint_angles": joint_angles,
                                "robot_eef_pos": obs['robot0_eef_pos'],
                                "robot_eef_quat": obs['robot0_eef_quat'],
                                "robot0_gripper_qpos": obs['robot0_gripper_qpos']
                            }
                        }
                    }
                    
                    cv2.imwrite(f"{self.save_stats_path}/rgb.png", cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR) * 255)
                    
                    if not self.offline_eval:
                        inpainted_image = np.zeros((256, 256, 3), dtype=np.uint8)                        
                        sent_joint_angles = np.concatenate([joint_angles, obs['robot0_gripper_qpos'][-1:]])
                        ros_rgb_img = (rgb_img * 255).astype(np.uint8)
                        ros_depth_img = depth_img.astype(np.float64)
                        ros_segmentation_mask = np.repeat(segmentation_mask[:,:,np.newaxis],3,axis=2).astype(np.uint8)
                        if self.use_ros:
                            print("Publishing")
                            from mirage.infra.ros_inpaint_publisher_sim import ROSInpaintSimData
                            eef_pose = self.compute_eef_pose()
                            eef_pose_matrix = T.pose2mat((eef_pose[:3], eef_pose[3:]))
                            data = ROSInpaintSimData(ros_rgb_img, ros_depth_img, ros_segmentation_mask, eef_pose_matrix, obs['robot0_gripper_qpos'][-1:])
                            print("Joints including gripper", sent_joint_angles)
                            self.ros_inpaint_publisher.publish_to_ros_node(data)
                            inpainted_image = self.ros_inpaint_publisher.get_inpainted_image(True)
                            inpainted_image = inpainted_image.astype(np.float32) / 255.0
                            print("Received inpainted image")

                        if self.naive:
                            inpainted_image = rgb_img                     
                        
                        if self.use_diffusion:
                            if self.diffusion_input == "target_robot":
                                inpainted_image_256, inpainted_image_84 = self.controlnet.inpaint(rgb_img)
                                diffusion_input = rgb_img.copy()
                            elif self.diffusion_input == "analytic":
                                inpainted_image_256, inpainted_image_84 = self.controlnet.inpaint(inpainted_image)
                                diffusion_input = inpainted_image.copy()
                            elif self.diffusion_input == "masked":
                                if self.use_ros:
                                    segmentation_mask_target_robot = segmentation_mask
                                    segmentation_mask_source_robot = inpainted_image
                                    masked_image = mask_rgb_image(rgb_img, segmentation_mask_target_robot, segmentation_mask_source_robot)
                                else:
                                    source_robot_info = np.load(self.groundtruth_and_inpaintedprediction_path, allow_pickle=True).item()
                                    segmentation_mask_target_robot = segmentation_mask
                                    segmentation_mask_source_robot = source_robot_info["ground_truth"]["segmentation_mask"]
                                    masked_image = mask_rgb_image(rgb_img, segmentation_mask_target_robot, segmentation_mask_source_robot)
                                diffusion_input = masked_image.copy()
                                cv2.imwrite(f"{self.save_stats_path}/masked_image.png", cv2.cvtColor(masked_image, cv2.COLOR_RGB2BGR) * 255)
                                inpainted_image_256, inpainted_image_84 = self.controlnet.inpaint(masked_image)
                            
                            inpainted_image = inpainted_image_256
                    np.save(self.inpainted_img_path, inpainted_image, allow_pickle=True)
                    if self.use_diffusion:
                        np.save(self.diffusion_model_input_path, diffusion_input, allow_pickle=True)
                    cv2.imwrite(self.inpainted_rgb_img_path, cv2.cvtColor(inpainted_image, cv2.COLOR_RGB2BGR) * 255)
                    if self.inpaint_writer is not None:
                        self.inpaint_writer.append_data((inpainted_image * 255).astype(np.uint8))


                # Pickle the object and send it to the server
                data_string = pickle.dumps(variable)
                message_length = struct.pack("!I", len(data_string))
                self.s.send(message_length)
                self.s.send(data_string)
            
                
            # receive target object state and target robot pose from target robot
            if self.s is not None:
                pickled_message_size = self._receive_all_bytes(4)
                message_size = struct.unpack("!I", pickled_message_size)[0]
                data = self._receive_all_bytes(message_size)
                source_env_robot_state = pickle.loads(data)
                assert source_env_robot_state.message == "Respond with Action", "Wrong Synchronization"
                # print("Received actions")
                if self.inpaint_enabled:
                    timestep_info_dict["source_robot"] = np.load(self.groundtruth_and_inpaintedprediction_path, allow_pickle=True).item()
                if source_env_robot_state.done:
                    print("Source robot is done")
                if source_env_robot_state.success:
                    print("Source robot is successful")
                    if source_finished_step is None:
                        source_finished_step = step_i

            if target_robot_delta_action:
                # print("Executing delta action")
                action = source_env_robot_state.action
                if self.inpaint_enabled:
                    inpaint_action = timestep_info_dict["source_robot"]["inpainting"]["predicted_action"]
                    timestep_info_dict["ground_truth_action"] = action
                    timestep_info_dict["inpaint_action"] = inpaint_action
                    # online eval uses the inpaint action
                    if not self.offline_eval:
                        print("Inpaint action: ", inpaint_action)
                        print("Ground truth action: ", action)
                        print("Use inpaint action")
                        action = inpaint_action
                action, r, done, success = self.step(action, use_delta=True, goal_pose=source_env_robot_state.robot_pose, name="Target Robot")
            else:
                # print("Executing action")
                if self.num_robots == 1:
                    action = source_env_robot_state.robot_pose # get action from the source robot
                    # append gripper action
                    action = np.concatenate([action, source_env_robot_state.action[-1:]])
                    if self.inpaint_enabled:
                        inpaint_action = timestep_info_dict["source_robot"]["inpainting"]["predicted_state"][:7] # only get position and quarternion of the target state and not the gripper part
                        inpaint_action = np.concatenate([inpaint_action, timestep_info_dict["source_robot"]["inpainting"]["predicted_action"][-1:]])

                        inpaint_action = timestep_info_dict["source_robot"]["ground_truth"]["target_state"][:7] # only get position and quarternion of the target state and not the gripper part
                        inpaint_action = np.concatenate([inpaint_action, timestep_info_dict["source_robot"]["inpainting"]["predicted_action"][-1:]])

                        predicted_state_with_gt_action = np.concatenate([timestep_info_dict["source_robot"]["inpainting"]["predicted_state_from_gt"][:7], action[-1:]])
                        
                        timestep_info_dict["ground_truth_action"] = action
                        timestep_info_dict["inpaint_action"] = inpaint_action
                        # online eval uses the inpaint action
                        if not self.offline_eval:
                            print("Inpaint action: ", inpaint_action)
                            print("Ground truth action: ", action)
                            action = inpaint_action
                            print("Use predicted_state_with_gt_action action")
                            # print("Predicted from gt action: ", predicted_state_with_gt_action)
                            action = predicted_state_with_gt_action
                else:
                    action_0, action_1 = source_env_robot_state.robot_pose[:7], source_env_robot_state.robot_pose[7:]
                    # append gripper action
                    action = np.concatenate([action_0, source_env_robot_state.action[6:7], action_1, source_env_robot_state.action[-1:]])
                    if self.inpaint_enabled:
                        raise NotImplementedError
                    
                action, r, done, success = self.step(action, use_delta=False, blocking=True, tracking_error_threshold=tracking_error_threshold, num_iter_max=num_iter_max, name="Target Robot")
            
            if self.inpaint_enabled:
                trajectory_timestep_infos.append(timestep_info_dict)

                # if the file does not exist:
                if not os.path.exists(self.inpaint_data_for_analysis_path_temp):
                    # create the file and save the trajectory_timestep_infos
                    np.save(self.inpaint_data_for_analysis_path_temp, [trajectory_timestep_infos], allow_pickle=True)
                # else, append the timestep_info_dict to the last trajectory in the file
                else:
                    trajectory_timestep_infos_temp = np.load(self.inpaint_data_for_analysis_path_temp, allow_pickle=True)
                    trajectory_timestep_infos_temp = trajectory_timestep_infos_temp.tolist()
                    trajectory_timestep_infos_temp[-1].append(timestep_info_dict)
                    np.save(self.inpaint_data_for_analysis_path_temp, trajectory_timestep_infos_temp, allow_pickle=True)
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
            if done or success:
                print("Done: ", done, "Success: ", success)
            # Pickle the object and send it to the server
            data_string = pickle.dumps(variable)
            message_length = struct.pack("!I", len(data_string))
            self.s.send(message_length)
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
            if not target_robot_delta_action:
                # save the 3D rotation instead of the 4D quaternion since that is the default input to osc absolute pose controller
                action_target = np.zeros(7)
                action_target[:3] = action[:3]
                action_target[3:6] = T.quat2axisangle(action[3:7])
                action_target[-1] = action[-1]
                action = action_target
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
                    if source_env_robot_state.done and self.use_demo:
                        print("Source robot is successful. Target robot is not successful. Demo exhausted")
                        break
                elif source_env_robot_state.done:
                    if done:
                        print("Target robot is done")
                        break
                    if has_succeeded:
                        print("Target robot is successful")
                        break
                    if self.use_demo:
                        print("Source robot is done. Target robot is not successful. Demo exhausted")
                        break
        
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

        return stats, traj, trajectory_timestep_infos
    
    def _receive_all_bytes(self, num_bytes: int) -> bytes:
        """
        Receives all the bytes.
        :param num_bytes: The number of bytes.
        :return: The bytes.
        """
        data = bytearray(num_bytes)
        pos = 0
        while pos < num_bytes:
            cr = self.s.recv_into(memoryview(data)[pos:])
            if cr == 0:
                raise EOFError
            pos += cr
        return data

def mask_rgb_image(rgb_image, mask1, mask2):
    # Create a combined mask of the union of mask1 and mask2
    combined_mask = np.logical_or(mask1, mask2)
    
    # Apply the combined mask to the RGB image
    # Set RGB values to one where the combined mask is True
    masked_image = np.where(np.expand_dims(combined_mask, axis=-1), np.ones_like(rgb_image), rgb_image)
    
    return masked_image

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Path to trained model
    parser.add_argument(
        "--agent",
        type=str,
        default=None,
        help="(optional) path to saved checkpoint pth file",
    )

    # Path to demo file
    parser.add_argument(
        "--demo_path",
        type=str,
        default=None,
        help="(optional) path to saved demo hdf5 file",
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
        "--device",
        type=str,
        default=None,
        help="(optional) set device for execution",
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
    parser.add_argument(
        "--inpaint_enabled",
        action='store_true',
        help="if True, pass inpainted images to the policy",
    )
    parser.add_argument(
        "--offline_eval",
        action='store_true',
        help="only relevant for inpaint_enabled. If True, does not really use inpainted images but instead uses the ground truth images for target robot stepping, but still record the differences in actions between the ground truth and inpainted images",
    )
    parser.add_argument(
        "--save_paired_images",
        action='store_true',
        help="if True, save paired images and masks",
    )
    parser.add_argument(
        "--save_paired_images_folder_path",
        type=str,
        default=None,
        help="directory of the folder to save paired images and masks",
    )    
    parser.add_argument(
        "--use_diffusion",
        action='store_true',
        help="only relevant for inpaint_enabled. If True, uses the diffusion model for inpainting",
    )
    parser.add_argument(
        "--use_ros",
        action='store_true',
        help="only relevant for inpaint_enabled. If True, use ROS for inpainting",
    )
    parser.add_argument(
        "--diffusion_input",
        type=str,
        default=None,
        help="One of the following: [analytic, masked, target_robot]",
    )
    parser.add_argument(
        "--save_failed_demos",
        action='store_true',
        help="Set this to true to also save demos that failed",
    )
    parser.add_argument(
        "--gripper",
        type=str,
        default=None,
        help="provide the name of the gripper to be used, such as PandaGripper or Robotiq85Gripper"
    )
    parser.add_argument(
        "--naive",
        action='store_true',
        help="Set this to true to use naive (no inpainting)",
    )
    args = parser.parse_args()
    
    
   
    time.sleep(4) # wait for the server to start
    target_robot = TargetRobot(robot_name=args.robot_name, ckpt_path=args.agent, render=args.render, video_path=args.video_path, rollout_horizon=args.horizon, dataset_path=args.dataset_path, passive=args.passive, port=args.port, connection=args.connection, demo_path=args.demo_path, inpaint_enabled=args.inpaint_enabled, offline_eval=args.offline_eval, save_paired_images=args.save_paired_images, save_paired_images_folder_path=args.save_paired_images_folder_path, use_diffusion=args.use_diffusion, use_ros=args.use_ros, diffusion_input=args.diffusion_input, device=args.device, save_failed_demos=args.save_failed_demos, gripper_types=args.gripper, naive=args.naive, save_stats_path=args.save_stats_path)
    target_robot.run_experiments(seeds=args.seeds, rollout_num_episodes=args.n_rollouts, video_skip=args.video_skip, camera_names=args.camera_names, dataset_obs=args.dataset_obs, save_stats_path=args.save_stats_path, tracking_error_threshold=args.tracking_error_threshold, num_iter_max=args.num_iter_max, target_robot_delta_action=args.delta_action, inpaint_online_eval=not target_robot.offline_eval)

