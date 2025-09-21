import argparse
import pdb
import json
import h5py
import imageio
import numpy as np
from copy import deepcopy
import socket, pickle
from scipy.spatial.transform import Rotation
import torch
import os
import cv2
import struct
import robomimic.utils.file_utils as FileUtils
import robomimic.utils.torch_utils as TorchUtils
import robomimic.utils.tensor_utils as TensorUtils
import robomimic.utils.obs_utils as ObsUtils
from robomimic.envs.env_base import EnvBase
import robomimic.utils.env_utils as EnvUtils
from robomimic.algo import RolloutPolicy
import robosuite.utils.transform_utils as T
from robosuite.wrappers import DomainRandomizationWrapper

from robosuite.utils.mjcf_utils import array_to_string, string_to_array
import robosuite.utils.camera_utils as camera_utils
from mirage.gripper_interpolation.robosuite.gripper_interpolator import GripperInterpolator

TASK_OBJECT_DICT = {"Lift": ["cube_joint0"],
                    "NutAssemblySquare": ["SquareNut_joint0", "RoundNut_joint0"],
                    "PickPlaceCan": ["Milk_joint0", "Bread_joint0", "Cereal_joint0", "Can_joint0"],
                    "ToolHang": ["stand_joint0", "frame_joint0", "tool_joint0"],
                    "TwoArmTransport": ['payload_joint0', 'trash_joint0', 'transport_start_bin_joint0', 'transport_target_bin_joint0', 'transport_trash_bin_joint0', 'transport_start_bin_lid_joint0'],
                    "StackThree_D0": ["cubeA_joint0", "cubeB_joint0", "cubeC_joint0"],
                    "Stack_D0": ["cubeA_joint0", "cubeB_joint0"],
                    "Threading_D0": ["needle_obj_joint0"],
                    "ThreePieceAssembly_D0": ["piece_1_joint0", "piece_2_joint0"],
                    "Square_D0": ["SquareNut_joint0"],
                    "Coffee_D0": ["coffee_pod_joint0", "coffee_machine_joint0", "coffee_machine_lid_main_joint0"]
                    }
import random  
import cv2
import numpy as np
import random

def add_black_patches(
        image: np.ndarray,
        num_patches: int = 10,
        max_patch_size_factor: float = 0.15,
        seed: int | None = None
    ) -> np.ndarray:
    if seed is not None:
        rng = np.random.default_rng(seed)   # ← local, independent RNG
    else:
        rng = np.random.default_rng()
    print(seed, 'seed')
    chw_input = image.shape[0] == 3 and image.ndim == 3
    img = np.transpose(image, (1, 2, 0)).copy() if chw_input else image.copy()

    h, w = img.shape[:2]
    max_side = int(min(h, w) * max_patch_size_factor)
    if max_side < 1:
        return image

    for _ in range(num_patches):
        cx = rng.integers(w // 5, 4 * w // 5)
        cy = rng.integers(0, h // 20)
        half_w = rng.integers(1, max_side + 1)
        half_h = rng.integers(1, max_side + 1)

        x1, x2 = max(cx - half_w, 0), min(cx + half_w, w - 1)
        y1, y2 = max(cy - half_h, 0), min(cy + half_h, h - 1)
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 0), thickness=-1)

    return np.transpose(img, (2, 0, 1)) if chw_input else img

class Data:
    obs = {}
    object_state = np.zeros(7)
    action = np.zeros(7)
    robot_pose = np.zeros(7)
    done = False
    success = False
    message = ""

tracking_error_history = []

