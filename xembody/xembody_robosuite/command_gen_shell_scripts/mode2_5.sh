# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30400 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_lowdim_source_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30400 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_lowdim_target_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --delta_action


# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30401 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_lowdim_source_jaco_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30401 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_lowdim_target_jaco_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco


# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30402 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_lowdim_source_jaco_0.04_300.txt --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30402 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_lowdim_target_jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30403 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_lowdim_source_jaco_0.03_300.txt --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30403 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_lowdim_target_jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30404 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_lowdim_source_jaco_0.02_300.txt --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30404 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_lowdim_target_jaco_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Jaco

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30405 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_lowdim_source_jaco_0.01_300.txt --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30405 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_lowdim_target_jaco_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Jaco

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30406 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_highdim_source_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30406 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_highdim_target_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30407 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_highdim_source_jaco_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30407 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_highdim_target_jaco_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30408 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_highdim_source_jaco_0.04_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30408 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_highdim_target_jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30409 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_highdim_source_jaco_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30409 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_highdim_target_jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30410 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_highdim_source_jaco_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30410 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_highdim_target_jaco_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Jaco

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30411 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_highdim_source_jaco_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30411 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/jaco/can_highdim_target_jaco_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Jaco

