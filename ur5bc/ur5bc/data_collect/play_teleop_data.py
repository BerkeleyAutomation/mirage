import numpy as np
from ur5py.ur5 import UR5Robot
import subprocess
import cv2
import os
from autolab_core import CameraIntrinsics,RigidTransform
import time
import threading
import queue
import pickle
from PIL import Image
from ur5.robot_env import RobotEnv
from ur5.spacemouse import SpaceMouseRobotController


def main():
    env = RobotEnv()
    index = 169
    saving_directory = "/home/lawrence/robotlerf/ur5bc/data/raw/teleop"
    with open(os.path.join(saving_directory, f"traj{index}", "state_traj.pkl"), "rb") as f:
        state_traj = pickle.load(f)
    with open(os.path.join(saving_directory, f"traj{index}", "obs_traj.pkl"), "rb") as f:
        obs_traj = pickle.load(f)
    with open(os.path.join(saving_directory, f"traj{index}", "action_traj.pkl"), "rb") as f:
        act_traj = pickle.load(f)

    action_traj = np.array(act_traj)
    action_blocked = state_traj["action_blocked"]
    starting_state = np.array(state_traj["joints"][0])
    env.play_teleop_trajectory(action_traj, action_blocked, starting_state)

if __name__=="__main__":
    main()