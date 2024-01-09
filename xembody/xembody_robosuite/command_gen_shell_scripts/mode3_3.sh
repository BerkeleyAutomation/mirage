# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10100 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_ph_source_sawyer_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10100 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_ph_target_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10101 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_ph_source_ur5e_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10101 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_ph_target_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10102 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_ph_source_kinova3_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10102 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_ph_target_kinova3_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10103 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_ph_source_jaco_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10103 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_ph_target_jaco_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10104 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_ph_source_iiwa_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10104 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_ph_target_iiwa_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10105 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_mh_source_sawyer_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10105 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_mh_target_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10106 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_mh_source_ur5e_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10106 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_mh_target_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10107 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_mh_source_kinova3_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10107 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_mh_target_kinova3_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10108 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_mh_source_jaco_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10108 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_mh_target_jaco_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10109 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_mh_source_iiwa_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10109 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_mh_target_iiwa_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10110 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_ph_source_sawyer_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10110 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_ph_target_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10111 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_ph_source_ur5e_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10111 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_ph_target_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10112 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_ph_source_kinova3_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10112 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_ph_target_kinova3_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10113 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_ph_source_jaco_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10113 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_ph_target_jaco_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10114 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_ph_source_iiwa_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10114 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_ph_target_iiwa_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10115 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_mh_source_sawyer_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10115 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_mh_target_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10116 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_mh_source_ur5e_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10116 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_mh_target_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10117 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_mh_source_kinova3_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10117 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_mh_target_kinova3_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10118 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_mh_source_jaco_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10118 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_mh_target_jaco_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10119 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_mh_source_iiwa_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10119 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_mh_target_iiwa_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive

