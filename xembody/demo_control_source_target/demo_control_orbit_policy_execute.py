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
parser.add_argument("--checkpoint", type=str, default="/home/lawrence/xembody/xembody/xembody/test/orbit/trained_runs/model_650.pt", help="Checkpoint of RSL_RL Policy.")
parser.add_argument("--source_act", action="store_true", help="Should use source policy for target.")
parser.add_argument("--seed", type=int, default=0, help="Seed for the environment.")

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
from moviepy.editor import ImageSequenceClip

import omni.isaac.core.utils.prims as prim_utils
from omni.isaac.cloner import GridCloner
from omni.isaac.core.simulation_context import SimulationContext
from omni.isaac.core.utils.carb import set_carb_setting
from omni.isaac.core.utils.viewports import set_camera_view
from omni.isaac.orbit_envs.utils import parse_env_cfg

from rsl_rl.runners import OnPolicyRunner

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
from omni.isaac.orbit_envs.utils.wrappers.rsl_rl import RslRlVecEnvWrapper

from xembody.src.orbit.orbit_renderer import OrbitRenderer

import os
import yaml
import cv2

from omni.isaac.orbit_envs import ORBIT_ENVS_DATA_DIR

__all__ = ["RSLRL_PPO_CONFIG_FILE", "parse_rslrl_cfg"]

RSLRL_PPO_CONFIG_FILE = {
    # classic
    "Isaac-Cartpole-v0": os.path.join(ORBIT_ENVS_DATA_DIR, "rsl_rl/cartpole_ppo.yaml"),
    # manipulation
    "Isaac-Lift-Franka-v0": os.path.join(ORBIT_ENVS_DATA_DIR, "rsl_rl/lift_ppo.yaml"),
    "Isaac-Reach-Franka-v0": os.path.join(ORBIT_ENVS_DATA_DIR, "rsl_rl/reach_ppo.yaml"),
    # locomotion
    "Isaac-Velocity-Anymal-C-v0": os.path.join(ORBIT_ENVS_DATA_DIR, "rsl_rl/anymal_ppo.yaml"),
}
"""Mapping from environment names to PPO agent files."""


def parse_rslrl_cfg(task_name) -> dict:
    """Parse configuration for RSL-RL agent based on inputs.

    Args:
        task_name (str): The name of the environment.

    Returns:
        dict: A dictionary containing the parsed configuration.
    """
    # retrieve the default environment config file
    try:
        config_file = RSLRL_PPO_CONFIG_FILE[task_name]
    except KeyError:
        raise ValueError(f"Task not found: {task_name}")

    # parse agent configuration
    with open(config_file, encoding="utf-8") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)

    return cfg

def get_ee_poses(env):
    return torch.cat((env.observation_manager.tool_positions(env), env.observation_manager.tool_orientations(env)), dim=1)

class ActionRecorder(gym.Wrapper):
    def __init__(self, env, file_path):
        super().__init__(env)
        self._file_path = file_path
        self._out_dict = {
            "block_pos": env.observation_manager.object_positions(env),
            "obs": []
        }

    def step(self, action):
        obs, reward, terminated, info = self.env.step(action)   
        ee_pose = get_ee_poses(self.env)[0]
        recorded_obs = torch.cat((ee_pose, action[:, -1]), dim=0)
        self._out_dict["obs"].append(recorded_obs)
        with open(self._file_path, "wb") as f:
            pickle.dump(self._out_dict, f)
        return obs, reward, terminated, info
    
    def reset(self):
        out = self.env.reset()
        self._out_dict["block_pos"] = self.env.observation_manager.object_positions(self.env)
        return out

class Agent(object):

    def act(self, obs):
        raise NotImplementedError

class RLAgent(Agent):

    def __init__(self, model_checkpoint: str, task_name: str, env):
        self.model_checkpoint = model_checkpoint

        agent_cfg = parse_rslrl_cfg(task_name)
        resume_path = os.path.abspath(self.model_checkpoint)
        self.ppo_runner = OnPolicyRunner(env, agent_cfg, log_dir=None, device=agent_cfg["device"])
        self.ppo_runner.load(resume_path)
        
        self.policy = self.ppo_runner.get_inference_policy(device=env.unwrapped.device)

    def get_initial_gripper_pose(self):
        return None
    
    def act(self, obs):
        return self.policy(obs)

