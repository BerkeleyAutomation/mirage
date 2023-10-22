# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --port 10050 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/panda/tool_hang_ph_source_panda.txt
# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10051 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/sawyer/tool_hang_ph_source_sawyer_1_delta.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10051 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/sawyer/tool_hang_ph_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive --delta_action

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10052 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/ur5e/tool_hang_ph_source_ur5e_1_delta.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10052 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/ur5e/tool_hang_ph_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive --delta_action

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10053 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/kinova3/tool_hang_ph_source_kinova3_1_delta.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10053 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/kinova3/tool_hang_ph_target_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive --delta_action

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10054 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/jaco/tool_hang_ph_source_jaco_1_delta.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10054 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/jaco/tool_hang_ph_target_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive --delta_action

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10055 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/iiwa/tool_hang_ph_source_iiwa_1_delta.txt &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10055 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/iiwa/tool_hang_ph_target_iiwa_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive --delta_action

# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --port 10056 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/panda/transport_ph_source_panda.txt
# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10057 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_ph_source_sawyer_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10057 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_ph_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10058 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_ph_source_ur5e_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10058 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_ph_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10059 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_ph_source_kinova3_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10059 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_ph_target_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10060 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_ph_source_jaco_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10060 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_ph_target_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10061 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_ph_source_iiwa_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10061 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_ph_target_iiwa_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive --delta_action

# python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --port 10062 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/panda/transport_mh_source_panda.txt
# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10063 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_mh_source_sawyer_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10063 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_mh_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10064 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_mh_source_ur5e_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10064 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_mh_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10065 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_mh_source_kinova3_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10065 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_mh_target_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10066 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_mh_source_jaco_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10066 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_mh_target_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive --delta_action

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10067 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_mh_source_iiwa_1_delta.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10067 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_mh_target_iiwa_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive --delta_action

