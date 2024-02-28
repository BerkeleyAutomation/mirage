
"""
# Mode 1: Target robot following the source robot
python evaluate_policy_demo_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 1 --seeds 0 --connection --video_path /home/lawrence/xembody/robosuite/collected_data/output_lift_low_dim_1.mp4 

# Mode 2: Target robot querying the source robot for actions
python evaluate_policy_demo_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 1 --horizon 400 --seeds 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_lift_low_dim_1.mp4 --connection --passive 

python3 source_robot_eval.py --agent /home/lawrence/xembody/xembody/xembody/test/orbit/trained_runs/model_700.pt --task Isaac-Lift-Franka-v0  --n_rollouts 1 --seeds 0 --connection --passive

python3 source_robot_eval.py --agent /home/lawrence/xembody/Orbit/source/standalone/workflows/rsl_rl/models/image_based_multihead_policy_40.pth --task Isaac-Lift-Visual-v0  --n_rollouts 1 --seeds 0 --connection --passive
"""

import argparse
import imageio
import gym
import json
from copy import deepcopy
import socket
import pickle

import numpy as np
import torch
import robomimic.utils.torch_utils as TorchUtils
from omni.isaac.kit import SimulationApp

# Need to engage bad workaround, since certain imports need to be done after the Simulation env is created
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Path to trained model
    parser.add_argument(
        "--agent",
        type=str,
        default=None,
        help="(optional) path to saved checkpoint pth file (RSL RL)",
    )

    # Path to trained model
    parser.add_argument(
        "--task",
        type=str,
        default='Isaac-Lift-Visual-v0',
        help="task name in Orbit",
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
        default=200,
        help="(optional) override maximum horizon of rollout from the one in the checkpoint",
    )

    # Whether to render rollouts to screen
    parser.add_argument(
        "--headless",
        action='store_true',
        help="go headless mode?",
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
        default="franka",
        help="(optional) if provided, there will be a second robot tracking the panda robot where the policy is executed with,\
            [ur5, franka, jaco]",
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
        default=3,
        help="(optional) unused by the source robot. For logging purposes only",
    )
    args = parser.parse_args()


    config = {"headless": args.headless}
    simulation_app = SimulationApp(config)

from omni.isaac.orbit_envs.utils.wrappers.rsl_rl import RslRlVecEnvWrapper
from config import parse_rslrl_cfg
import robomimic.utils.tensor_utils as TensorUtils
from mirage.orbit.orbit_renderer import OrbitRenderer
from mirage.orbit.utils import set_robot_configuration
import robosuite.utils.transform_utils as T
from omni.isaac.orbit_envs.utils import parse_env_cfg

from torchvision.models import resnet34, ResNet34_Weights, resnet18, ResNet18_Weights
import torch.nn as nn
from collections import OrderedDict

