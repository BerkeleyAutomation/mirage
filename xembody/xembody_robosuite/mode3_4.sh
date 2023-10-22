# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10150 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/sawyer/tool_hang_ph_source_sawyer_1_absolute.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10150 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/sawyer/tool_hang_ph_target_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10151 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/ur5e/tool_hang_ph_source_ur5e_1_absolute.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10151 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/ur5e/tool_hang_ph_target_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10152 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/kinova3/tool_hang_ph_source_kinova3_1_absolute.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10152 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/kinova3/tool_hang_ph_target_kinova3_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10153 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/jaco/tool_hang_ph_source_jaco_1_absolute.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10153 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/jaco/tool_hang_ph_target_jaco_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10154 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/iiwa/tool_hang_ph_source_iiwa_1_absolute.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10154 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/iiwa/tool_hang_ph_target_iiwa_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10155 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_ph_source_sawyer_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10155 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_ph_target_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10156 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_ph_source_ur5e_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10156 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_ph_target_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10157 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_ph_source_kinova3_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10157 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_ph_target_kinova3_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10158 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_ph_source_jaco_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10158 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_ph_target_jaco_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10159 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_ph_source_iiwa_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10159 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_ph_target_iiwa_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10160 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_mh_source_sawyer_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10160 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_mh_target_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10161 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_mh_source_ur5e_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10161 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_mh_target_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10162 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_mh_source_kinova3_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10162 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_mh_target_kinova3_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10163 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_mh_source_jaco_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10163 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_mh_target_jaco_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10164 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_mh_source_iiwa_1_absolute.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10164 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_mh_target_iiwa_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive

