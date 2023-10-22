# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10350 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/sawyer/tool_hang_ph_source_sawyer_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10350 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/sawyer/tool_hang_ph_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10351 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/ur5e/tool_hang_ph_source_ur5e_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10351 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/ur5e/tool_hang_ph_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10352 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/kinova3/tool_hang_ph_source_kinova3_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10352 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/kinova3/tool_hang_ph_target_kinova3_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10353 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/jaco/tool_hang_ph_source_jaco_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10353 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/jaco/tool_hang_ph_target_jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10354 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/iiwa/tool_hang_ph_source_iiwa_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10354 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/iiwa/tool_hang_ph_target_iiwa_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10355 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_ph_source_sawyer_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10355 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_ph_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10356 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_ph_source_ur5e_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10356 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_ph_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10357 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_ph_source_kinova3_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10357 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_ph_target_kinova3_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10358 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_ph_source_jaco_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10358 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_ph_target_jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10359 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_ph_source_iiwa_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10359 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_ph_target_iiwa_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10360 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_mh_source_sawyer_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10360 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_mh_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10361 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_mh_source_ur5e_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10361 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_mh_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10362 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_mh_source_kinova3_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10362 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_mh_target_kinova3_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10363 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_mh_source_jaco_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10363 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_mh_target_jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10364 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_mh_source_iiwa_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10364 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_mh_target_iiwa_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name IIWA --passive

