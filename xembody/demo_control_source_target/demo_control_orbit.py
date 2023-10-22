import argparse

from omni.isaac.kit import SimulationApp

# add argparse arguments
parser = argparse.ArgumentParser("Welcome to Orbit: Omniverse Robotics Environments!")
parser.add_argument("--headless", action="store_true", default=False, help="Force display off at all times.")
parser.add_argument("--robot_type", type=str, default="franka_panda", help="Name of the robot type.")
parser.add_argument("--task", type=str, default=None, help="Task to use.")
parser.add_argument("--num_envs", type=int, default=128, help="Number of environments to spawn.")
parser.add_argument("--data_save_dir", type=str, default=None, help="Directory to save the files in.")
parser.add_argument("--is_replay_robot", action="store_true", help="If the flag is set, this run will be that of the replay robot.")

args_cli = parser.parse_args()

# launch omniverse app
config = {"headless": args_cli.headless}
simulation_app = SimulationApp(config)


"""Rest everything follows."""


import torch
import gym
import pickle
import numpy as np
import time
import os

import omni.isaac.core.utils.prims as prim_utils
from omni.isaac.cloner import GridCloner
from omni.isaac.core.simulation_context import SimulationContext
from omni.isaac.core.utils.carb import set_carb_setting
from omni.isaac.core.utils.viewports import set_camera_view
from omni.isaac.orbit_envs.utils import parse_env_cfg

import omni.isaac.orbit.utils.kit as kit_utils
from omni.isaac.orbit.controllers.differential_inverse_kinematics import (
    DifferentialInverseKinematics,
    DifferentialInverseKinematicsCfg,
)
from omni.isaac.orbit.markers import StaticMarker
from omni.isaac.orbit.robots.config.franka import FRANKA_PANDA_ARM_WITH_PANDA_HAND_CFG
from omni.isaac.orbit.robots.config.universal_robots import UR10_CFG, UR5_CFG
from omni.isaac.orbit.robots.config.kinova import JACO_CFG
from omni.isaac.orbit.robots.single_arm import SingleArmManipulator
from omni.isaac.orbit.utils.assets import ISAAC_NUCLEUS_DIR

def get_ee_poses(env):
    return torch.cat((env.observation_manager.tool_positions(env), env.observation_manager.tool_orientations(env)), dim=1)

class ActionRecorder(gym.Wrapper):
    def __init__(self, env, file_path):
        super().__init__(env)
        self._file_path = file_path
        self._obs = []
    
    def step(self, action):
        obs, reward, terminated, info = self.env.step(action)
        # self._obs.append(obs)
        self._obs.append(get_ee_poses(self.env)[0])
        with open(self._file_path, "wb") as f:
            pickle.dump(self._obs, f)
        return obs, reward, terminated, info

class ReplayAgent(object):

    def __init__(self, source_data_file: str):
        self.source_data_file = source_data_file

        # Load up the data
        with open(self.source_data_file, 'rb') as f: 
            self.data = pickle.load(f)
        self.step = 0

    def get_initial_gripper_pose(self):
        return self.data[0]
    
    def act(self):
        action = np.zeros(8)
        if self.step < len(self.data):
            action = self.data[self.step]
            action = action.cpu().numpy()
        self.step += 1
        gripper = [1.0]  # Always open
        return torch.from_numpy(np.concatenate([action, gripper], axis=-1)[None, :]).to('cuda:0')
    
"""
Main
"""

def get_robot_conf(robot_name: str):
    # -- Robot
    # resolve robot config from command-line arguments
    robot_cfg = None
    if robot_name == "franka_panda":
        robot_cfg = FRANKA_PANDA_ARM_WITH_PANDA_HAND_CFG
    elif robot_name == "ur10":
        robot_cfg = UR10_CFG
    elif robot_name == "ur5":
        robot_cfg = UR5_CFG
    elif robot_name == "jaco":
        robot_cfg = JACO_CFG
    else:
        raise ValueError(f"Robot {robot_name} is not supported. Valid: franka_panda, ur10, ur5, jaco")
    return robot_cfg
    
