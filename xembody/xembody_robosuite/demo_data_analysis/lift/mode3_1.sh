#############################################################################################################################
#############################################################################################################################
# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10000 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_source_sawyer_0.04_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10000 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_target_Sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10001 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_source_sawyer_0.03_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10001 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_target_Sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10002 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_source_sawyer_0.02_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10002 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_target_Sawyer_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10003 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_source_sawyer_0.015_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10003 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_target_Sawyer_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10004 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_source_sawyer_0.007_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10004 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_target_Sawyer_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10005 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_source_sawyer_0.003_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10005 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_target_Sawyer_0.003_300.txt --tracking_error_threshold 0.003 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10006 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_source_sawyer_0.001_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10006 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_ph_target_Sawyer_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name Sawyer --passive

#############################################################################################################################
#############################################################################################################################
# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10007 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_source_sawyer_0.04_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10007 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_target_Sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10008 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_source_sawyer_0.03_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10008 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_target_Sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10009 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_source_sawyer_0.02_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10009 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_target_Sawyer_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10010 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_source_sawyer_0.015_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10010 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_target_Sawyer_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10011 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_source_sawyer_0.007_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10011 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_target_Sawyer_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10012 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_source_sawyer_0.003_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10012 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_target_Sawyer_0.003_300.txt --tracking_error_threshold 0.003 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10013 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_source_sawyer_0.001_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 10013 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/sawyer/lift_mh_target_Sawyer_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name Sawyer --passive

