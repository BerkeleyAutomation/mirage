# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10300 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_ph_source_sawyer_0.03_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10300 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_ph_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10301 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_ph_source_ur5e_0.03_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10301 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_ph_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10302 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_ph_source_kinova3_0.03_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10302 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_ph_target_kinova3_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Kinova3 --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10303 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_ph_source_jaco_0.03_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10303 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_ph_target_jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10304 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_ph_source_iiwa_0.03_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10304 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_ph_target_iiwa_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name IIWA --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10305 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_mh_source_sawyer_0.03_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10305 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_mh_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10306 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_mh_source_ur5e_0.03_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10306 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_mh_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10307 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_mh_source_kinova3_0.03_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10307 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_mh_target_kinova3_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Kinova3 --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10308 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_mh_source_jaco_0.03_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10308 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_mh_target_jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10309 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_mh_source_iiwa_0.03_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10309 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_mh_target_iiwa_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name IIWA --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10310 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_ph_source_sawyer_0.03_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10310 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_ph_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10311 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_ph_source_ur5e_0.03_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10311 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_ph_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10312 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_ph_source_kinova3_0.03_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10312 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_ph_target_kinova3_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10313 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_ph_source_jaco_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10313 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_ph_target_jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10314 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_ph_source_iiwa_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10314 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_ph_target_iiwa_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10315 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_mh_source_sawyer_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10315 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_mh_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10316 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_mh_source_ur5e_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10316 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_mh_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10317 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_mh_source_kinova3_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10317 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_mh_target_kinova3_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10318 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_mh_source_jaco_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10318 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_mh_target_jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10319 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_mh_source_iiwa_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10319 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_mh_target_iiwa_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name IIWA --passive