class DistilledPolicy(nn.Module):

    def __init__(self, checkpoint_weights):
        super().__init__()
        image_encoder = resnet18(weights=ResNet18_Weights.DEFAULT)
        weights = ResNet18_Weights.DEFAULT
        self.actor_preprocess = weights.transforms()
        n_inputs = image_encoder.fc.in_features
        # add more layers as required
        classifier = nn.Sequential(OrderedDict([
            ('fc1', nn.Linear(n_inputs, 128))
        ]))
        image_encoder.fc = classifier

        # Define MLPs for each head
        hidden_dims = [256, 256, 256]
        # Define individual heads for each task
        head_ik_2_position_rel_15 = nn.Sequential(
            nn.Linear(128, hidden_dims[0]),
            nn.ReLU(),
            nn.Linear(hidden_dims[0], hidden_dims[1]),
            nn.ReLU(),
            nn.Linear(hidden_dims[1], hidden_dims[2]),
            nn.ReLU(),
            nn.Linear(hidden_dims[2], 4)
        )  # Output dimensions: 4
        head_ik_2_position_abs_15 = nn.Sequential(
            nn.Linear(128, hidden_dims[0]),
            nn.ReLU(),
            nn.Linear(hidden_dims[0], hidden_dims[1]),
            nn.ReLU(),
            nn.Linear(hidden_dims[1], hidden_dims[2]),
            nn.ReLU(),
            nn.Linear(hidden_dims[2], 4)
        )  # Output dimensions: 4
        head_ik_2_pose_rel_15 = nn.Sequential(
            nn.Linear(128, hidden_dims[0]),
            nn.ReLU(),
            nn.Linear(hidden_dims[0], hidden_dims[1]),
            nn.ReLU(),
            nn.Linear(hidden_dims[1], hidden_dims[2]),
            nn.ReLU(),
            nn.Linear(hidden_dims[2], 7)
        )
        head_ik_2_pose_abs_15 = nn.Sequential(
            nn.Linear(128, hidden_dims[0]),
            nn.ReLU(),
            nn.Linear(hidden_dims[0], hidden_dims[1]),
            nn.ReLU(),
            nn.Linear(hidden_dims[1], hidden_dims[2]),
            nn.ReLU(),
            nn.Linear(hidden_dims[2], 8)
        )  # Output dimensions: 8
        # Output dimensions: 7
        head_default_2_pose_rel_15 = nn.Sequential(
            nn.Linear(128, hidden_dims[0]),
            nn.ReLU(),
            nn.Linear(hidden_dims[0], hidden_dims[1]),
            nn.ReLU(),
            nn.Linear(hidden_dims[1], hidden_dims[2]),
            nn.ReLU(),
            nn.Linear(hidden_dims[2], 8)
        )  # Output dimensions: 8

        # Combine the heads
        self.distilled_policy = nn.Sequential(
            image_encoder,
            nn.ModuleList([head_ik_2_position_rel_15, 
                        head_ik_2_position_abs_15, 
                        head_ik_2_pose_rel_15, 
                        head_ik_2_pose_abs_15, 
                        head_default_2_pose_rel_15])
        ).to("cuda")

        self.distilled_policy.load_state_dict(torch.load(checkpoint_weights))
        self.distilled_policy.eval()
    
    def forward(self, x):
        # Perform forward pass through the image encoder
        input_image = x[..., -15].view(-1, 128, 128, 3).permute(0, 3, 1, 2)
        image_features = self.distilled_policy[0](self.actor_preprocess(input_image))

        # Initialize a list to store outputs from each head
        head_outputs = []

        # Iterate through each head in the ModuleList and compute their outputs
        for head in self.distilled_policy[1]:  # Assuming multi_task_model[1] contains the ModuleList of heads
            output = head(image_features)
            head_outputs.append(output)

        return head_outputs[2]

class Data:
    obs = {}
    object_state = np.zeros(7)
    action = np.zeros(7)
    robot_pose = np.zeros(7)
    done = False
    success = False
    message = ""

