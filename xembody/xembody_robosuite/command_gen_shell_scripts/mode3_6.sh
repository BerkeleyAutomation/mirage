# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10250 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/sawyer/tool_hang_ph_source_sawyer_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10250 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/sawyer/tool_hang_ph_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10251 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/ur5e/tool_hang_ph_source_ur5e_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10251 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/ur5e/tool_hang_ph_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10252 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/kinova3/tool_hang_ph_source_kinova3_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10252 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/kinova3/tool_hang_ph_target_kinova3_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10253 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/jaco/tool_hang_ph_source_jaco_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10253 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/jaco/tool_hang_ph_target_jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10254 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/iiwa/tool_hang_ph_source_iiwa_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10254 --demo_path /home/lawrence/xembody/robomimic/datasets/tool_hang/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/tool_hang/iiwa/tool_hang_ph_target_iiwa_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10255 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_ph_source_sawyer_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10255 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_ph_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10256 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_ph_source_ur5e_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10256 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_ph_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10257 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_ph_source_kinova3_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10257 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_ph_target_kinova3_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10258 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_ph_source_jaco_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10258 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_ph_target_jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10259 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_ph_source_iiwa_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10259 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_ph_target_iiwa_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10260 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_mh_source_sawyer_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10260 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/sawyer/transport_mh_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10261 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_mh_source_ur5e_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10261 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/ur5e/transport_mh_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10262 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_mh_source_kinova3_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10262 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/kinova3/transport_mh_target_kinova3_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10263 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_mh_source_jaco_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10263 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/jaco/transport_mh_target_jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10264 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_mh_source_iiwa_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 300 --horizon 700 --seeds 0 --connection --port 10264 --demo_path /home/lawrence/xembody/robomimic/datasets/transport/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/transport/iiwa/transport_mh_target_iiwa_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name IIWA --passive

