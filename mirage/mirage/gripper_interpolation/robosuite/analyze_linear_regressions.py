import os
import pickle

if __name__ == '__main__':
    results_file = os.path.join("/home/kdharmarajan/x-embody/xembody/xembody_robosuite/paired_trajectories_collection", "gripper_interpolation_results_20_rollouts.pkl")
    with open(results_file, "rb") as f:
        regression_values = pickle.load(f)

    for key, value in regression_values.items():
        print(f"{key}: {value}")