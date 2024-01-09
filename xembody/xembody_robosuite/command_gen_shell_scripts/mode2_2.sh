# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30100 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_lowdim_source_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30100 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_lowdim_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30101 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_lowdim_source_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30101 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_lowdim_target_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30102 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_lowdim_source_sawyer_0.04_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30102 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_lowdim_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30103 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_lowdim_source_sawyer_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30103 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_lowdim_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30104 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_lowdim_source_sawyer_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30104 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_lowdim_target_sawyer_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30105 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_lowdim_source_sawyer_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30105 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_lowdim_target_sawyer_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30106 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_highdim_source_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30106 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_highdim_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30107 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_highdim_source_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30107 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_highdim_target_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30108 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_highdim_source_sawyer_0.04_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30108 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_highdim_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30109 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_highdim_source_sawyer_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30109 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_highdim_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30110 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_highdim_source_sawyer_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30110 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_highdim_target_sawyer_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30111 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_highdim_source_sawyer_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30111 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/sawyer/can_highdim_target_sawyer_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Sawyer

