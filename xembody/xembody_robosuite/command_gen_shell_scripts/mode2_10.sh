# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31300 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_lowdim_source_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31300 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_lowdim_target_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31301 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_lowdim_source_kinova3_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31301 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_lowdim_target_kinova3_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31302 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_lowdim_source_kinova3_0.04_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31302 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_lowdim_target_kinova3_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31303 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_lowdim_source_kinova3_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31303 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_lowdim_target_kinova3_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31304 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_lowdim_source_kinova3_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31304 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_lowdim_target_kinova3_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31305 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_lowdim_source_kinova3_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31305 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_lowdim_target_kinova3_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31306 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_highdim_source_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31306 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_highdim_target_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31307 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_highdim_source_kinova3_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31307 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_highdim_target_kinova3_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31308 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_highdim_source_kinova3_0.04_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31308 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_highdim_target_kinova3_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31309 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_highdim_source_kinova3_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31309 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_highdim_target_kinova3_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31310 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_highdim_source_kinova3_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31310 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_highdim_target_kinova3_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31311 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_highdim_source_kinova3_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31311 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/kinova3/square_highdim_target_kinova3_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Kinova3