class ReplayAgent(Agent):

    def __init__(self, source_data_file: str, env):
        self.source_data_file = source_data_file

        # Load up the data
        with open(self.source_data_file, 'rb') as f: 
            self.prev_dict = pickle.load(f)
            self.data = self.prev_dict["obs"]
            self.block_pos = self.prev_dict["block_pos"]

            env_ids = torch.tensor([0], device=env.device)
            self.block_pos[:, 0:3] += env.envs_positions[env_ids]
            # env.object.set_root_state(self.block_pos, env_ids=env_ids)

        self.step = 0

    def get_initial_gripper_pose(self):
        return self.data[0]
    
    def act(self, obs):
        if self.step < len(self.data):
            action = self.data[self.step]
            # action[-1] *= -1
        else:
            return False
        self.step += 1
        return action[None, :]

class VideoRecorderWithOrbit(gym.Wrapper):        
    """
    Writes a video file with images gathered from an OrbitRenderer
    """

    def __init__(self, env, video_folder, step_trigger):
        super().__init__(env)
        self._video_folder = video_folder
        self._step_trigger = step_trigger
        self._step = 0
        self._frames = []

        self._orbit_renderer = OrbitRenderer(robot_path="/World/envs/env_0/Robot", device="cuda", use_segmentation=False, resolution=(720, 1280))
        
        intrinsic_matrix = np.array([[528.433756, 0.0, 320.5],
                                    [0.0, 528.433756, 240.5],
                                    [0.0, 0.0, 1.0]])
        camera_translation = np.array([0.75, 0.75, 1])

        self._orbit_renderer.initialize(camera_translation, intrinsics=intrinsic_matrix)

    def step(self, action):
        obs, reward, terminated, info = self.env.step(action)
        if self._step_trigger(self._step):
            render_result = self._orbit_renderer.render_current_view()
            frame = render_result.rgb.cpu().numpy()[:, :, :3]
            self._frames.append(frame)
        self._step += 1
        return obs, reward, terminated, info
    
    def release(self):
        clip = ImageSequenceClip(self._frames, fps=1 / self.env.dt)
        clip.write_videofile(os.path.join(self._video_folder, "video.mp4"), fps=1 / self.env.dt)

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
    os.makedirs(video_folder, exist_ok=True)
    env_cfg.robot = robot_cfg
    
    env = gym.make(args_cli.task, cfg=env_cfg, headless=args_cli.headless, viewport=True)    
    
    video_kwargs = {
        "video_folder": video_folder,
        "step_trigger": lambda step: step % 1 == 0,
    }
    env = VideoRecorderWithOrbit(env, **video_kwargs)
    env = ActionRecorder(env, file_path)
    return env