class Robot:
    def __init__(self, robot_name=None, ckpt_path=None, render=False, video_path=None, rollout_horizon=None, seed=None, dataset_path=None, demo_path=None, inpaint_enabled=False, save_paired_images=False, save_paired_images_folder_path=None, device=None, save_failed_demos=False, gripper_types=None, save_stats_path=None, add_patches=False):
        """_summary_

        Args:
            robot_name (string, optional): one of [Sawyer, UR5e, Panda, Kinova3, Jaco, IIWA]. If None, then the robot name is read from the checkpoint.
            ckpt_path (string, optional): 
            render (bool, optional): 
            video_path (string, optional): 
            rollout_horizon (int, optional): 
            seed (int, optional): 
            connection (socket, optional):
        """
        
        self.robot_name = robot_name
        self.ckpt_path = ckpt_path
        self.render = render
        self.video_path = video_path
        self.rollout_horizon = rollout_horizon
        self.seed = seed
        self.hdf5_path = demo_path
        self.use_demo = (demo_path is not None) # if True, use demo playback; if false, use source policy
        self.write_video = (video_path is not None)
        self.count_file = os.path.join(os.path.dirname(video_path) if video_path else ".", "execution_count.txt")
        
        # Read current count from file if it exists
    
        # Increment count and write back to file
        self.execution_count = 0
        self.video_writer = imageio.get_writer(f'{self.execution_count}_{video_path}', fps=20) if self.write_video else None
        # Keep count of executions in a file
       
        self.inpaint_writer = imageio.get_writer(os.path.join(os.path.dirname(self.video_path), "inpaint_video.mp4"), fps=20) if self.video_writer is not None else None
        self.save_failed_demos = save_failed_demos
        self.gripper_types = gripper_types
        self.save_stats_path = os.path.dirname(save_stats_path)
        self.add_patches = add_patches

        self.inpaint_enabled = inpaint_enabled
        self.save_paired_images = save_paired_images
        
        if self.inpaint_enabled:
            base_path = os.path.basename(ckpt_path).split(".")[0]

            self.groundtruth_and_inpaintedprediction_path = f"{self.save_stats_path}/groundtruth_source_img_{base_path}.npy"
            self.inpainted_img_path = f"{self.save_stats_path}/inpainted_img_{base_path}.npy"
            self.inpainted_rgb_img_path = f"{self.save_stats_path}/inpainted_rgb_img_{base_path}_{gripper_types}.jpg"
            self.inpaint_data_for_analysis_path = f"{self.save_stats_path}/inpaint_data_for_analysis_{base_path}_{gripper_types}.npy"
            self.inpaint_data_for_analysis_path_temp = f"{self.save_stats_path}/inpaint_data_for_analysis_temp_{base_path}_{gripper_types}.npy"
            self.diffusion_model_input_path = f"{self.save_stats_path}/diffusion_model_input_{base_path}_{gripper_types}.npy"
            self.inpaint_data_for_analysis_path = f"{self.save_stats_path}/inpaint_ur5_offline_data.npy"

        if self.save_paired_images:
            assert save_paired_images_folder_path is not None, "Please specify save_paired_images_folder_path"
            self.save_paired_images_folder_path = save_paired_images_folder_path
            # create folders if it does not exist
            if self.robot_name is None:
                os.makedirs(os.path.join(self.save_paired_images_folder_path, "franka_rgb"), exist_ok=True)
                os.makedirs(os.path.join(self.save_paired_images_folder_path, "franka_mask"), exist_ok=True)
                os.makedirs(os.path.join(self.save_paired_images_folder_path, "franka_ee_pose"), exist_ok=True)
                os.makedirs(os.path.join(self.save_paired_images_folder_path, "franka_joint_gripper_pose"), exist_ok=True)
                os.makedirs(os.path.join(self.save_paired_images_folder_path, "franka_depth"), exist_ok=True)
            else:
                os.makedirs(os.path.join(self.save_paired_images_folder_path, "{}_rgb".format(self.robot_name.lower())), exist_ok=True)
                os.makedirs(os.path.join(self.save_paired_images_folder_path, "{}_mask".format(self.robot_name.lower())), exist_ok=True)
                os.makedirs(os.path.join(self.save_paired_images_folder_path, "{}_ee_pose".format(self.robot_name.lower())), exist_ok=True)
                os.makedirs(os.path.join(self.save_paired_images_folder_path, "{}_joint_gripper_pose".format(self.robot_name.lower())), exist_ok=True)
                os.makedirs(os.path.join(self.save_paired_images_folder_path, "{}_depth".format(self.robot_name.lower())), exist_ok=True)

        # create environment from saved checkpoint
        self.device = TorchUtils.get_torch_device(try_to_use_cuda=True) if device is None else device
        if self.use_demo:
            env_meta = FileUtils.get_env_metadata_from_dataset(dataset_path=self.hdf5_path)
            self.env = EnvUtils.create_env_for_data_processing(
                env_meta=env_meta,
                camera_names=["agentview"], 
                camera_height=84, 
                camera_width=84, 
                reward_shaping=False,
                robot=robot_name
            )
            
            print("==== Using environment with the following metadata ====")
            print(json.dumps(self.env.serialize(), indent=4))
            print("")
            
            # list of all demonstration episodes (sorted in increasing number order)
            self.f = h5py.File(self.hdf5_path, "r")
            demos = list(self.f["data"].keys())
            inds = np.argsort([int(elem[5:]) for elem in demos])
            self.demos = [demos[i] for i in inds]
            
            self.control_delta = env_meta['env_kwargs']['controller_configs']['control_delta']
            self.task = env_meta['env_name']
            
        elif self.ckpt_path is not None:
            # restore policy
            self.policy, self.ckpt_dict = FileUtils.policy_from_checkpoint(ckpt_path=self.ckpt_path, device=self.device, verbose=True)

            # create environment from saved checkpoint

            self.env, _ = FileUtils.env_from_checkpoint(
                ckpt_dict=self.ckpt_dict, 
                render=self.render, 
                render_offscreen=(self.video_path is not None), 
                verbose=True,
                robot=robot_name,
                gripper_types=self.gripper_types
            )

            #self.env.env.env = DomainRandomizationWrapper(self.env.env.env)

            self.control_delta = self.ckpt_dict["env_metadata"]['env_kwargs']['controller_configs']['control_delta']
            self.task = self.ckpt_dict["env_metadata"]['env_name']
            
            if self.rollout_horizon is None:
                # read horizon from config
                config, _ = FileUtils.config_from_checkpoint(ckpt_dict=self.ckpt_dict)
                self.rollout_horizon = config.experiment.rollout.horizon
        
        self.core_env = self.env.env

        self.is_diffusion = False
        while hasattr(self.core_env, "env"):
            self.is_diffusion = True
            self.core_env = self.core_env.env
        
        self.num_robots = len(self.core_env.robots)
        self.eef_site_name = []
        for i in range(self.num_robots):
            self.eef_site_name.append(self.core_env.robots[i].controller.eef_name)

    
        # maybe open hdf5 to write rollouts
        self.write_dataset = (dataset_path is not None)
        if self.write_dataset:
            self.dataset_path = dataset_path
            self.data_writer = h5py.File(dataset_path, "w")
            self.data_grp = self.data_writer.create_group("data")
            self.total_samples = 0
        
        self.prev_action = None

        # set seed
        if self.seed is not None:
            self.set_seed(self.seed)
            

    def set_seed(self, seed):
        self.seed = seed
        np.random.seed(seed)
        torch.manual_seed(seed)
        random.seed(seed)
        

    def initialize_robot(self):
        self.obs = self.env.reset()
        state_dict_source = self.env.get_state()
        self.obs = self.env.reset_to(state_dict_source) # necessary for robosuite tasks for deterministic action playback
        
    def compute_pose_error(self, target_pose):
        starting_pose = self.compute_eef_pose()
        if self.num_robots == 1:
            # quarternions are equivalent up to sign
            error = min(np.linalg.norm(starting_pose - target_pose), np.linalg.norm(starting_pose - np.concatenate((target_pose[:3], -target_pose[3:]))))
        else:
            error1 = min(np.linalg.norm(starting_pose[:7] - target_pose[:7]), np.linalg.norm(starting_pose[:7] - np.concatenate((target_pose[:3], -target_pose[3:7]))))
            error2 = min(np.linalg.norm(starting_pose[7:] - target_pose[7:]), np.linalg.norm(starting_pose[7:] - np.concatenate((target_pose[7:10], -target_pose[10:]))))
            error = max(error1, error2)
        return error, starting_pose
    
    def drive_robot_to_target_pose(self, target_pose=None, tracking_error_threshold=0.003, num_iter_max=100):
        for i in range(self.num_robots):
            self.core_env.robots[i].controller.use_delta = False # change to absolute pose for setting the initial state
        
        error, starting_pose = self.compute_pose_error(target_pose)
        num_iters = 0    
        while error > tracking_error_threshold and num_iters < num_iter_max:
            if self.num_robots == 1:
                assert len(target_pose) == 7, "Target pose should be 7DOF"
                action = np.zeros(7)
                action[:3] = target_pose[:3]
                action[3:6] = T.quat2axisangle(target_pose[3:])
            else:
                assert len(target_pose) == 14, "Target pose should be 14DOF"
                action = np.zeros(14)
                action[:3] = target_pose[:3]
                action[3:6] = T.quat2axisangle(target_pose[3:7])
                action[6] = 0
                action[7:10] = target_pose[7:10]
                action[10:13] = T.quat2axisangle(target_pose[10:])
            
            self.obs, _, _, _ = self.env.step(action)

            error, starting_pose = self.compute_pose_error(target_pose)
            num_iters += 1

        print("Take {} iterations to drive robot to target pose".format(num_iters))
        try:
            # flip the sign of the quarternion because that is equivalent
            # assert np.allclose(starting_pose, target_pose, atol=0.005) or np.allclose(starting_pose, np.concatenate((target_pose[:3], -target_pose[3:])), atol=0.005), "Starting states are not the same"
            assert error < tracking_error_threshold, "Starting states are not the same"
        except:
            print("Starting states are not the same"
                    "Source: ", starting_pose,
                    "Target: ", target_pose)
            # breakpoint()
        
        # change back to delta pose
        for i in range(self.num_robots):
            self.core_env.robots[i].controller.use_delta = True
        

    def compute_eef_pose(self):
        """return a 7D or 14D pose vector"""
        pose = []
        for i in range(self.num_robots):
            pos = np.array(self.core_env.sim.data.site_xpos[self.core_env.sim.model.site_name2id(self.eef_site_name[i])])
            rot = np.array(T.mat2quat(self.core_env.sim.data.site_xmat[self.core_env.sim.model.site_name2id(self.eef_site_name[i])].reshape([3, 3])))
            pose.append(np.concatenate((pos, rot)))
        pose = np.concatenate(pose)
        return pose


    def get_object_state(self):
        object_state = dict()
        for obj_name in TASK_OBJECT_DICT[self.task]:
            object_state[obj_name] = self.core_env.sim.data.get_joint_qpos(obj_name)
        return object_state
    
    def set_object_state(self, set_to_target_object_state=None):
        if set_to_target_object_state is not None:
            # set target object to target object state
            for obj_name in TASK_OBJECT_DICT[self.task]:
                self.core_env.sim.data.set_joint_qpos(obj_name, set_to_target_object_state[obj_name])
            # self.core_env.sim.data.set_joint_qpos("cube_joint0", set_to_target_object_state)
                self.core_env.sim.forward()
            self.obs = self.env.get_observation()
            if hasattr(self.env, "_get_stacked_obs_from_history"):
                self.obs = self.env._get_stacked_obs_from_history()
        
        
    def step(self, action, use_delta=True, blocking=False, tracking_error_threshold=0.003, num_iter_max=100, goal_pose=None, name="Source Robot"):
        """
        If not blocking, action is EEF (delta) pose (6DOF) + gripper
        If blocking, action is EEF target state (7DOF using quarternion) + gripper
        """
        if self.prev_action is None:
            self.prev_action = action
        # if action[-1] != self.prev_action[-1]:
        #     print(action)
        #     print("before", self.compute_eef_pose())
        if not blocking:
            assert (len(action) == 7 and self.num_robots == 1) or (len(action) == 14 and self.num_robots == 2), "Action should be 7DOF"
            for i in range(self.num_robots):
                self.core_env.robots[i].controller.use_delta = use_delta
            next_obs, r, done, _ = self.env.step(action) # just execute action
            # if action[-1] != self.prev_action[-1]:
            #     print("after", self.compute_eef_pose())
            if goal_pose is None:
                tracking_error_history.append(0)
            else:
                actual_pose = self.compute_eef_pose()
                error = np.linalg.norm(goal_pose - actual_pose)
                tracking_error_history.append(error)
        else:
            # robot_env.py #L583
            # single_arm.py #L247
            # osc.py #L264
            if use_delta:
                self.core_env.robots[0].controller.use_delta = True
                # convert to equivalent absolute actions
                self.core_env.robots[0].controller.set_goal(action[:self.core_env.robots[0].controller.control_dim])
                action_goal_pos = self.core_env.robots[0].controller.goal_pos
                action_goal_ori = Rotation.from_matrix(self.core_env.robots[0].controller.goal_ori).as_rotvec()
                raise NotImplementedError
                next_obs, r, done, _ = self.env.step(action) 
            else:
                assert (len(action) == 8 and self.num_robots == 1) or (len(action) == 16 and self.num_robots == 2), "Action should be 8DOF"
                for i in range(self.num_robots):
                    self.core_env.robots[i].controller.use_delta = False
                    self.core_env.robots[i].controller.kp = np.array([150, 150, 150, 150, 150, 150]) # control gain
                    # self.core_env.robots[i].controller.kp = np.array([100, 100, 500, 10, 10, 50]) # control gain
                    print("Robot {} controller kp: {}".format(i, self.core_env.robots[i].controller.kp))
                if self.num_robots == 1:
                    action_target = np.zeros(7)
                    action_target[:3] = action[:3]
                    action_target[3:6] = T.quat2axisangle(action[3:7])
                    action_target[-1] = self.prev_action[-1]
                elif self.num_robots == 2:
                    action_target = np.zeros(14)
                    action_target[:3] = action[:3]
                    action_target[3:6] = T.quat2axisangle(action[3:7])
                    action_target[6] = self.prev_action[7]
                    action_target[7:10] = action[8:11]
                    action_target[10:13] = T.quat2axisangle(action[11:15])
                    action_target[-1] = self.prev_action[-1]
                error = np.inf
                num_iters = 0
                while error > tracking_error_threshold and num_iters < num_iter_max:
                    # if action[-1] != self.prev_action[-1]:
                    #     print("action_target", action_target)
                    next_obs, r, done, _ = self.env.step(action_target)
                    actual_pose = self.compute_eef_pose()
                    if self.num_robots == 1:
                        error = np.linalg.norm(action[:-1] - actual_pose)
                    elif self.num_robots == 2:
                        error = np.linalg.norm(np.concatenate((action[:7], action[8:15])) - actual_pose)
                            
                    num_iters += 1
                print("{}: Take {} iterations to drive robot to target pose".format(name, num_iters))
                
                if self.num_robots == 1:
                    if action[-1] != self.prev_action[-1]:
                        # print("after", self.compute_eef_pose())
                        # self.core_env.robots[0].controller.use_delta = True
                        # action_target = np.zeros(7)
                        action_target[-1] = action[-1]
                        # print("action_target", action_target)
                        next_obs, r, done, _ = self.env.step(action_target)
                        # self.core_env.robots[0].controller.use_delta = False
                        # print("after", self.compute_eef_pose())
                elif self.num_robots == 2:
                    action_target[6] = action[7]
                    action_target[-1] = action[-1]
                    next_obs, r, done, _ = self.env.step(action_target)
                if error > tracking_error_threshold:
                    print("Warning: did not reach target pose, error: ", error)
                tracking_error_history.append(error)
        success = self.env.is_success()["task"]
        self.prev_action = action
        self.obs = deepcopy(next_obs)
        return action, r, done, success

    
    def run_experiments(self, seeds, rollout_num_episodes=1, video_skip=5, camera_names="agentview", dataset_obs=False, save_stats_path=None, tracking_error_threshold=0.003, num_iter_max=100, target_robot_delta_action=False, inpaint_online_eval=False):
        """target_robot_delta_action only affects the target robot. Default is to track the absolute pose of the source robot."""
        avg_rollout_stats = dict(Seeds=[], Return=[], Horizon=[], Success_Rate=[], Num_Success=[])
        inpaint_data_for_analysis = []
        print(seeds, 'seeds')
        for seed in seeds:
            self.seed = seed
            print("Seed_check: ", seed)
            self.set_seed(seed)
            rollout_stats = []
            if self.use_demo:
                rollout_num_episodes = min(rollout_num_episodes, len(self.demos))
            for i in range(0, rollout_num_episodes):
                self.set_seed(seed * rollout_num_episodes +i)
                if i==0:
                    import os
                    if (self.inpaint_enabled and os.path.exists(self.inpaint_data_for_analysis_path_temp)):
                        os.remove(self.inpaint_data_for_analysis_path_temp) # remove that file
                self.execution_count = i
                print("Rollout {}/{}".format(i + 1, rollout_num_episodes))
                stats, traj, inpaint_data_for_analysis_1traj = self.rollout_robot(
                    video_skip=1,
                    return_obs=self.write_dataset,
                    camera_names=camera_names,
                    set_object_state=True,
                    set_robot_pose=inpaint_online_eval or self.save_paired_images, # no need to set it to true since the target robot will be tracking the source robot, unless it is inpainting with online eval
                    tracking_error_threshold=tracking_error_threshold, # used only by the target robot because it is blocking
                    num_iter_max=num_iter_max, # used only by the target robot because it is blocking
                    target_robot_delta_action = target_robot_delta_action,
                    demo_index=i
                )
                rollout_stats.append(stats)
                inpaint_data_for_analysis.append(inpaint_data_for_analysis_1traj)
                
                if (self.save_failed_demos or stats["Success_Rate"] >= 1) and self.write_dataset: # only save successful trajs
                    # store transitions
                    ep_data_grp = self.data_grp.create_group("demo_{}".format(i))
                    ep_data_grp.create_dataset("actions", data=np.array(traj["actions"]))
                    ep_data_grp.create_dataset("states", data=np.array(traj["states"]))
                    ep_data_grp.create_dataset("rewards", data=np.array(traj["rewards"]))
                    ep_data_grp.create_dataset("dones", data=np.array(traj["dones"]))
                    if dataset_obs:
                        for k in traj["obs"]:
                            ep_data_grp.create_dataset("obs/{}".format(k), data=np.array(traj["obs"][k]))
                            ep_data_grp.create_dataset("next_obs/{}".format(k), data=np.array(traj["next_obs"][k]))

                    # episode metadata
                    if "model" in traj["initial_state_dict"]:
                        ep_data_grp.attrs["model_file"] = traj["initial_state_dict"]["model"] # model xml for this episode
                    ep_data_grp.attrs["num_samples"] = traj["actions"].shape[0] # number of transitions in this episode
                    self.total_samples += traj["actions"].shape[0]

                # avg_rollout_stats = {k : np.mean(rollout_stats[k]) for k in rollout_stats}
                dict_rollout_stats = TensorUtils.list_of_flat_dict_to_dict_of_list(rollout_stats)
                avg_rollout_stats = dict(Seeds=[], Return=[], Horizon=[], Success_Rate=[], Num_Success=[])
                for k in dict_rollout_stats:
                    avg_rollout_stats[k].append(np.mean(dict_rollout_stats[k]))
                avg_rollout_stats["Num_Success"].append(np.sum(dict_rollout_stats["Success_Rate"]))
                avg_rollout_stats["Num Rollouts"] = i + 1
                avg_rollout_stats["Seeds"].append(seed)
                avg_rollout_stats["Robot"] = self.robot_name
                print("Average Rollout Stats:")
                print(json.dumps(avg_rollout_stats, indent=4))
                summary_stats = {k : (np.mean(avg_rollout_stats[k]), np.std(avg_rollout_stats[k])) for k in avg_rollout_stats if k not in ["Seeds", "Robot"]}
                summary_stats["tracking_error"] = (np.mean(tracking_error_history), np.std(tracking_error_history))
                summary_stats["config"] = dict()
                summary_stats["config"]["Robot"] = avg_rollout_stats["Robot"]
                summary_stats["config"]["tracking_error_threshold"] = tracking_error_threshold
                summary_stats["config"]["num_iter_max"] = num_iter_max
                print("Summary Stats:")
                print(json.dumps(summary_stats, indent=4))
                if save_stats_path is not None:
                    with open(save_stats_path, "w") as f:
                        json.dump(avg_rollout_stats, f, indent=4)
                        json.dump(summary_stats, f, indent=4)
        
        if self.write_video:
            self.video_writer.close()

        if self.inpaint_writer:
            self.inpaint_writer.close()

        if self.write_dataset:
            # global metadata
            self.data_grp.attrs["total"] = self.total_samples
            env_args_dict = self.env.serialize()
            env_args_dict['env_kwargs']['controller_configs']['control_delta'] = target_robot_delta_action # since we are saving the dataset for the target robot
            self.data_grp.attrs["env_args"] = json.dumps(env_args_dict, indent=4) # environment info
            # self.data_grp.attrs["env_args"] = json.dumps(self.env.serialize(), indent=4) # environment info
            self.data_writer.close()
            print("Wrote dataset trajectories to {}".format(self.dataset_path))
        
        if self.inpaint_enabled:
            if len(inpaint_data_for_analysis_1traj) != 0: # only save the target copy
                import pickle
                with open(self.inpaint_data_for_analysis_path, "wb") as f:
                    pickle.dump(inpaint_data_for_analysis, f)
                print("Saved inpaint_data_for_analysis to {}".format(self.inpaint_data_for_analysis_path))
            # clean up temporary files
            import os
            if os.path.isfile(self.groundtruth_and_inpaintedprediction_path):
                os.remove(self.groundtruth_and_inpaintedprediction_path)
            if os.path.isfile(self.inpainted_img_path):
                os.remove(self.inpainted_img_path)
        
        if self.s is not None:
            self.s.close()


