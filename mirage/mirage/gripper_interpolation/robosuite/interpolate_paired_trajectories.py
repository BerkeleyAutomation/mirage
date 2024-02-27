import pickle
from sklearn.linear_model import LinearRegression
import numpy as np
import re
import os
import h5py
import argparse

def interpolate_paired_trajectories(source_gripper_joints, target_gripper_joints):
    """
    Interpolates the trajectories from the target back to source (i.e. UR5 to Panda)
    """
    model = LinearRegression()
    model = model.fit(target_gripper_joints, source_gripper_joints)
    return {
        "intercept": model.intercept_,
        "coef": model.coef_
    }

def interpolate_all_trajectories(paired_trajectory_folder: str, single_trajectory: bool = False):
    """
    Loops through all of the files and then interpolates the trajectories
    """
    interpolation_results = {}

    regex_pattern = re.compile(r"(?P<source>[a-zA-Z0-9]+)_(?P<target>[a-zA-Z0-9]+)_(?P<task>\w+)_source.hdf5")
    for file in os.listdir(paired_trajectory_folder):
        match = regex_pattern.match(file)
        if match:
            source_robot = match.group("source")
            target_robot = match.group("target")
            task = match.group("task")
            server_file_name = os.path.join(paired_trajectory_folder, file)
            client_file_name = os.path.join(paired_trajectory_folder, f"{source_robot}_{target_robot}_{task}_client.hdf5")

            try:
                server_file = h5py.File(server_file_name, "r")
                server_data = server_file["data"]
                server_demos = set(server_data.keys())
                source_gripper_joints = []

                client_file = h5py.File(client_file_name, "r")
                client_data = client_file["data"]
                client_demos = set(client_data.keys())
                target_gripper_joints = []
            except:
                continue

            demos = list(server_demos.intersection(client_demos))
            if len(demos) == 0:
                continue
                raise ValueError("No demos in common between server and client")

            inds = np.argsort([int(elem[5:]) for elem in demos])
            demos = [demos[i] for i in inds]

            for demo in demos:
                source_gripper_joints.append(server_data[demo]["obs"]["robot0_gripper_qpos"][()])
                target_gripper_joints.append(client_data[demo]["obs"]["robot0_gripper_qpos"][()])
                if single_trajectory:
                    break

            server_file.close()
            client_file.close()

            source_gripper_joints = np.vstack(source_gripper_joints)
            target_gripper_joints = np.vstack(target_gripper_joints)

            found_params = interpolate_paired_trajectories(source_gripper_joints, target_gripper_joints)
            # interpolation_results[(source_robot, target_robot, task)] = found_params
            interpolation_results[(source_robot, target_robot)] = found_params

    results_file = os.path.join("/home/kdharmarajan/x-embody/xembody/xembody_robosuite/paired_trajectories_collection", "gripper_interpolation_results_no_task_diff.pkl")
    with open(results_file, "wb") as f:
        pickle.dump(interpolation_results, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--single_trajectory", help="Use only a single trajectory when computing the interpolations", action="store_true")
    args = parser.parse_args()
    interpolate_all_trajectories("/home/kdharmarajan/x-embody/xembody/xembody_robosuite/paired_trajectories_collection/results/20240120013131", args.single_trajectory)