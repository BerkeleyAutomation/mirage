#############################################################################################################################
#############################################################################################################################
# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50000 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_source_iiwa_0.04_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50000 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_target_IIWA_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50001 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_source_iiwa_0.03_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50001 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_target_IIWA_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50002 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_source_iiwa_0.02_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50002 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_target_IIWA_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50003 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_source_iiwa_0.015_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50003 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_target_IIWA_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50004 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_source_iiwa_0.007_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50004 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_target_IIWA_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50005 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_source_iiwa_0.003_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50005 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_target_IIWA_0.003_300.txt --tracking_error_threshold 0.003 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50006 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_source_iiwa_0.001_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50006 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_ph_target_IIWA_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name IIWA --passive

#############################################################################################################################
#############################################################################################################################
# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50007 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_source_iiwa_0.04_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50007 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_target_IIWA_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50008 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_source_iiwa_0.03_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50008 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_target_IIWA_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50009 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_source_iiwa_0.02_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50009 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_target_IIWA_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50010 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_source_iiwa_0.015_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50010 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_target_IIWA_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50011 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_source_iiwa_0.007_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50011 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_target_IIWA_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50012 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_source_iiwa_0.003_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50012 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_target_IIWA_0.003_300.txt --tracking_error_threshold 0.003 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50013 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_source_iiwa_0.001_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 50013 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/iiwa/lift_mh_target_IIWA_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name IIWA --passive

