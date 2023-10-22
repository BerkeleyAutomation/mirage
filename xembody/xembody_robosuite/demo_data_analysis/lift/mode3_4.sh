#############################################################################################################################
#############################################################################################################################
# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40000 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_source_jaco_0.04_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40000 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_target_Jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40001 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_source_jaco_0.03_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40001 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_target_Jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40002 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_source_jaco_0.02_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40002 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_target_Jaco_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40003 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_source_jaco_0.015_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40003 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_target_Jaco_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40004 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_source_jaco_0.007_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40004 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_target_Jaco_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40005 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_source_jaco_0.003_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40005 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_target_Jaco_0.003_300.txt --tracking_error_threshold 0.003 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40006 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_source_jaco_0.001_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40006 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_ph_target_Jaco_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name Jaco --passive

#############################################################################################################################
#############################################################################################################################
# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40007 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_source_jaco_0.04_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40007 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_target_Jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40008 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_source_jaco_0.03_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40008 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_target_Jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40009 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_source_jaco_0.02_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40009 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_target_Jaco_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40010 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_source_jaco_0.015_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40010 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_target_Jaco_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40011 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_source_jaco_0.007_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40011 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_target_Jaco_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40012 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_source_jaco_0.003_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40012 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_target_Jaco_0.003_300.txt --tracking_error_threshold 0.003 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40013 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_source_jaco_0.001_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 40013 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/jaco/lift_mh_target_Jaco_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name Jaco --passive

