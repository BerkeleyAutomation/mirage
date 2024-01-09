# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10200 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_ph_source_sawyer_0.04_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10200 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_ph_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10201 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_ph_source_ur5e_0.04_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10201 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_ph_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10202 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_ph_source_kinova3_0.04_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10202 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_ph_target_kinova3_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Kinova3 --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10203 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_ph_source_jaco_0.04_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10203 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_ph_target_jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10204 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_ph_source_iiwa_0.04_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10204 --demo_path /home/lawrence/xembody/robomimic/datasets/can/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_ph_target_iiwa_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name IIWA --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10205 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_mh_source_sawyer_0.04_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10205 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/sawyer/can_mh_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10206 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_mh_source_ur5e_0.04_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10206 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/ur5e/can_mh_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10207 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_mh_source_kinova3_0.04_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10207 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/kinova3/can_mh_target_kinova3_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Kinova3 --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10208 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_mh_source_jaco_0.04_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10208 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/jaco/can_mh_target_jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10209 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_mh_source_iiwa_0.04_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10209 --demo_path /home/lawrence/xembody/robomimic/datasets/can/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/can/iiwa/can_mh_target_iiwa_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name IIWA --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10210 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_ph_source_sawyer_0.04_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10210 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_ph_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10211 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_ph_source_ur5e_0.04_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10211 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_ph_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10212 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_ph_source_kinova3_0.04_300.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10212 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_ph_target_kinova3_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10213 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_ph_source_jaco_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10213 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_ph_target_jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10214 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_ph_source_iiwa_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10214 --demo_path /home/lawrence/xembody/robomimic/datasets/square/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_ph_target_iiwa_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10215 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_mh_source_sawyer_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10215 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/sawyer/square_mh_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10216 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_mh_source_ur5e_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10216 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/ur5e/square_mh_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10217 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_mh_source_kinova3_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10217 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/kinova3/square_mh_target_kinova3_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10218 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_mh_source_jaco_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10218 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/jaco/square_mh_target_jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10219 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_mh_source_iiwa_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10219 --demo_path /home/lawrence/xembody/robomimic/datasets/square/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/square/iiwa/square_mh_target_iiwa_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name IIWA --passive

