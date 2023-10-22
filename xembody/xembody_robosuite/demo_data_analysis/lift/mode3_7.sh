# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61000 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_source_sawyer_1_delta.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61000 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive --delta_action

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61001 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_source_sawyer_1_delta.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61001 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --passive --delta_action

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61002 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_source_ur5e_1_delta.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61002 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive --delta_action

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61003 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_source_ur5e_1_delta.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61003 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --passive --delta_action

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61004 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/kinova3/lift_ph_source_kinova3_1_delta.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61004 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/kinova3/lift_ph_target_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive --delta_action

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61005 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/kinova3/lift_mh_source_kinova3_1_delta.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61005 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/kinova3/lift_mh_target_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --passive --delta_action

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61006 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_source_jaco_1_delta.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61006 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_target_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive --delta_action

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61007 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_source_jaco_1_delta.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61007 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_target_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --passive --delta_action

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61008 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_source_iiwa_1_delta.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61008 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_target_iiwa_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive --delta_action

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61009 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_source_iiwa_1_delta.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 61009 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_target_iiwa_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --passive --delta_action

