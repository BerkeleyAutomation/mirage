# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32100 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/ur5e/tool_hang_lowdim_source_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32100 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/ur5e/tool_hang_lowdim_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --delta_action


# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32101 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/ur5e/tool_hang_lowdim_source_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32101 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/ur5e/tool_hang_lowdim_target_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e


# # source
# python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32102 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/ur5e/tool_hang_lowdim_source_ur5e_0.04_300.txt --passive &
# # target
# python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32102 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/ur5e/tool_hang_lowdim_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32103 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/ur5e/tool_hang_lowdim_source_ur5e_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32103 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/ur5e/tool_hang_lowdim_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32104 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/ur5e/tool_hang_lowdim_source_ur5e_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32104 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/ur5e/tool_hang_lowdim_target_ur5e_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name UR5e


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32106 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/kinova3/tool_hang_lowdim_source_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32106 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/kinova3/tool_hang_lowdim_target_kinova3_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32107 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/kinova3/tool_hang_lowdim_source_kinova3_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32107 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/kinova3/tool_hang_lowdim_target_kinova3_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32108 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/kinova3/tool_hang_lowdim_source_kinova3_0.04_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32108 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/kinova3/tool_hang_lowdim_target_kinova3_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32109 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/kinova3/tool_hang_lowdim_source_kinova3_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32109 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/kinova3/tool_hang_lowdim_target_kinova3_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32110 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/kinova3/tool_hang_lowdim_source_kinova3_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32110 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/kinova3/tool_hang_lowdim_target_kinova3_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32111 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/kinova3/tool_hang_lowdim_source_kinova3_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32111 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/kinova3/tool_hang_lowdim_target_kinova3_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32105 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/ur5e/tool_hang_lowdim_source_ur5e_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 32105 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/active_target/ur5e/tool_hang_lowdim_target_ur5e_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name UR5e