class Robot:
    def __init__(self, robot_name=None, ckpt_path=None, video_path=None, rollout_horizon=None, seed=None, task_name=None, env_cfg=None, is_target=False):
        """_summary_

        Args:
            robot_name (string, optional): one of [ur5, franka, jaco]
            ckpt_path (string, optional): 
            video_path (string, optional): 
            rollout_horizon (int, optional): 
            seed (int, optional): 
            connection (socket, optional):
        """
        self.robot_name = robot_name
        self.ckpt_path = ckpt_path
        self.video_path = video_path
        self.rollout_horizon = rollout_horizon
        self.seed = seed
        self.write_video = (video_path is not None)
        self.video_writer = imageio.get_writer(video_path, fps=20) if self.write_video else None
        self.task = task_name

        self.env_cfg = env_cfg
        if self.env_cfg is None:
            self.env_cfg = parse_env_cfg(self.task, use_gpu=True, num_envs=1)

        self.is_target = is_target
        if self.is_target:
            self.env_cfg.control.control_type = "inverse_kinematics"
            self.env_cfg.control.inverse_kinematics.command_type = "pose_abs"

        self.prev_gripper_action = None

        # Set the robot configuration
        set_robot_configuration(robot_name, self.env_cfg)
        self.env = gym.make(task_name, cfg=self.env_cfg)
        self.env = RslRlVecEnvWrapper(self.env)

        # create environment from saved checkpoint
        self.device = TorchUtils.get_torch_device(try_to_use_cuda=True)
        self.num_robots = 1

        self.agent_cfg = parse_rslrl_cfg(self.task)
        self.agent_cfg["seed"] = seed

        if self.ckpt_path is not None:
            # ppo_runner = OnPolicyRunner(env=self.env, train_cfg=self.agent_cfg, log_dir=None, device=self.device)
            # ppo_runner.load(self.ckpt_path)
            # self.policy = ppo_runner.get_inference_policy(device=self.device)
            self.policy = DistilledPolicy(self.ckpt_path).to(self.device)

        # set seed
        if self.seed is not None:
            self.set_seed(self.seed)
        
        self.tracking_error_history = []
        self.renderer = OrbitRenderer(robot_path="/World/envs/env_0/Robot", device="cuda")
        self.control_delta = False

        self.initialize_robot()

    def set_seed(self, seed):
        np.random.seed(seed)
        torch.manual_seed(seed)
        self.agent_cfg["seed"] = seed
        if self.ckpt_path is not None:
            # ppo_runner = OnPolicyRunner(env=self.env, train_cfg=self.agent_cfg, log_dir=None, device=self.device)
            # ppo_runner.load(self.ckpt_path)
            # self.policy = ppo_runner.get_inference_policy(device=self.device)
            self.policy = DistilledPolicy(self.ckpt_path).to(self.device)

    def initialize_robot(self):
        self.renderer.initialize()
        self.obs = self.env.reset()
        
    def compute_pose_error(self, target_pose):
        starting_pose = self.compute_eef_pose()
        # quarternions are equivalent up to sign
        error = min(np.linalg.norm(starting_pose - target_pose), np.linalg.norm(starting_pose - np.concatenate((target_pose[:3], -target_pose[3:]))))
        return error, starting_pose
    
    def drive_robot_to_target_pose(self, target_pose=None, tracking_error_threshold=0.003, num_iter_max=5):        
        error, starting_pose = self.compute_pose_error(target_pose)
        num_iters = 0
        while error > tracking_error_threshold and num_iters < num_iter_max:
            assert len(target_pose) == 7, "Target pose should be 7DOF"
            action = np.zeros(8)
            if self.is_target:
                action[-1] = 1.0

            action[:3] = target_pose[:3]
            action[3:7] = target_pose[3:]
            
            action = torch.tensor(action, dtype=torch.float32, device=self.env.device).unsqueeze(0)
            self.obs, _, _, _, _ = self.env.step(action)

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
        # self.env_cfg.control.inverse_kinematics.command_type = "pose_rel"
        # TODO: Make general
        if self.is_target:
            self.env_cfg.control.inverse_kinematics.command_type = "pose_abs"


    def compute_eef_pose(self):
        """return a 7D vector"""
        pose = []
        pose.append(self.env.observation_manager.tool_positions(self.env).cpu().numpy()[0])
        pose.append(self.env.observation_manager.tool_orientations(self.env).cpu().numpy()[0])
        pose = np.concatenate(pose)
        return pose


    def get_object_state(self):
        return torch.concat((self.env.observation_manager.object_positions(self.env), self.env.observation_manager.object_orientations(self.env)), dim=-1)
    
    def set_object_state(self, target_object_state):
        root_state = torch.zeros(1, 13, device=self.env.device)
        root_state[0, :7] = target_object_state
        self.env.object.set_root_state(root_state, env_ids=None)

    def step(self, action, use_delta=True, blocking=False, tracking_error_threshold=0.003, num_iter_max=1, goal_pose=None):
        """
        If not blocking, action is EEF (delta) pose (6DOF) + gripper
        If blocking, action is EEF target state (7DOF using quarternion) + gripper
        """
        # TODO: Change to be general
        if self.is_target:

            if not blocking:
                assert (len(action) == 7 and self.num_robots == 1) or (len(action) == 14 and self.num_robots == 2), "Action should be 7DOF"
                self.env._ik_controller.cfg.command_type = "pose_abs"
                next_obs, r, done, _ = self.env.step(action) # just execute action
                if goal_pose is None:
                    self.tracking_error_history.append(0)
                else:
                    actual_pose = self.compute_eef_pose()
                    error = np.linalg.norm(goal_pose - actual_pose)
                    self.tracking_error_history.append(error)
            else:
                # robot_env.py #L583
                # single_arm.py #L247
                # osc.py #L264
                if use_delta:
                    self.env_cfg.control.inverse_kinematics.command_type = "pose_rel"
                    # convert to equivalent absolute actions
                    next_obs, next_obs_critic, r, done, _ = self.env.step(action) 
                else:
                    assert action.shape[-1] == 8 and self.num_robots == 1, "Action should be 8DOF"
                    self.env_cfg.control.inverse_kinematics.command_type = "pose_abs"
                    action_target = action

                    gripper_action = torch.clone(action_target[:, -1])
                    gripper_action =  -(gripper_action - 0.04) * 5 - 0.2
                    if self.prev_gripper_action is None:
                        self.prev_gripper_action = gripper_action.clone()
                    
                    # print("Gripper action: ", gripper_action)
                    # print("Prev gripper action: ", self.prev_gripper_action)

                    if self.is_target:
                        # Keep target open before closing
                        action_target[:, -1] = torch.clone(self.prev_gripper_action)

                    error = np.inf
                    num_iters = 0
                    while error > tracking_error_threshold and num_iters < num_iter_max:
                        next_obs, next_obs_critic, r, done, _ = self.env.step(action_target)
                        actual_pose = self.compute_eef_pose()
                        error = np.linalg.norm(action[0, :-1].detach().cpu().numpy() - actual_pose)
                        num_iters += 1

                    print("Take {} iterations to drive robot to target pose".format(num_iters))
                    if error > tracking_error_threshold:
                        print("Warning: did not reach target pose, error: ", error)
                    self.tracking_error_history.append(error)

                    if self.is_target:
                        # Close target after reaching target pose
                        action_target[:, -1] = gripper_action
                        next_obs, _, r, done, _ = self.env.step(action_target)
                        self.prev_gripper_action = torch.clone(gripper_action)
                        actual_pose = self.compute_eef_pose()
                        error = np.linalg.norm(action[0, :-1].detach().cpu().numpy() - actual_pose)
                        num_iters += 1

        else:
            next_obs, _, r, done, _ = self.env.step(action)
            self.tracking_error_history.append(0)


        # 0.08 is the threshold
        success = self.env.reward_manager.lifting_object_success(self.env, 0.08)
        
        self.obs = torch.clone(next_obs)
        return action, r, done, success

    
    def run_experiments(self, seeds, rollout_num_episodes=1, video_skip=5, save_stats_path=None, tracking_error_threshold=0.003, num_iter_max=10, target_robot_delta_action=False):
        """target_robot_delta_action only affects the target robot. Default is to track the absolute pose of the source robot."""
        avg_rollout_stats = dict(Seeds=[], Return=[], Horizon=[], Success_Rate=[], Num_Success=[])
        for seed in seeds:
            print("Seed: ", seed)
            self.set_seed(seed)
            rollout_stats = []
            for i in range(rollout_num_episodes):
                self.set_seed(seed * rollout_num_episodes +i)
                print("Rollout {}/{}".format(i + 1, rollout_num_episodes))
                stats, traj = self.rollout_robot(
                    video_skip=video_skip,
                    # set_object_state=False,
                    set_robot_pose=False, # no need to set it to true since the target robot will be tracking the source robot
                    tracking_error_threshold=tracking_error_threshold, # used only by the target robot because it is blocking
                    num_iter_max=num_iter_max, # used only by the target robot because it is blocking
                    target_robot_delta_action = target_robot_delta_action
                )
                rollout_stats.append(stats)
                
            rollout_stats = TensorUtils.list_of_flat_dict_to_dict_of_list(rollout_stats)
            for k in rollout_stats:
                if isinstance(rollout_stats[k][0], torch.Tensor):
                    for i in range(len(rollout_stats[k])):
                        rollout_stats[k][i] = rollout_stats[k][i].detach().cpu().numpy()
                avg_rollout_stats[k].append(np.mean(rollout_stats[k]))
            avg_rollout_stats["Num_Success"].append(np.sum(rollout_stats["Success_Rate"]))
            avg_rollout_stats["Seeds"].append(seed)
        avg_rollout_stats["Robot"] = self.robot_name
        print("Average Rollout Stats:")
        print(avg_rollout_stats)
        summary_stats = {k : (np.mean(avg_rollout_stats[k]), np.std(avg_rollout_stats[k])) for k in avg_rollout_stats if k not in ["Seeds", "Robot"]}
        summary_stats["tracking_error"] = (np.mean(self.tracking_error_history), np.std(self.tracking_error_history))
        summary_stats["config"] = dict()
        summary_stats["config"]["Robot"] = avg_rollout_stats["Robot"]
        summary_stats["config"]["tracking_error_threshold"] = tracking_error_threshold
        summary_stats["config"]["num_iter_max"] = num_iter_max
        print("Summary Stats:")
        print(summary_stats)
        # if save_stats_path is not None:
        #     with open(save_stats_path, "w") as f:
        #         json.dump(avg_rollout_stats, f, indent=4)
        #         json.dump(summary_stats, f, indent=4)
        
        if self.write_video:
            self.video_writer.close()
        
        if self.s is not None:
            self.s.close()