class SourceRobot(Robot):
    def __init__(self, robot_name=None, ckpt_path=None, render=False, video_path=None, rollout_horizon=None, seed=None, dataset_path=None, connection=None, port = 50007, passive=True, demo_path=None, inpaint_enabled=False, forward_dynamics_model_path='', save_paired_images=False, save_paired_images_folder_path=None, device=None, save_failed_demos=False, naive=False, save_stats_path=None, add_patches=False):
        super().__init__(robot_name=robot_name, ckpt_path=ckpt_path, render=render, video_path=video_path, rollout_horizon=rollout_horizon, seed=seed, dataset_path=dataset_path, demo_path=demo_path, inpaint_enabled=inpaint_enabled, save_paired_images=save_paired_images, save_paired_images_folder_path=save_paired_images_folder_path, device=device, save_failed_demos=save_failed_demos, save_stats_path=save_stats_path, add_patches=add_patches)
        
        if connection:
            HOST = 'localhost'
            PORT = port
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.s.bind((HOST, PORT))
            self.s.listen(1)
            self.conn, addr = self.s.accept()
            print('Connected by', addr)
        else:
            self.s = None
            self.conn = None
            
        self.passive = passive
        
        if self.inpaint_enabled:
            self.forward_dynamics_model = None
            if forward_dynamics_model_path:
                from image_inpainting.forward_dynamics_model import ForwardDynamicsModel
                self.forward_dynamics_model = ForwardDynamicsModel(model_path=forward_dynamics_model_path)

        self.naive = naive
        
    def rollout_robot(self, video_skip=5, return_obs=False, camera_names=None, set_object_state=False, set_robot_pose=False, tracking_error_threshold=0.003, num_iter_max=100, target_robot_delta_action=False, demo_index=0):
        """
        Helper function to carry out rollouts. Supports on-screen rendering, off-screen rendering to a video, 
        and returns the rollout trajectory.
        
        The source robot will:
            - optionally receive the target object state and target robot pose from the target robot, and then set its environment to that state and/or pose.
            - Then, the source robot will execute the action from the policy as usual from its own environment.
            - Then, it will send the action command and the actual achieved pose to the target robot.
        
        Args:
            video_skip (int): how often to write video frames
            return_obs (bool): if True, return possibly high-dimensional observations along the trajectoryu. 
                They are excluded by default because the low-dimensional simulation states should be a minimal 
                representation of the environment. 
            camera_names (list): determines which camera(s) are used for rendering. Pass more than
                one to output a video with multiple camera views concatenated horizontally.
            
        Returns:
            stats (dict): some statistics for the rollout - such as return, horizon, and task success
            traj (dict): dictionary that corresponds to the rollout trajectory
        """
        # assert isinstance(self.env, EnvBase)
        # assert isinstance(self.policy, RolloutPolicy)

        self.video_writer = imageio.get_writer(f'{self.execution_count}_{self.video_path}', fps=20) if self.write_video else None
        if self.save_paired_images:            
            os.makedirs(os.path.join(self.save_paired_images_folder_path, "franka_rgb", str(demo_index)), exist_ok=True)
            os.makedirs(os.path.join(self.save_paired_images_folder_path, "franka_mask", str(demo_index)), exist_ok=True)
            os.makedirs(os.path.join(self.save_paired_images_folder_path, "franka_ee_pose", str(demo_index)), exist_ok=True)
            os.makedirs(os.path.join(self.save_paired_images_folder_path, "franka_joint_gripper_pose", str(demo_index)), exist_ok=True)
            os.makedirs(os.path.join(self.save_paired_images_folder_path, "franka_depth", str(demo_index)), exist_ok=True)
        
        
        if self.use_demo:
            # reset to the initial state of the demo
            ep = self.demos[demo_index]

            # prepare initial state to reload from
            states = self.f["data/{}/states".format(ep)][()]
            initial_state = dict(states=states[0])
            initial_state["model"] = self.f["data/{}".format(ep)].attrs["model_file"]

            # extract obs, rewards, dones
            actions = self.f["data/{}/actions".format(ep)][()]
            traj_len = states.shape[0]
            print("Demo length: ", traj_len)
            # load the initial state
            self.env.reset()
            self.obs = self.env.reset_to(initial_state)
        else:
            self.policy.start_episode()
            self.initialize_robot()
            
            
        # the source robot is ready to execute the policy
        if self.conn is not None:
            # tell the target robot that the source robot is ready
            # Create an instance of Data() to send to client.
            variable = Data()
            variable.object_state = self.get_object_state()
            variable.robot_pose = self.compute_eef_pose()
            variable.message = "Ready"
            # Pickle the object and send it to the server
            data_string = pickle.dumps(variable)
            message_length = struct.pack("!I", len(data_string))
            self.conn.sendall(message_length)
            self.conn.send(data_string)
            # confirm that the target robot is ready
            pickled_message_size = self._receive_all_bytes(4)
            message_size = struct.unpack("!I", pickled_message_size)[0]
            data = self._receive_all_bytes(message_size)
            target_env_robot_state = pickle.loads(data)
            # print("Receiving target object state and target robot pose from target robot")
            assert target_env_robot_state.message == "Ready", "Target robot is not ready"
        
        # Save the ground truth so that the target robot can use it even before it does its first step
        if self.inpaint_enabled:
            image = self.obs['agentview_image'].transpose(1, 2, 0) # convert to HWC
            # image = np.array(Image.fromarray((image * 255).astype(np.uint8)).resize((84, 84))).astype(np.float32) / 255.0
            segmentation_mask = self.obs['agentview_segmentation_robot_only']
            segmentation_mask = cv2.flip(segmentation_mask, 0)
            output = {
                    "ground_truth": {
                        "rgb": image,
                        "segmentation_mask": segmentation_mask,
                        "low_dim": {
                            "joint_angles": self.obs['robot0_joint_pos'],
                            "robot_eef_pos": self.obs['robot0_eef_pos'],
                            "robot_eef_quat": self.obs['robot0_eef_quat'],
                            "robot0_gripper_qpos": self.obs['robot0_gripper_qpos']
                            }
                    }
                }
            np.save(self.groundtruth_and_inpaintedprediction_path, output)
        
        video_count = 0  # video frame counter
        total_reward = 0.
        state_dict = self.env.get_state()
        traj = dict(actions=[], rewards=[], dones=[], states=[], initial_state_dict=state_dict)
        if return_obs:
            # store observations too
            traj.update(dict(obs=[], next_obs=[]))
        
        target_finished_step = None
        has_succeeded = False # since we don't break once succeed and it may fail later, we set has_succeeded to True avoid success being overwritten
        # try:
        for step_i in range(self.rollout_horizon):
            print("Source Step: ", step_i)
            # receive target object state and target robot pose from target robot
            if self.passive:
                if self.conn is not None:
                    pickled_message_size = self._receive_all_bytes(4)
                    message_size = struct.unpack("!I", pickled_message_size)[0]

                    data = self._receive_all_bytes(message_size)
                    target_env_robot_state = pickle.loads(data)
                    assert target_env_robot_state.message == "Request for Action", "Wrong synchronization"
                    # print("Receiving target object state and target robot pose from target robot")
                    # if target_env_robot_state.done:
                    #     print("Target robot is done")
                    #     break
                    # if target_env_robot_state.success:
                    #     print("Target robot is successful")
                    #     break
                
                if set_object_state:
                    self.set_object_state(set_to_target_object_state=target_env_robot_state.object_state)
                if set_robot_pose:
                    self.drive_robot_to_target_pose(target_env_robot_state.robot_pose, tracking_error_threshold=tracking_error_threshold, num_iter_max=num_iter_max)
            
            # state_dict and obs are before taking the action
            state_dict = self.env.get_state()
            obs = deepcopy(self.obs)
            
            if self.save_paired_images:
                # save the rgb image and segmentation mask
                # because we've modified `get_observation` (Line 187) of env_robosuite.py such that all rgb images are flipped and channel swapped,
                # they are now 3, H, W and not upside down (which is what the policy wants), but the segmentation mask is still upside down and H, W, 1
                rgb_img = obs['agentview_image']
                rgb_img = rgb_img.transpose(1, 2, 0)
                segmentation_mask = obs['agentview_segmentation_robot_only']
                segmentation_mask = cv2.flip(segmentation_mask, 0)
                depth_normalized = obs['agentview_depth']
                depth_normalized = cv2.flip(depth_normalized, 0)
                depth_img = camera_utils.get_real_depth_map(self.core_env.sim, depth_normalized)
                # save the rgb image
                cv2.imwrite(os.path.join(self.save_paired_images_folder_path, "franka_rgb", str(demo_index), "{}.jpg".format(step_i)), cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR) * 255)
                # save the segmentation mask
                cv2.imwrite(os.path.join(self.save_paired_images_folder_path, "franka_mask", str(demo_index), "{}.jpg".format(step_i)), segmentation_mask * 255)
                # save the EE pose
                with open(os.path.join(self.save_paired_images_folder_path, "franka_ee_pose", str(demo_index), "{}.txt".format(step_i)), "w") as f:
                    f.write(str(np.concatenate([self.compute_eef_pose(), obs['robot0_gripper_qpos']])))
                # save the joint and gripper pose
                with open(os.path.join(self.save_paired_images_folder_path, "franka_joint_gripper_pose", str(demo_index), "{}.txt".format(step_i)), "w") as f:
                    f.write(str(np.concatenate([obs['robot0_joint_pos'], obs['robot0_gripper_qpos']])))
                # save the depth map
                np.save(os.path.join(self.save_paired_images_folder_path, "franka_depth", str(demo_index), "{}.npy".format(step_i)), depth_img)
            
            obs_copy = deepcopy(obs)
            # if obs_copy["agentview_image"].shape[-1] != 84:
            #     rgb_img = obs_copy['agentview_image']
            #     rgb_img = rgb_img.transpose(1, 2, 0)
            #     rgb_img = np.array(Image.fromarray((rgb_img * 255).astype(np.uint8)).resize((84, 84))).astype(np.float32) / 255.0
            #     obs_copy["agentview_image"] = rgb_img.transpose(2, 0, 1)
            
            if self.use_demo:
                action = actions[step_i]
            else:
                # Hack to get rid of stuff that screws with robomimic for coffee env
                for k, v in obs_copy.items():
                    if np.isscalar(v):
                        obs_copy[k] = np.array([v])

                gt_action = 0
                #action2 = self.policy(ob=obs_copy) # get action from policy
                #gt_action = action.copy()                    

                #for i in range(1):
                    #action = self.policy(ob=obs_copy) # get action from policy
                    #gt_action += action.copy()/1                    
            
            if self.inpaint_enabled:
                # ground truth
                rgb_img = obs['agentview_image']
                rgb_img = rgb_img.transpose(1, 2, 0)
                cv2.imwrite(f"{self.save_stats_path}/groundtruth.png", cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR) * 255)
                # inpainted image
                # diffusion_model_input = np.load(self.diffusion_model_input_path)
                inpainted_image = np.load(self.inpainted_img_path, allow_pickle=True)
                # if inpainted_image.shape[-1] != 84:
                #     inpainted_image_84 = Image.fromarray((inpainted_image*255).round().astype(np.uint8)).resize((84, 84))
                #     inpainted_image_84 = np.array(inpainted_image_84).astype(np.float32) / 255.0
                # else:
                #     inpainted_image_84 = inpainted_image
                inpainted_image_84 = inpainted_image
                obs_copy = deepcopy(obs)
                obs_copy["agentview_image"] = inpainted_image_84.transpose(2, 0, 1)
                inpainted_img_action = self.policy(ob=obs_copy)
                current_pose = target_env_robot_state.robot_pose #self.compute_eef_pose()
                transition = {
                            'current_state': np.concatenate([current_pose, obs['robot0_gripper_qpos']]),
                            'action': inpainted_img_action,
                            'gt_action': gt_action
                        }
                if self.forward_dynamics_model:
                    predicted_state = self.forward_dynamics_model(transition['current_state'], transition['action'])
                    predicted_state_from_gt = self.forward_dynamics_model(transition['current_state'], transition['gt_action'])
                # if predicted_state[2] > 0.865:
                #     print("Adjusted")
                #     predicted_state[2] -= 0.015 # the z coordinate is too high
                action = inpainted_img_action.copy()
                # action = gt_action.copy()
            
            if self.naive:
                target_img = np.load(f"{self.save_stats_path}/naive_input.npy", allow_pickle=True)
                if self.add_patches:
                    target_img[0] = add_black_patches(target_img[0], seed=self.seed)
                    target_img[1] = add_black_patches(target_img[1], seed=self.seed)
                obs_copy = deepcopy(obs)
                obs_copy["agentview_image"] = target_img
                action = self.policy(ob=obs_copy)

            action, r, done, success = self.step(action, use_delta=self.control_delta, blocking=False, name="Source Robot")
     
            if success:
                has_succeeded = True
            next_obs = deepcopy(self.obs)
            total_reward += r
            
            # if the target robot has succeeded, allow 10 more steps for the source robot to finish
            if target_finished_step is not None and not self.passive:
                if step_i - target_finished_step >= 10:
                    done = True
            # regardless of what happens, if we are at the end of the demo, we have to break
            if self.use_demo and step_i >= traj_len - 1:
                done = True
            else:
                done = False
            if self.conn is not None:
                # Create an instance of Data() to send to client.
                variable = Data()
                # variable.obs = obs
                variable.action = action
                variable.object_state = self.get_object_state()
                variable.robot_pose = self.compute_eef_pose()
                variable.done = done
                variable.success = success
                variable.message = "Respond with Action"
                if self.inpaint_enabled:
                    image = self.obs['agentview_image'].transpose(1, 2, 0) # convert to HWC
                    # image = np.array(Image.fromarray((image * 255).astype(np.uint8)).resize((84, 84))).astype(np.float32) / 255.0
                    segmentation_mask = self.obs['agentview_segmentation_robot_only']
                    segmentation_mask = cv2.flip(segmentation_mask, 0)

                    inpainting_dict_data = {
                        # "input": diffusion_model_input,
                        "rgb": inpainted_image,
                        "predicted_action": inpainted_img_action,
                    }

                    if self.forward_dynamics_model:
                        inpainting_dict_data["predicted_state"] = predicted_state
                        inpainting_dict_data["predicted_state_from_gt"] = predicted_state_from_gt

                    output = {
                            "inpainting": inpainting_dict_data,
                            "ground_truth": {
                                "rgb": image,
                                "segmentation_mask": segmentation_mask,
                                "low_dim": {
                                    "joint_angles": obs['robot0_joint_pos'],
                                    "robot_eef_pos": obs['robot0_eef_pos'],
                                    "robot_eef_quat": obs['robot0_eef_quat'],
                                    "robot0_gripper_qpos": obs['robot0_gripper_qpos']
                                    },
                                "action": inpainted_img_action,
                                "target_state": self.compute_eef_pose()
                            }
                        }
                    np.save(self.groundtruth_and_inpaintedprediction_path, output)

                # Pickle the object and send it to the server
                data_string = pickle.dumps(variable)
                message_length = struct.pack("!I", len(data_string))
                self.conn.sendall(message_length)
                self.conn.send(data_string)
            
            # visualization
            if self.render:
                self.env.render(mode="human", camera_name=camera_names[0]) # on-screen rendering can only support one camera
            if self.write_video:
                if video_count % 1 == 0:
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
                
            
            # confirm that the target robot is ready for the next iteration
            if self.conn is not None:
                pickled_message_size = self._receive_all_bytes(4)
                message_size = struct.unpack("!I", pickled_message_size)[0]
                data = self._receive_all_bytes(message_size)

                target_env_robot_state = pickle.loads(data)
                assert target_env_robot_state.message == "OK", "Wrong synchronization"
                if target_env_robot_state.success or target_finished_step is not None:
                    print("Target robot is successful")
                    if target_finished_step is None:
                        target_finished_step = step_i
                    if not success:
                        print("Source robot is not successful!")
                    else:
                        print("Both robots are successful!")
                        break
                    if done:
                        print("Source robot is done!")
                        break
                    if self.passive:
                        break # no need to wait for source to succeed
                if target_env_robot_state.done:
                    print("Target robot is done")
                    if not (done or has_succeeded):
                        print("Source robot is not done!")
                    else:
                        print("Both robots are done!")
                    break
                
            # break if done or if success
            if done:
                if self.conn is not None:
                    if target_finished_step is None and not self.use_demo:
                        print("Source robot done and target robot is not!")
                    else:
                        print("Both robots are done!")
                        break
                else:
                    print("Source robot done!")
                    break
            if success:
                if self.conn is not None:
                    print("Source robot successful and target robot is not!")
                else:
                    print("Source robot successful!")
                    break
                
        # except:
        #     if self.env.rollout_exceptions:
        #         print("WARNING: got source robot rollout exception {}".format(self.env.rollout_exceptions))

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

        
        return stats, traj, []

    def _receive_all_bytes(self, num_bytes: int) -> bytes:
        """
        Receives all the bytes.
        :param num_bytes: The number of bytes.
        :return: The bytes.
        """
        data = bytearray(num_bytes)
        pos = 0
        while pos < num_bytes:
            cr = self.conn.recv_into(memoryview(data)[pos:])
            if cr == 0:
                raise EOFError
            pos += cr
        return data
