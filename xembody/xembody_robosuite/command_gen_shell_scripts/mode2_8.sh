# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31100 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_lowdim_source_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31100 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_lowdim_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --delta_action


# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31101 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_lowdim_source_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31101 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_lowdim_target_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer


# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31102 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_lowdim_source_sawyer_0.04_300.txt --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31102 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_lowdim_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31103 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_lowdim_source_sawyer_0.03_300.txt --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31103 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_lowdim_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31104 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_lowdim_source_sawyer_0.02_300.txt --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31104 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_lowdim_target_sawyer_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Sawyer

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31105 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_lowdim_source_sawyer_0.01_300.txt --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31105 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_lowdim_target_sawyer_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31106 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_highdim_source_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31106 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_highdim_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31107 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_highdim_source_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31107 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_highdim_target_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31108 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_highdim_source_sawyer_0.04_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31108 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_highdim_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31109 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_highdim_source_sawyer_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31109 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_highdim_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31110 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_highdim_source_sawyer_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31110 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_highdim_target_sawyer_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31111 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_highdim_source_sawyer_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31111 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/sawyer/square_highdim_target_sawyer_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Sawyer

