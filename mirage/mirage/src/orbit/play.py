# Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES, ETH Zurich, and University of Toronto
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Script to play a checkpoint if an RL agent from RSL-RL."""

"""Launch Isaac Sim Simulator first."""


import argparse

from omni.isaac.kit import SimulationApp

# add argparse arguments
parser = argparse.ArgumentParser("Welcome to Orbit: Omniverse Robotics Environments!")
parser.add_argument("--headless", action="store_true", default=False, help="Force display off at all times.")
parser.add_argument("--cpu", action="store_true", default=False, help="Use CPU pipeline.")
parser.add_argument("--num_envs", type=int, default=None, help="Number of environments to simulate.")
parser.add_argument("--task", type=str, default=None, help="Name of the task.")
parser.add_argument("--checkpoint", type=str, default=None, help="Path to model checkpoint.")
args_cli = parser.parse_args()

# launch the simulator
config = {"headless": args_cli.headless}
simulation_app = SimulationApp(config)

"""Rest everything follows."""


import gym
import os
from datetime import datetime
from rsl_rl.runners import OnPolicyRunner

import omni.isaac.contrib_envs  # noqa: F401
import omni.isaac.orbit_envs  # noqa: F401
from omni.isaac.orbit_envs.utils import get_checkpoint_path, parse_env_cfg
from omni.isaac.orbit_envs.utils.wrappers.rsl_rl import RslRlVecEnvWrapper, export_policy_as_onnx
from omni.isaac.orbit.utils.dict import print_dict
from config import parse_rslrl_cfg


def main():
    """Play with RSL-RL agent."""
    # parse configuration
    env_cfg = parse_env_cfg(args_cli.task, use_gpu=not args_cli.cpu, num_envs=args_cli.num_envs)
    agent_cfg = parse_rslrl_cfg(args_cli.task)

    # create isaac environment
    env = gym.make(args_cli.task, cfg=env_cfg, headless=args_cli.headless, viewport=True)
    
    # specify directory for logging experiments
    log_root_path = os.path.join("logs", "rsl_rl", agent_cfg["runner"]["experiment_name"])
    log_root_path = os.path.abspath(log_root_path)
    print(f"[INFO] Logging experiment in directory: {log_root_path}")
    # specify directory for logging runs
    log_dir = datetime.now().strftime("%b%d_%H-%M-%S")
    if agent_cfg["runner"]["run_name"]:
        log_dir += f"_{agent_cfg['runner']['run_name']}"
    log_dir = os.path.join(log_root_path, log_dir)
    video_kwargs = {
        "video_folder": os.path.join(log_dir, "videos"),
        "step_trigger": lambda step: step % 500 == 0,
        "video_length": 200
    }
    print("[INFO] Recording videos during training.")
    print_dict(video_kwargs, nesting=4)
    env = gym.wrappers.RecordVideo(env, **video_kwargs)
    # wrap around environment for rsl-rl
    env = RslRlVecEnvWrapper(env)

    # specify directory for logging experiments
    log_root_path = os.path.join("logs", "rsl_rl", agent_cfg["runner"]["experiment_name"])
    log_root_path = os.path.abspath(log_root_path)
    print(f"[INFO] Loading experiment from directory: {log_root_path}")
    # get path to previous checkpoint
    if args_cli.checkpoint is None:
        # specify directory for logging runs
        run_dir = "*"
        if agent_cfg["runner"]["load_run"] != -1:
            run_dir = agent_cfg["runner"]["load_run"]
        # specify name of checkpoint
        checkpoint_file = None
        if agent_cfg["runner"]["checkpoint"] != -1:
            checkpoint_file = f"model_{agent_cfg['runner']['checkpoint']}.pt"
        # get path to previous checkpoint
        resume_path = get_checkpoint_path(log_root_path, run_dir, checkpoint_file)
    else:
        resume_path = os.path.abspath(args_cli.checkpoint)
    # load previously trained model
    print(f"[INFO]: Loading model checkpoint from: {resume_path}")

    # create runner from rsl-rl
    ppo_runner = OnPolicyRunner(env, agent_cfg, log_dir=None, device=agent_cfg["device"])
    ppo_runner.load(resume_path)
    # obtain the trained policy for inference
    policy = ppo_runner.get_inference_policy(device=env.unwrapped.device)

    # export policy to onnx
    export_model_dir = os.path.join(os.path.dirname(resume_path), "exported")
    export_policy_as_onnx(ppo_runner.alg.actor_critic, export_model_dir, filename="policy.onnx")

    # reset environment
    obs, _ = env.reset()
    # simulate environment
    while simulation_app.is_running():
        # agent stepping
        actions = policy(obs)
        print(actions)
        # env stepping
        obs, _, rewards, dones, _ = env.step(actions)
        print(rewards, dones)
        # check if simulator is stopped
        if env.unwrapped.sim.is_stopped():
            break

    # close the simulator
    env.close()
    simulation_app.close()


if __name__ == "__main__":
    main()
