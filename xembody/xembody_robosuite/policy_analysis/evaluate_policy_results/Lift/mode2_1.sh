################################################################################################################################################
################################################################################################################################################
# lift low dim
# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50017 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_panda_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50017 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_panda_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Panda

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50017 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_sawyer_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50017 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_sawyer_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50018 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_ur5e_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50018 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_ur5e_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50019 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_kinova3_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50019 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_kinova3_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50020 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_jaco_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50020 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_jaco_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Jaco

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50021 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_iiwa_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50021 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_iiwa_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name IIWA

################################################################################################################################################
# lift high dim

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50017 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_source_sawyer_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50017 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_target_sawyer_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50018 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_source_ur5e_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50018 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_target_ur5e_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50019 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_source_kinova3_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50019 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_target_kinova3_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50020 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_source_jaco_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50020 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_target_jaco_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Jaco

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50021 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_source_iiwa_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50021 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_target_iiwa_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name IIWA

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50016 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_source_panda_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50016 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_target_panda_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Panda


################################################################################################################################################
################################################################################################################################################

################################################################################################################################################
################################################################################################################################################
# lift low dim
# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50016 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_panda_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50016 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_panda_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name Panda 

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50017 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_sawyer_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50017 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_sawyer_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50018 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_ur5e_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50018 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_ur5e_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50019 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_kinova3_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50019 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_kinova3_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50020 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_jaco_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50020 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_jaco_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name Jaco

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50021 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_iiwa_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50021 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_iiwa_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name IIWA

################################################################################################################################################
# lift high dim
# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50016 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_source_panda_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50016 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_target_panda_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name Panda

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50017 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_source_sawyer_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50017 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_target_sawyer_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50018 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_source_ur5e_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50018 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_target_ur5e_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50019 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_source_kinova3_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50019 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_target_kinova3_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50020 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_source_jaco_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50020 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_target_jaco_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name Jaco

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50021 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_source_iiwa_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50021 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_highdim_target_iiwa_0.007_300.txt --tracking_error_threshold 0.007 --num_iter_max 300 --robot_name IIWA


################################################################################################################################################
################################################################################################################################################
