

"""
# Mode 1: Target robot following the source robot
python evaluate_policy_demo_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 1 --horizon 400 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_lift_low_dim_2.mp4 --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Sawyer --passive --connection

# Mode 2: Target robot querying the source robot for actions
python evaluate_policy_demo_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 1 --horizon 400 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_lift_low_dim_2.mp4 --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Sawyer --connection

python target_robot_eval.py --agent /home/lawrence/xembody/Orbit/source/standalone/workflows/rsl_rl/models/image_based_multihead_policy_40.pth --n_rollouts 1 --horizon 400 --seed 0 --tracking_error_threshold 0.015 --num_iter_max 300 --connection --task Isaac-Lift-Franka-v0

# Mode 3: Demonstration playback
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift_lowdim_target_sawyer_0.015_300.txt  --connection --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Sawyer --passive --video_path /home/lawrence/xembody/robosuite/collected_data/output_lift_demo_playback_2.mp4 
"""

import argparse
import imageio
import gym
import json
from copy import deepcopy
import socket
import pickle
import time

from rsl_rl.runners import OnPolicyRunner

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
        help="(optional) path to saved checkpoint pth file",
    )
    
    # Path to trained model
    parser.add_argument(
        "--task",
        type=str,
        default=None,
        help="task name in Orbit",
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

    # Whether to render rollouts to screen
    parser.add_argument(
        "--headless",
        action='store_true',
        help="headless mode",
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
        default=None,
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
        help="(optional) if provided, the source robot will drive to the target pose with this tracking error threshold",
    )
    parser.add_argument(
        "--num_iter_max",
        type=int,
        default=3,
        help="(optional) if provided, the source robot will drive to the target pose with this maximum number of iterations",
    )
    parser.add_argument(
        "--delta_action",
        action='store_true',
        help="if True, execute the same delta action as the source robot",
    )
    args = parser.parse_args()
    
    config = {"headless": args.headless}
    simulation_app = SimulationApp(config)

import robomimic
import robomimic.utils.file_utils as FileUtils
import robomimic.utils.torch_utils as TorchUtils
import robomimic.utils.tensor_utils as TensorUtils
import robomimic.utils.obs_utils as ObsUtils
from robomimic.envs.env_base import EnvBase
from robomimic.algo import RolloutPolicy
import robosuite.utils.transform_utils as T
from robosuite.utils.mjcf_utils import array_to_string, string_to_array


from source_robot_eval import Data, Robot

class TargetRobot(Robot):
    def __init__(self, robot_name=None, ckpt_path=None, video_path=None, rollout_horizon=None, seed=None, connection=None, port = 50007, passive=False, task_name=None):
        super().__init__(robot_name=robot_name, ckpt_path=ckpt_path, video_path=video_path, rollout_horizon=rollout_horizon, seed=seed, task_name=task_name, is_target=True)
        
        if connection:
            HOST = 'localhost'
            PORT = port
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((HOST, PORT))
            # self.s.settimeout(3)
        else:
            self.s = None
            
        self.passive = passive
        
    def rollout_robot(self, video_skip=5, return_obs=False, set_object_state=False, set_robot_pose=False, tracking_error_threshold=0.003, num_iter_max=100, target_robot_delta_action=False):        
        # self.initialize_robot()
        
        if True: #self.passive:
            # the target robot needs to be first initialized to the source object state and source robot pose
            # receive source object state and source robot pose from source robot
            if self.s is not None:
                data = self.s.recv(4096)
                source_env_robot_state = pickle.loads(data)
                print("Receiving source object state and source robot pose from source robot")
                assert source_env_robot_state.message == "Ready"
                # self.set_object_state(set_to_target_object_state=source_env_robot_state.object_state)
                self.drive_robot_to_target_pose(source_env_robot_state.robot_pose)
                
                # tell the source robot that the target robot is ready
                # Create an instance of Data() to send to client.
                variable = Data()
                variable.message = "Ready"
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
        state_dict = self.env.observation_manager.compute()
        traj = dict(actions=[], rewards=[], dones=[], states=[], initial_state_dict=state_dict)
        if return_obs:
            # store observations too
            traj.update(dict(obs=[], next_obs=[]))
        
        source_finished_step = None
        has_succeeded = False
        # try:
        for step_i in range(self.rollout_horizon):
            print("Target Step: ", step_i)
            # state_dict and obs are before taking the action
            state_dict = self.env.observation_manager.compute()
            # print("State dict: ", state_dict)
            obs = deepcopy(self.obs)
            
            if not self.passive:
                # send state_dict and obs to source robot
                # Create an instance of Data() to send to client.
                variable = Data()
                # variable.obs = obs
                variable.object_state = self.get_object_state()
                variable.robot_pose = self.compute_eef_pose()
                variable.message = "Request for Action"
                # Pickle the object and send it to the server
                data_string = pickle.dumps(variable)
                self.s.send(data_string)
                time.sleep(0.01) # if we don't sleep, the target robot will not recieve the message
                
                # print("Request for Action")
            
                
            # receive target object state and target robot pose from target robot
            if self.s is not None:
                # breakpoint()
                data = self.s.recv(4096)
                source_env_robot_state = pickle.loads(data)
                assert source_env_robot_state.message == "Respond with Action", "Wrong Synchronization"
                # print("Received actions")
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
                if self.num_robots == 1:
                    action = source_env_robot_state.robot_pose # get action from the source robot
                    # append gripper action
                    action = torch.from_numpy(np.concatenate([action, source_env_robot_state.action[-1:]])).to(self.device).unsqueeze(0)
                else:
                    action_0, action_1 = source_env_robot_state.robot_pose[:7], source_env_robot_state.robot_pose[7:]
                    # append gripper action
                    action = np.concatenate([action_0, source_env_robot_state.action[6:7], action_1, source_env_robot_state.action[-1:]])
                action, r, done, success = self.step(action, use_delta=False, blocking=True, tracking_error_threshold=tracking_error_threshold, num_iter_max=num_iter_max)
            if success:
                has_succeeded = True
            next_obs = deepcopy(self.obs)[0]
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
            self.s.send(data_string)

            # collect transition
            traj["actions"].append(action)
            traj["rewards"].append(r)
            traj["dones"].append(done)
            traj["states"].append(state_dict["policy"])
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
    time.sleep(30) # wait for the server to start
    target_robot = TargetRobot(robot_name=args.robot_name, ckpt_path=args.agent, video_path=args.video_path, rollout_horizon=args.horizon, passive=args.passive, port=args.port, connection=args.connection, task_name=args.task)
    target_robot.run_experiments(seeds=args.seeds, rollout_num_episodes=args.n_rollouts, video_skip=args.video_skip, save_stats_path=args.save_stats_path, tracking_error_threshold=args.tracking_error_threshold, num_iter_max=args.num_iter_max, target_robot_delta_action=args.delta_action)