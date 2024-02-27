import itertools
import subprocess
from typing import List
from concurrent.futures import ThreadPoolExecutor
import threading
import socket
import concurrent
import time
import os

SERVER_EXECUTABLE_PATH = "/home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_analysis/../evaluate_policy_demo_source_robot_server.py" 
CLIENT_EXECUTABLE_PATH = "/home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_analysis/../evaluate_policy_demo_target_robot_client.py"
TRAJECTORY_PAIR_RESULT_DIR = "/home/kdharmarajan/x-embody/xembody/xembody_robosuite/paired_trajectories_collection/results"
TIME = time.strftime("%Y%m%d%H%M%S")

port_lock = threading.Lock()

def collect_paired_trajectory(source_robot: str, target_robot: str, task: str):
    """
    Launches server / client setup to generate paired trajectories
    """
    port_lock.acquire()
    sock = socket.socket()
    sock.bind(('', 0))
    chosen_port = sock.getsockname()[1]
    sock.close()

    task_start_index = task.find("core/") + len("core/")
    task_name = task[task_start_index: task.find("/", task_start_index)]
    server_dataset_path = os.path.join(TRAJECTORY_PAIR_RESULT_DIR, TIME, f"{source_robot}_{target_robot}_{task_name}_source.hdf5")
    client_dataset_path = os.path.join(TRAJECTORY_PAIR_RESULT_DIR, TIME, f"{source_robot}_{target_robot}_{task_name}_client.hdf5")

    device = "cuda:2"

    server_args = ["python3", SERVER_EXECUTABLE_PATH, "--agent", task, "--n_rollouts", 10, "--seeds", 0, "--connection", "--port", chosen_port, "--tracking_error_threshold", 0.015, "--num_iter_max", 400, "--passive", "--robot_name", source_robot, "--dataset_path", server_dataset_path, "--device", device, "--dataset_obs", "--save_failed_demos"]
    client_args = ["python3", CLIENT_EXECUTABLE_PATH, "--agent", task, "--n_rollouts", 10, "--seeds", 0, "--connection", "--port", chosen_port, "--tracking_error_threshold", 0.015, "--num_iter_max", 400, "--robot_name", target_robot, "--dataset_path", client_dataset_path, "--device", device, "--dataset_obs", "--save_failed_demos"]

    server_args = list(map(str, server_args))
    client_args = list(map(str, client_args))
    print(" ".join(server_args) + " & " + " ".join(client_args))

    server = subprocess.Popen(server_args)
    client = subprocess.Popen(client_args)
    port_lock.release()
    
    server.wait()
    client.wait()
    return True
    
def compute_pairs_and_execute_trajectories(max_processes: int, source_robots: List[str], target_robots: List[str], tasks: List[str]):
    """
    Computes all pairs of robots and tasks and executes the paired trajectories
    """
    source_target_tasks_tuple = list(itertools.product(source_robots, target_robots, tasks))
    jobs = []
    with ThreadPoolExecutor() as executor:
        for source_robot, target_robot, task in source_target_tasks_tuple:
            jobs.append(executor.submit(collect_paired_trajectory, source_robot, target_robot, task))
        for no, future in enumerate(concurrent.futures.as_completed(jobs)):
            print("Result: {}".format(future.result()))
            print("Finished task {}".format(no))

if __name__ == "__main__":
    max_processes = 20
    source_robots = ["Panda"]
    robots = ["Panda", "UR5e", "Sawyer", "Kinova3", "Jaco", "IIWA"]

    # Create the appropriate folder
    os.makedirs(os.path.join(TRAJECTORY_PAIR_RESULT_DIR, TIME), exist_ok=True)

    # TODO: Generalize
    tasks = [
        "/home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/stack_d0/image/trained_models/core_stack_d0_image/20240108080130/models/model_epoch_540.pth",
        "/home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/stack_three_d0/low_dim/trained_models/core_stack_three_d0_low_dim/20240108083606/models/model_epoch_1900.pth",
        "/home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/coffee_d0/low_dim/trained_models/core_coffee_d0_low_dim/20240108082741/models/model_epoch_900_Coffee_D0_success_0.98.pth",
        "/home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/threading_d0/low_dim/trained_models/core_threading_d0_low_dim/20240108083807/models/model_epoch_550_Threading_D0_success_0.98.pth",
        "/home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/three_piece_assembly_d0/low_dim/trained_models/core_three_piece_assembly_d0_low_dim/20240108083905/models/model_epoch_2000.pth",
        "/home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/square_d0/low_dim/trained_models/core_square_d0_low_dim/20240108083408/models/model_epoch_2000.pth"
        ]
    compute_pairs_and_execute_trajectories(max_processes, source_robots, robots, tasks)