#python /home/harshapolavaram/mirage/mirage/mirage/benchmark/robosuite/evaluate_policy_demo_source_robot_server.py --agent /home/harshapolavaram/mirage/secondversion/trained_diffusion_policies/exp_11_ur5e_can_clean/20250421045854/models/model_epoch_400.pth --n_rollouts 10 --video_path source_clean.mp4 --save_stats_path /home/harshapolavaram/mirage/
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Path to trained model
    parser.add_argument(
        "--agent",
        type=str,
        default=None,
        help="(optional) path to saved checkpoint pth file",
    )

    parser.add_argument(
        "--device",
        type=str,
        default=None,
        help="(optional) set device for execution",
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
        default=1,
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
        default=[0],
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
        help="(optional) unused by the source robot. For logging purposes only",
    )
    parser.add_argument(
        "--num_iter_max",
        type=int,
        default=100,
        help="(optional) unused by the source robot. For logging purposes only",
    )
    parser.add_argument(
        "--inpaint_enabled",
        action='store_true',
        help="if True, pass inpainted images to the policy",
    )
    parser.add_argument(
        "--forward_dynamics_model_path",
        type=str,
        default=None,
        help="checkpoint path of the forward dynamics model",
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
        "--save_failed_demos",
        action='store_true',
        help="Set this to true to also save demos that failed",
    )
    parser.add_argument(
        "--naive",
        action='store_true',
        help="Set this to true to have a naive highdim policy that passes in the rendered image to the ",
    )
    parser.add_argument(
        "--add_patches",
        action='store_true',
        help="if True, add black patches to the target robot camera images",
    )
    args = parser.parse_args()

    source_robot = SourceRobot(robot_name=args.robot_name, ckpt_path=args.agent, render=args.render, video_path=args.video_path, rollout_horizon=args.horizon, seed=None, dataset_path=args.dataset_path, passive=args.passive, port=args.port, connection=args.connection, demo_path=args.demo_path, inpaint_enabled=args.inpaint_enabled, save_paired_images=args.save_paired_images, save_paired_images_folder_path=args.save_paired_images_folder_path, forward_dynamics_model_path=args.forward_dynamics_model_path, device=args.device, save_failed_demos=args.save_failed_demos, save_stats_path=args.save_stats_path, naive=args.naive, add_patches=args.add_patches)
    source_robot.run_experiments(seeds=args.seeds, rollout_num_episodes=args.n_rollouts, video_skip=args.video_skip, camera_names=args.camera_names, dataset_obs=args.dataset_obs, save_stats_path=args.save_stats_path, tracking_error_threshold=args.tracking_error_threshold, num_iter_max=args.num_iter_max, inpaint_online_eval=args.inpaint_enabled)