class SourceRobot(Robot):
    def __init__(self, robot_name=None, ckpt_path=None, video_path=None, rollout_horizon=None, seed=None, connection=None, port = 50007, passive=True, task_name=None):
        super().__init__(robot_name=robot_name, ckpt_path=ckpt_path, video_path=video_path, rollout_horizon=rollout_horizon, seed=seed, task_name=task_name)
        
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
        
    def rollout_robot(self, video_skip=5, return_obs=False, set_object_state=True, set_robot_pose=False, tracking_error_threshold=0.003, num_iter_max=100, target_robot_delta_action=False, demo_index=0):
        """
        Helper function to carry out rollouts. Supports on-screen rendering, off-screen rendering to a video, 
        and returns the rollout trajectory.
        
        The source robot will:
            - optionally receive the target object state and/or target robot pose from the target robot, and then set its environment to that state and/or pose.
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
        if False: #self.passive:
            # the source robot needs to be first initialized to the target object state and target robot pose
            # before the target robot can start executing the policy
            # receive target object state and target robot pose from target robot
            if self.conn is not None:
                data = self.conn.recv(4096)
                target_env_robot_state = pickle.loads(data)
                # print("Receiving target object state and target robot pose from target robot")
                
                self.set_object_state(set_to_target_object_state=target_env_robot_state.object_state)
                self.drive_robot_to_target_pose(target_env_robot_state.robot_pose)
                
                # tell the target robot that the source robot is ready
                # Create an instance of Data() to send to client.
                variable = Data()
                variable.message = "Ready"
                # Pickle the object and send it to the server
                data_string = pickle.dumps(variable)
                self.conn.send(data_string)
        else:
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
                self.conn.send(data_string)
                # confirm that the target robot is ready
                data = self.conn.recv(4096)
                target_env_robot_state = pickle.loads(data)
                print("Receiving target object state and target robot pose from target robot")
                assert target_env_robot_state.message == "Ready", "Target robot is not ready"
        
        
        video_count = 0  # video frame counter
        total_reward = 0.
        state_dict = self.env.observation_manager.compute()
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
                    # breakpoint()
                    # import time
                    # time.sleep(0.1)
                    data = self.conn.recv(4096)
                    target_env_robot_state = pickle.loads(data)
                    assert target_env_robot_state.message == "Request for Action", "Wrong synchronization"
                    print("Receiving target object state and target robot pose from target robot")
                    # if target_env_robot_state.done:
                    #     print("Target robot is done")
                    #     break
                    # if target_env_robot_state.success:
                    #     print("Target robot is successful")
                    #     break
                
                if set_object_state:
                    self.set_object_state(target_object_state=target_env_robot_state.object_state)
                if set_robot_pose:
                    self.drive_robot_to_target_pose(target_env_robot_state.robot_pose)
            
            # state_dict and obs are before taking the action
            state_dict = self.env.observation_manager.compute()
            
            obs = self.obs[0].clone()
            action = self.policy(obs) # get action from policy
            action = action.squeeze().unsqueeze(0) # add batch dimension
            action, r, done, success = self.step(action, use_delta=self.control_delta, blocking=True)
            if success:
                has_succeeded = True
            next_obs = self.obs[0].clone()
            total_reward += r
            
            # if the target robot has succeeded, allow 10 more steps for the source robot to finish
            if target_finished_step is not None and not self.passive:
                if step_i - target_finished_step >= 10:
                    done = True
            
            if self.conn is not None:
                # Create an instance of Data() to send to client.
                variable = Data()
                # variable.obs = obs
                variable.action = action[0].detach().cpu().numpy()
                variable.object_state = self.get_object_state()
                variable.robot_pose = self.compute_eef_pose()
                variable.done = done
                variable.success = success
                variable.message = "Respond with Action"
                # Pickle the object and send it to the server
                data_string = pickle.dumps(variable)
                self.conn.send(data_string)
            
            # visualization
            if self.write_video:
                if video_count % video_skip == 0:
                    video_img = []
                    render_result = self.renderer.render_current_view()
                    video_img.append(render_result.rgb.cpu().numpy()[:, :, :3])
                    video_img = np.concatenate(video_img, axis=1) # concatenate horizontally
                    self.video_writer.append_data(video_img)

                video_count += 1

            # collect transition
            traj["actions"].append(action)
            traj["rewards"].append(r)
            traj["dones"].append(done)
            traj["states"].append(state_dict["policy"])
            if return_obs:
                # Note: We need to "unprocess" the observations to prepare to write them to dataset.
                #       This includes operations like channel swapping and float to uint8 conversion
                #       for saving disk space.
                traj["obs"] = obs
                traj["next_obs"] = next_obs


            # confirm that the target robot is ready for the next iteration
            if self.conn is not None:
                data = self.conn.recv(4096)
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
                    traj[k][kp] = np.array(traj[k][kp].cpu())
            elif isinstance(traj[k], list):
                for tensor in traj[k]:
                    if isinstance(tensor, torch.Tensor):
                        tensor = np.array(tensor.detach().cpu())
                    else:
                        tensor = np.array(tensor)
            else:
                if isinstance(traj[k], torch.Tensor):
                    traj[k] = np.array(traj[k].cpu())
                else:
                    traj[k] = np.array(traj[k])

        
        return stats, traj

if __name__ == "__main__":
    source_robot = SourceRobot(robot_name=args.robot_name, ckpt_path=args.agent, video_path=args.video_path, rollout_horizon=args.horizon, seed=None, passive=args.passive, port=args.port, connection=args.connection, task_name=args.task)
    source_robot.run_experiments(seeds=args.seeds, rollout_num_episodes=args.n_rollouts, video_skip=args.video_skip, save_stats_path=args.save_stats_path, tracking_error_threshold=args.tracking_error_threshold, num_iter_max=args.num_iter_max)