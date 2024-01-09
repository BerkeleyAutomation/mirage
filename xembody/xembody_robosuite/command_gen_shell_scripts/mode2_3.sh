# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30200 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_lowdim_source_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30200 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_lowdim_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --delta_action


# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30201 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_lowdim_source_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30201 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_lowdim_target_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e


# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30202 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_lowdim_source_ur5e_0.04_300.txt --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30202 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_lowdim_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30203 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_lowdim_source_ur5e_0.03_300.txt --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30203 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_lowdim_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30204 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_lowdim_source_ur5e_0.02_300.txt --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30204 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_lowdim_target_ur5e_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name UR5e

# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30205 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_lowdim_source_ur5e_0.01_300.txt --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30205 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_lowdim_target_ur5e_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30206 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_highdim_source_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30206 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_highdim_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30207 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_highdim_source_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30207 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_highdim_target_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30208 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_highdim_source_ur5e_0.04_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30208 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_highdim_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30209 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_highdim_source_ur5e_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30209 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_highdim_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30210 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_highdim_source_ur5e_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30210 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_highdim_target_ur5e_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30211 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_highdim_source_ur5e_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 30211 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/active_target/ur5e/can_highdim_target_ur5e_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name UR5e