def make_recorded_env(env_cfg, robot_cfg, video_folder, file_path):
    env_cfg.robot = robot_cfg
    
    env_cfg.viewer.resolution = (640, 480)
    
    env = gym.make(args_cli.task, cfg=env_cfg, headless=args_cli.headless, viewport=True)    
    video_kwargs = {
        "video_folder": video_folder,
        "step_trigger": lambda step: step % 1500 == 0,
        "video_length": 200,
    }

    env = gym.wrappers.RecordVideo(env, **video_kwargs)
    env = ActionRecorder(env, file_path)
    return env

def get_random_action():
    arm = np.random.normal(0.0, 0.4, size=(6,))
    gripper = [1.0]  # Always open
    return np.concatenate([arm, gripper], axis=-1)

def print_pose_errors(current_ee, desired_ee):
    print('Translation error:', torch.linalg.norm(current_ee[:3] - desired_ee[:3]))
    print('Rotation error:', torch.linalg.norm(current_ee[3:] - desired_ee[3:]))

def main():
    """Spawns a single-arm manipulator and applies commands through inverse kinematics control."""

    # parse configuration
    env_cfg = parse_env_cfg(args_cli.task, num_envs=args_cli.num_envs)
    robot_cfg = get_robot_conf(args_cli.robot_type)

    save_dir_source = f'{args_cli.data_save_dir}/source_robot'
    save_dir_source_data_name = os.path.join(save_dir_source, 'data.pkl')
    
    if not args_cli.is_replay_robot:
        # modify configuration
        env_cfg.control.control_type = "inverse_kinematics"
        env_cfg.control.inverse_kinematics.command_type = "pose_rel"
        env_cfg.terminations.episode_timeout = False
        # create environment
        env = make_recorded_env(env_cfg, robot_cfg, save_dir_source, save_dir_source_data_name)
        env.reset()
        
        # simulate environment
        print('Relative errors:')
        prev_ee_position = torch.zeros(7, device=env.device)
        for _ in range(200):
            # convert to torch
            delta_pose = get_random_action()
            actions = torch.tensor(delta_pose, dtype=torch.float, device=env.device).repeat(env.num_envs, 1)
            # apply actions
            obs, _, _, _ = env.step(actions)
            curr_ee = get_ee_poses(env)[0]
            # print_pose_errors(curr_ee, prev_ee_position)
            prev_ee_position = curr_ee
            # check if simulator is stopped
            if env.unwrapped.sim.is_stopped():
                break
    else:
        save_dir_target = f'{args_cli.data_save_dir}/target_robot'
        save_dir_target_data_name = os.path.join(save_dir_target, 'data.pkl')
            
        env_cfg.control.control_type = "inverse_kinematics"
        env_cfg.control.inverse_kinematics.command_type = "pose_abs"
        env_cfg.terminations.episode_timeout = False
        env = make_recorded_env(env_cfg, robot_cfg, save_dir_target, save_dir_target_data_name)
        env.reset()

        follower_actor = ReplayAgent(save_dir_source_data_name)
        start_pose = follower_actor.get_initial_gripper_pose()
        # env.robot.articulations.set_joint_positions(start_pose)
        
        print('Absolute errors:')
        for _ in range(200):
            actions = follower_actor.act()
            translation_error = torch.Tensor([10000000000]).to(env.device)
            # apply actions
            # while translation_error.cpu().numpy() > 0.01:
            obs, _, _, _ = env.step(actions)
            ee_pose = get_ee_poses(env)[0]
            translation_error = torch.linalg.norm(actions[0, :3] - ee_pose[:3])
            print_pose_errors(get_ee_poses(env)[0], actions[0, :7])
                # check if simulator is stopped
            if env.unwrapped.sim.is_stopped():
                break

if __name__ == "__main__":
    # Run IK example with Manipulator
    main()
    # Close the simulator
    simulation_app.close()
