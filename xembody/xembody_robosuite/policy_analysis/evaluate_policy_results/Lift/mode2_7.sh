
################################################################################################################################################
################################################################################################################################################
# lift low dim
# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50066 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_panda_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50066 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_panda_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Panda --delta_action 

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50067 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50067 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --delta_action 

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50068 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50068 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --delta_action 

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50069 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50069 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --delta_action 

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50070 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50070 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --delta_action 

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50071 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_source_iiwa_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50071 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/lift_lowdim_target_iiwa_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --delta_action 

