from subprocess import Popen
from datetime import datetime
import numpy as np

curr_time = datetime.now()

NUM_EXPERIMENTS = 1
for i in range(0, NUM_EXPERIMENTS):
    seed = np.random.randint(0, 100000)
    save_dir = f'/home/lawrence/xembody/xembody/orbit_collected_data_orbit/{curr_time}/{i}'
    start_robot_process = Popen(['python3', 
                                '/home/lawrence/xembody/xembody/demo_control_source_target/demo_control_orbit_policy_execute.py', 
                                '--robot_type', 'franka_panda', 
                                '--task', 'Isaac-Lift-Franka-v0', 
                                '--num_envs', '1', 
                                '--data_save_dir', save_dir,
                                '--seed', str(seed)])
    start_robot_process.wait()

    replay_robot_process = Popen(['python3', 
                                '/home/lawrence/xembody/xembody/demo_control_source_target/demo_control_orbit_policy_execute.py', 
                                '--robot_type', 'ur5', 
                                '--task', 'Isaac-Lift-Franka-v0', 
                                '--num_envs', '1', 
                                '--data_save_dir', save_dir,
                                '--is_replay_robot',
                                '--seed', str(seed)])
    replay_robot_process.wait()