def make_recorded_env_for_outer(env_cfg, robot_cfg, video_folder, file_path):
    os.makedirs(video_folder, exist_ok=True)
    env_cfg.robot = robot_cfg
    
    env = gym.make(args_cli.task, cfg=env_cfg, headless=args_cli.headless, viewport=True)    
    
    env = ActionRecorder(env, file_path)
    if args_cli.source_act:
        env = RslRlVecEnvWrapper(env)
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
        # env_cfg.control.control_type = "inverse_kinematics"
        # env_cfg.control.inverse_kinematics.command_type = "pose_abs"
        env_cfg.terminations.episode_timeout = True
        env_cfg.seed = args_cli.seed
        # create environment
        env = make_recorded_env(env_cfg, robot_cfg, save_dir_source, save_dir_source_data_name)
        env = RslRlVecEnvWrapper(env)
        obs, _ = env.reset()

        agent = RLAgent(args_cli.checkpoint, args_cli.task, env)        

        # simulate environment
        print('Relative errors:')
        done = torch.tensor([0], device=env.device)
        
        
        while torch.sum(done) == 0:
            # convert to torch
            actions = agent.act(obs)
            print('Policy output', actions)
            # apply actions

            # actions = torch.zeros_like(actions, device=env.device)
            # actions[0, -1] = current_gripper_value
            # current_gripper_value += 0.01

            print("Gripper Value:", actions[0, -1])

            obs, x, y, done, info = env.step(actions)
            curr_ee = get_ee_poses(env)[0]
            # check if simulator is stopped
            if env.unwrapped.sim.is_stopped():
                break
        is_success = (info["is_success"].sum() > 0).cpu().numpy()
        with open(os.path.join(save_dir_source, 'is_success.txt'), 'wb') as f:
            f.write(str(is_success).encode())
        env.release()
    else:
        save_dir_target = f'{args_cli.data_save_dir}/target_robot'
        save_dir_target_data_name = os.path.join(save_dir_target, 'data.pkl')
            
        # env_cfg.control.control_type = "default"

        env_cfg.control.control_type = "inverse_kinematics"
        env_cfg.control.inverse_kinematics.command_type = "pose_abs"
        env_cfg.terminations.episode_timeout = False
        env_cfg.seed = args_cli.seed
        env = make_recorded_env_for_outer(env_cfg, robot_cfg, save_dir_target, save_dir_target_data_name)
        out_values = env.reset()
        obs = out_values
        # done = out_values[-2]
        # info = out_values[-1]

        follower_actor = ReplayAgent(save_dir_source_data_name, env) if  not \
            args_cli.source_act else RLAgent(args_cli.checkpoint, args_cli.task, env)
        start_pose = follower_actor.get_initial_gripper_pose()
        # env.robot.articulations.set_joint_positions(start_pose)
        
        print('Absolute errors:')
        prev_gripper_action = None
        MAX_ITERS = 20
        with torch.no_grad():
            done = torch.tensor([0], device=env.device)
            _frames = []
            _orbit_renderer = OrbitRenderer(robot_path="/World/envs/env_0/Robot", device="cuda", use_segmentation=False, resolution=(720, 1280))
            intrinsic_matrix = np.array([[528.433756, 0.0, 320.5],
                                        [0.0, 528.433756, 240.5],
                                        [0.0, 0.0, 1.0]])
            camera_translation = np.array([0.75, 0.75, 1])
            _orbit_renderer.initialize(camera_translation, intrinsics=intrinsic_matrix)

            while torch.sum(done) == 0:
                iter = 0
                render_result = _orbit_renderer.render_current_view()
                frame = render_result.rgb.cpu().numpy()[:, :, :3]
                _frames.append(frame)
                actions = follower_actor.act(obs)
                if actions is False:
                    break
                if not args_cli.source_act:
                    print("Input gripper action:", actions[0, -1])
                    print("Output gripper action:", -(actions[0, -1] - 0.04) * 5 - 0.2)
                    gripper_action = torch.clone(-(actions[0, -1] - 0.04) * 5 - 0.2)
                    if prev_gripper_action is None:
                        prev_gripper_action = torch.clone(gripper_action)
                    actions[0, -1] = torch.clone(prev_gripper_action)

                translation_error = torch.Tensor([10000000000]).to(env.device)
                # apply actions
                while translation_error.cpu().numpy() > 0.05 and iter < MAX_ITERS:
                    # import pdb; pdb.set_trace()
                    out_values = env.step(actions)
                    obs = out_values[0]
                    done = out_values[-2]
                    info = out_values[-1]
                    
                    ee_pose = get_ee_poses(env)[0]
                    translation_error = torch.linalg.norm(actions[0, :7] - ee_pose[:7])
                    # print_pose_errors(get_ee_poses(env)[0], actions[0, :7])
                    iter += 1
                # check if simulator is stopped
                if not args_cli.source_act:
                    actions[0, -1] = torch.clone(gripper_action)
                    obs, _, done, info = env.step(actions)
                    prev_gripper_action = torch.clone(gripper_action)
                if env.unwrapped.sim.is_stopped():
                    break
        is_success = (info["is_success"].sum() > 0).cpu().numpy()
        with open(os.path.join(save_dir_target, 'is_success.txt'), 'wb') as f:
            f.write(str(is_success).encode())
        clip = ImageSequenceClip(_frames, fps=1 / env.dt)
        clip.write_videofile(os.path.join(save_dir_target, "video.mp4"), fps=1 / env.dt)


if __name__ == "__main__":
    # Run IK example with Manipulator
    main()
    # Close the simulator
    simulation_app.close()
