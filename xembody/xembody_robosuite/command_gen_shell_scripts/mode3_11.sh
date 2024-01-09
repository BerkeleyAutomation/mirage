# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10500 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_ph_source_sawyer_0.01_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10500 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_ph_target_sawyer_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Sawyer --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10501 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_ph_source_ur5e_0.01_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10501 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_ph_target_ur5e_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name UR5e --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10502 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_ph_source_kinova3_0.01_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10502 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_ph_target_kinova3_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Kinova3 --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10503 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_ph_source_jaco_0.01_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10503 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_ph_target_jaco_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Jaco --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10504 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_ph_source_iiwa_0.01_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10504 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_ph_target_iiwa_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name IIWA --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10505 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_mh_source_sawyer_0.01_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10505 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_mh_target_sawyer_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Sawyer --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10506 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_mh_source_ur5e_0.01_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10506 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_mh_target_ur5e_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name UR5e --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10507 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_mh_source_kinova3_0.01_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10507 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_mh_target_kinova3_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Kinova3 --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10508 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_mh_source_jaco_0.01_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10508 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_mh_target_jaco_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10509 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_mh_source_iiwa_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10509 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_mh_target_iiwa_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10510 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_ph_source_sawyer_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10510 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_ph_target_sawyer_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10511 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_ph_source_ur5e_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10511 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_ph_target_ur5e_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10512 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_ph_source_kinova3_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10512 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_ph_target_kinova3_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10513 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_ph_source_jaco_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10513 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_ph_target_jaco_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10514 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_ph_source_iiwa_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10514 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_ph_target_iiwa_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10515 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_mh_source_sawyer_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10515 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_mh_target_sawyer_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10516 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_mh_source_ur5e_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10516 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_mh_target_ur5e_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10517 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_mh_source_kinova3_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10517 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_mh_target_kinova3_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10518 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_mh_source_jaco_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10518 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_mh_target_jaco_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10519 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_mh_source_iiwa_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10519 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_mh_target_iiwa_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name IIWA --passive

