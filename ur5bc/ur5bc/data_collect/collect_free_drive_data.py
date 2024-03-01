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


def main():
    env = RobotEnv()
    index = 246
    # task_string = "Take the tiger out of the red bowl and put it in the grey bowl." # tiger pick and place
    # task_string = "Sweep the green cloth to the left side of the table." # cloth sweeping
    task_string = "Put the ranch bottle into the pot." # bottle pick and place
    # task_string = "Pick up the blue cup and put it into the brown cup. " # cup stacking
    saving_directory = "/home/lawrence/robotlerf/ur5bc/data/raw/teleop"
    while True:
        print("Starting index {}".format(index))
        # Ask the user whether to continue or not
        if input("Continue? (y/n): ") == "n":
            break

        env.reset(randomize=False, noise_type="joint")
        # action_traj, state_traj, obs_traj = env.record_free_drive_trajectory(traj_index=index, saving_directory=saving_directory)
        standard_output, action_traj, state_traj, obs_traj = env.record_teleop_trajectory(task_string, traj_index=index, saving_directory=saving_directory)
        print("Saving Trajectory ...")
        os.makedirs(os.path.join(saving_directory, f"traj{index}"), exist_ok=True)
        # save standard_output as a pkl file
        with open(os.path.join(saving_directory, f"traj{index}", "standard_output.pkl"), "wb") as f:
            pickle.dump(standard_output, f)
        # save action_traj as a pkl file
        with open(os.path.join(saving_directory, f"traj{index}", "action_traj.pkl"), "wb") as f:
            pickle.dump(action_traj, f)
        # save state_traj as a pkl file
        with open(os.path.join(saving_directory, f"traj{index}", "state_traj.pkl"), "wb") as f:
            pickle.dump(state_traj, f)
        # save obs_traj as a pkl file
        with open(os.path.join(saving_directory, f"traj{index}", "obs_traj.pkl"), "wb") as f:
            pickle.dump(obs_traj, f)
        # save the images
        # os.makedirs(os.path.join(saving_directory, f"traj{index}", "images"), exist_ok=True)
        # for i in range(len(obs_traj["hand_image"])):
        #     cv2.imwrite(os.path.join(saving_directory, f"traj{index}", "images", f"hand_img_{i}.jpg"), obs_traj["hand_image"][i])
        # for i in range(len(obs_traj["third_person_image"])):
        #     Image.fromarray(obs_traj["third_person_image"][i][0]).save(os.path.join(saving_directory, f"traj{index}", "images", f"third_person_img_{i}.jpg"))
        index += 1
    
    # load the data
    # with open(os.path.join(saving_directory, "traj0", "state_traj.pkl"), "rb") as f:
    #     state_traj = pickle.load(f)
    # with open(os.path.join(saving_directory, "traj0", "obs_traj.pkl"), "rb") as f:
    #     obs_traj = pickle.load(f)

if __name__=="__main__":
    main()