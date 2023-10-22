#############################################################################################################################
#############################################################################################################################
# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20000 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_source_ur5e_0.04_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20000 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_target_UR5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20001 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_source_ur5e_0.03_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20001 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_target_UR5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20002 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_source_ur5e_0.02_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20002 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_target_UR5e_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20003 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_source_ur5e_0.015_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20003 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_target_UR5e_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20004 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_source_ur5e_0.007_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20004 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_target_UR5e_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20005 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_source_ur5e_0.003_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20005 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_target_UR5e_0.003_300.txt --tracking_error_threshold 0.003 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20006 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_source_ur5e_0.001_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20006 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/ph/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_ph_target_UR5e_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name UR5e --passive

#############################################################################################################################
#############################################################################################################################
# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20007 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_source_ur5e_0.04_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20007 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_target_UR5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20008 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_source_ur5e_0.03_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20008 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_target_UR5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20009 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_source_ur5e_0.02_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20009 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_target_UR5e_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20010 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_source_ur5e_0.015_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20010 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_target_UR5e_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20011 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_source_ur5e_0.007_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20011 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_target_UR5e_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20012 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_source_ur5e_0.003_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20012 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_target_UR5e_0.003_300.txt --tracking_error_threshold 0.003 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_demo_source_robot_server.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20013 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_source_ur5e_0.001_300.txt &
# target
python evaluate_demo_target_robot_client.py --n_rollouts 300 --horizon 400 --seeds 0 --connection --port 20013 --demo_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/demo_data_analysis/lift/ur5e/lift_mh_target_UR5e_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name UR5e --passive

