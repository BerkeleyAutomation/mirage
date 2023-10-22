from subprocess import Popen
from datetime import datetime

curr_time = datetime.now()
save_dir = f'/home/lawrence/xembody/RLBench/collected_data_orbit/{curr_time}'

start_robot_process = Popen(['python3', 
                             '/home/lawrence/xembody/xembody/demo_control_orbit_policy_execute.py', 
                             '--robot_type', 'franka_panda', 
                             '--task', 'Isaac-Lift-Franka-v0', 
                             '--num_envs', '1', 
                             '--data_save_dir', save_dir])
start_robot_process.wait()

replay_robot_process = Popen(['python3', 
                             '/home/lawrence/xembody/xembody/demo_control_orbit_policy_execute.py', 
                             '--robot_type', 'ur5', 
                             '--task', 'Isaac-Lift-Franka-v0', 
                             '--num_envs', '1', 
                             '--data_save_dir', save_dir,
                             '--is_replay_robot'])
replay_robot_process.wait()