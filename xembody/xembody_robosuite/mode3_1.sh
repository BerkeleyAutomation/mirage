python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --port 10000 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/panda/can_ph_source_panda.txt
# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10001 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_ph_source_sawyer_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10001 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_ph_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10002 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_ph_source_ur5e_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10002 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_ph_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10003 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_ph_source_kinova3_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10003 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_ph_target_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10004 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_ph_source_jaco_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10004 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_ph_target_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10005 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_ph_source_iiwa_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10005 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_ph_target_iiwa_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive --delta_action

python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --port 10006 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/panda/can_mh_source_panda.txt
# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10007 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_mh_source_sawyer_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10007 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_mh_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10008 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_mh_source_ur5e_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10008 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_mh_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10009 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_mh_source_kinova3_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10009 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_mh_target_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10010 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_mh_source_jaco_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10010 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_mh_target_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10011 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_mh_source_iiwa_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10011 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_mh_target_iiwa_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive --delta_action

python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --port 10012 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/panda/square_ph_source_panda.txt
# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10013 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_ph_source_sawyer_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10013 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_ph_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10014 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_ph_source_ur5e_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10014 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_ph_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10015 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_ph_source_kinova3_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10015 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_ph_target_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10016 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_ph_source_jaco_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10016 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_ph_target_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10017 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_ph_source_iiwa_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10017 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_ph_target_iiwa_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive --delta_action

python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --port 10018 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/panda/square_mh_source_panda.txt
# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10019 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_mh_source_sawyer_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10019 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_mh_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10020 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_mh_source_ur5e_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10020 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_mh_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10021 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_mh_source_kinova3_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10021 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_mh_target_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10022 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_mh_source_jaco_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10022 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_mh_target_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10023 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_mh_source_iiwa_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10023 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_mh_target_iiwa_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive --delta_action

