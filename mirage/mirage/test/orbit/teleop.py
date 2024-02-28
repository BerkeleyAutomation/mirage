# Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES, ETH Zurich, and University of Toronto
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Script to run a keyboard teleoperation with Orbit manipulation environments."""

"""Launch Isaac Sim Simulator first."""


import argparse

from omni.isaac.kit import SimulationApp

# add argparse arguments
parser = argparse.ArgumentParser("Welcome to Orbit: Omniverse Robotics Environments!")
parser.add_argument("--headless", action="store_true", default=False, help="Force display off at all times.")
parser.add_argument("--cpu", action="store_true", default=False, help="Use CPU pipeline.")
parser.add_argument("--num_envs", type=int, default=1, help="Number of environments to simulate.")
parser.add_argument("--device", type=str, default="keyboard", help="Device for interacting with environment")
parser.add_argument("--task", type=str, default=None, help="Name of the task.")
parser.add_argument("--robot", type=str, default=None, help="Name of robot.")
parser.add_argument("--sensitivity", type=float, default=1.0, help="Sensitivity factor.")
args_cli = parser.parse_args()

# launch the simulator
config = {"headless": args_cli.headless}
simulation_app = SimulationApp(config)

"""Rest everything follows."""


import gym
import torch

import carb

from omni.isaac.orbit.devices import Se3Gamepad, Se3Keyboard, Se3SpaceMouse

import omni.isaac.contrib_envs  # noqa: F401
import omni.isaac.orbit_envs  # noqa: F401
from omni.isaac.orbit_envs.utils import parse_env_cfg
from omni.isaac.orbit.robots.config.franka import FRANKA_PANDA_ARM_WITH_PANDA_HAND_CFG
from omni.isaac.orbit.robots.config.universal_robots import UR10_CFG, UR5_CFG
from omni.isaac.orbit.robots.config.kinova import JACO_CFG
from omni.isaac.orbit.robots.single_arm import SingleArmManipulator
from omni.isaac.orbit.utils.assets import ISAAC_NUCLEUS_DIR
from mirage.orbit.orbit_renderer import OrbitRenderer
import cv2
import open3d as o3d
import numpy as np


def pre_process_actions(delta_pose: torch.Tensor, gripper_command: bool) -> torch.Tensor:
    """Pre-process actions for the environment."""
    # compute actions based on environment
    if "Reach" in args_cli.task:
        # note: reach is the only one that uses a different action space
        # compute actions
        return delta_pose
    else:
        # resolve gripper command
        gripper_vel = torch.zeros(delta_pose.shape[0], 1, device=delta_pose.device)
        gripper_vel[:] = -1.0 if gripper_command else 1.0
        # compute actions
        return torch.concat([delta_pose, gripper_vel], dim=1)


def main():
    """Running keyboard teleoperation with Orbit manipulation environment."""
    # parse configuration
    env_cfg = parse_env_cfg(args_cli.task, use_gpu=not args_cli.cpu, num_envs=args_cli.num_envs)
    # modify configuration
    env_cfg.control.control_type = "inverse_kinematics"
    env_cfg.control.inverse_kinematics.command_type = "pose_rel"
    env_cfg.terminations.episode_timeout = False
    # create environment
    if args_cli.robot == "franka_panda":
        robot_cfg = FRANKA_PANDA_ARM_WITH_PANDA_HAND_CFG
    elif args_cli.robot == "ur10":
        robot_cfg = UR10_CFG
    elif args_cli.robot == "ur5":
        robot_cfg = UR5_CFG
    elif args_cli.robot == "jaco":
        robot_cfg = JACO_CFG
    else:
        raise ValueError(f"Robot {args_cli.robot} is not supported. Valid: franka_panda, ur10, ur5, jaco")
    env_cfg.robot = robot_cfg

    env = gym.make(args_cli.task, cfg=env_cfg, headless=args_cli.headless)
    # check environment name (for reach , we don't allow the gripper)
    if "Reach" in args_cli.task:
        carb.log_warn(
            f"The environment '{args_cli.task}' does not support gripper control. The device command will be ignored."
        )


    # create controller
    if args_cli.device.lower() == "keyboard":
        teleop_interface = Se3Keyboard(
            pos_sensitivity=0.1 * args_cli.sensitivity, rot_sensitivity=0.5 * args_cli.sensitivity
        )
    elif args_cli.device.lower() == "spacemouse":
        teleop_interface = Se3SpaceMouse(
            pos_sensitivity=0.05 * args_cli.sensitivity, rot_sensitivity=0.005 * args_cli.sensitivity
        )
    elif args_cli.device.lower() == "gamepad":
        teleop_interface = Se3Gamepad(
            pos_sensitivity=0.1 * args_cli.sensitivity, rot_sensitivity=0.1 * args_cli.sensitivity
        )
    else:
        raise ValueError(f"Invalid device interface '{args_cli.device}'. Supported: 'keyboard', 'spacemouse'.")
    # add teleoperation key for env reset
    teleop_interface.add_callback("L", env.reset)
    # print helper for keyboard
    print(teleop_interface)

    # reset environment
    env.reset()
    teleop_interface.reset()

    count = 0
    orbit_renderer = OrbitRenderer(robot_path="/World/envs/env_0/Robot", device="cuda", use_segmentation=True)

    intrinsic_matrix = np.array([[528.433756, 0.0, 320.5],
                                 [0.0, 528.433756, 240.5],
                                 [0.0, 0.0, 1.0]])
    camera_translation = np.array([1.5, 1.5, 1.5])

    orbit_renderer.initialize(camera_translation, intrinsics=intrinsic_matrix)

    # simulate environment
    while simulation_app.is_running():
        # get keyboard command
        delta_pose, gripper_command = teleop_interface.advance()
        if count % 450 == 0:
            render_result = orbit_renderer.render_current_view()

            rgb_numpy = render_result.rgb.cpu().numpy()[:, :, :3]
            bgr_numpy = cv2.cvtColor(rgb_numpy, cv2.COLOR_RGB2BGR)
            cv2.imwrite('img.jpg', bgr_numpy)

            segmentation_mask_numpy = render_result.segmentation_mask.cpu().numpy()
            cv2.imwrite('seg.jpg', segmentation_mask_numpy)

            np.save('rgbd.npy', render_result.rgbd_image.detach().cpu().numpy())
            
            # point_cloud = render_result.point_cloud.cpu().numpy()
            # pcd.points = o3d.utility.Vector3dVector(point_cloud)
            # o3d.io.write_point_cloud("point_cloud.pcd", pcd)

            np.savetxt('joints.txt', env.robot.data.arm_dof_pos.detach().cpu().numpy())
            np.savetxt('gripper_joints.txt', env.robot.data.tool_dof_pos.detach().cpu().numpy())

        # convert to torch
        delta_pose = torch.tensor(delta_pose, dtype=torch.float, device=env.device).repeat(env.num_envs, 1)
        # pre-process actions
        actions = pre_process_actions(delta_pose, gripper_command)
        # apply actions
        _, _, _, _ = env.step(actions)
        # check if simulator is stopped
        if env.unwrapped.sim.is_stopped():
            break
        count += 1

    # close the simulator
    env.close()
    simulation_app.close()


if __name__ == "__main__":
    main()
