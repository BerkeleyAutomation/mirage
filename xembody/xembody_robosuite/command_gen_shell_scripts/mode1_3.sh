# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20400 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/sawyer/tool_hang_lowdim_source_sawyer_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20400 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/sawyer/tool_hang_lowdim_target_sawyer_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Sawyer --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20401 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/sawyer/tool_hang_lowdim_source_sawyer_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20401 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/sawyer/tool_hang_lowdim_target_sawyer_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Sawyer --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20402 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/sawyer/tool_hang_lowdim_source_sawyer_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20402 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/sawyer/tool_hang_lowdim_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20403 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/sawyer/tool_hang_lowdim_source_sawyer_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20403 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/sawyer/tool_hang_lowdim_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20404 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/sawyer/tool_hang_lowdim_source_sawyer_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20404 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/sawyer/tool_hang_lowdim_target_sawyer_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20405 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/sawyer/tool_hang_lowdim_source_sawyer_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20405 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/sawyer/tool_hang_lowdim_target_sawyer_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20406 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/ur5e/tool_hang_lowdim_source_ur5e_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20406 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/ur5e/tool_hang_lowdim_target_ur5e_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name UR5e --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20407 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/ur5e/tool_hang_lowdim_source_ur5e_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20407 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/ur5e/tool_hang_lowdim_target_ur5e_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name UR5e --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20408 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/ur5e/tool_hang_lowdim_source_ur5e_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20408 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/ur5e/tool_hang_lowdim_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20409 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/ur5e/tool_hang_lowdim_source_ur5e_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20409 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/ur5e/tool_hang_lowdim_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20410 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/ur5e/tool_hang_lowdim_source_ur5e_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20410 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/ur5e/tool_hang_lowdim_target_ur5e_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20411 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/ur5e/tool_hang_lowdim_source_ur5e_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20411 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/ur5e/tool_hang_lowdim_target_ur5e_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20412 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/kinova3/tool_hang_lowdim_source_kinova3_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20412 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/kinova3/tool_hang_lowdim_target_kinova3_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Kinova3 --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20413 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/kinova3/tool_hang_lowdim_source_kinova3_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20413 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/kinova3/tool_hang_lowdim_target_kinova3_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Kinova3 --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20414 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/kinova3/tool_hang_lowdim_source_kinova3_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20414 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/kinova3/tool_hang_lowdim_target_kinova3_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20415 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/kinova3/tool_hang_lowdim_source_kinova3_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20415 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/kinova3/tool_hang_lowdim_target_kinova3_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20416 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/kinova3/tool_hang_lowdim_source_kinova3_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20416 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/kinova3/tool_hang_lowdim_target_kinova3_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20417 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/kinova3/tool_hang_lowdim_source_kinova3_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20417 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/kinova3/tool_hang_lowdim_target_kinova3_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20418 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/jaco/tool_hang_lowdim_source_jaco_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20418 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/jaco/tool_hang_lowdim_target_jaco_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Jaco --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20419 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/jaco/tool_hang_lowdim_source_jaco_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20419 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/jaco/tool_hang_lowdim_target_jaco_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Jaco --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20420 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/jaco/tool_hang_lowdim_source_jaco_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20420 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/jaco/tool_hang_lowdim_target_jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20421 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/jaco/tool_hang_lowdim_source_jaco_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20421 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/jaco/tool_hang_lowdim_target_jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20422 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/jaco/tool_hang_lowdim_source_jaco_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20422 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/jaco/tool_hang_lowdim_target_jaco_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20423 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/jaco/tool_hang_lowdim_source_jaco_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20423 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/jaco/tool_hang_lowdim_target_jaco_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20424 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/iiwa/tool_hang_lowdim_source_iiwa_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20424 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/iiwa/tool_hang_lowdim_target_iiwa_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name IIWA --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20425 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/iiwa/tool_hang_lowdim_source_iiwa_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20425 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/iiwa/tool_hang_lowdim_target_iiwa_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name IIWA --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20426 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/iiwa/tool_hang_lowdim_source_iiwa_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20426 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/iiwa/tool_hang_lowdim_target_iiwa_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20427 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/iiwa/tool_hang_lowdim_source_iiwa_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20427 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/iiwa/tool_hang_lowdim_target_iiwa_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20428 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/iiwa/tool_hang_lowdim_source_iiwa_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20428 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/iiwa/tool_hang_lowdim_target_iiwa_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20429 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/iiwa/tool_hang_lowdim_source_iiwa_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20429 --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/tool_hang/passive_target/iiwa/tool_hang_lowdim_target_iiwa_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20430 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/sawyer/transport_lowdim_source_sawyer_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20430 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/sawyer/transport_lowdim_target_sawyer_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Sawyer --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20431 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/sawyer/transport_lowdim_source_sawyer_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20431 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/sawyer/transport_lowdim_target_sawyer_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Sawyer --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20432 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/sawyer/transport_lowdim_source_sawyer_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20432 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/sawyer/transport_lowdim_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20433 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/sawyer/transport_lowdim_source_sawyer_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20433 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/sawyer/transport_lowdim_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20434 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/sawyer/transport_lowdim_source_sawyer_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20434 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/sawyer/transport_lowdim_target_sawyer_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20435 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/sawyer/transport_lowdim_source_sawyer_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20435 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/sawyer/transport_lowdim_target_sawyer_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20436 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/ur5e/transport_lowdim_source_ur5e_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20436 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/ur5e/transport_lowdim_target_ur5e_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name UR5e --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20437 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/ur5e/transport_lowdim_source_ur5e_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20437 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/ur5e/transport_lowdim_target_ur5e_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name UR5e --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20438 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/ur5e/transport_lowdim_source_ur5e_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20438 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/ur5e/transport_lowdim_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20439 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/ur5e/transport_lowdim_source_ur5e_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20439 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/ur5e/transport_lowdim_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20440 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/ur5e/transport_lowdim_source_ur5e_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20440 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/ur5e/transport_lowdim_target_ur5e_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20441 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/ur5e/transport_lowdim_source_ur5e_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20441 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/ur5e/transport_lowdim_target_ur5e_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20442 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/kinova3/transport_lowdim_source_kinova3_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20442 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/kinova3/transport_lowdim_target_kinova3_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Kinova3 --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20443 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/kinova3/transport_lowdim_source_kinova3_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20443 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/kinova3/transport_lowdim_target_kinova3_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Kinova3 --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20444 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/kinova3/transport_lowdim_source_kinova3_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20444 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/kinova3/transport_lowdim_target_kinova3_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20445 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/kinova3/transport_lowdim_source_kinova3_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20445 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/kinova3/transport_lowdim_target_kinova3_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20446 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/kinova3/transport_lowdim_source_kinova3_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20446 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/kinova3/transport_lowdim_target_kinova3_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20447 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/kinova3/transport_lowdim_source_kinova3_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20447 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/kinova3/transport_lowdim_target_kinova3_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20448 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/jaco/transport_lowdim_source_jaco_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20448 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/jaco/transport_lowdim_target_jaco_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Jaco --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20449 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/jaco/transport_lowdim_source_jaco_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20449 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/jaco/transport_lowdim_target_jaco_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Jaco --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20450 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/jaco/transport_lowdim_source_jaco_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20450 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/jaco/transport_lowdim_target_jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20451 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/jaco/transport_lowdim_source_jaco_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20451 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/jaco/transport_lowdim_target_jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20452 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/jaco/transport_lowdim_source_jaco_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20452 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/jaco/transport_lowdim_target_jaco_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20453 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/jaco/transport_lowdim_source_jaco_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20453 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/jaco/transport_lowdim_target_jaco_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20454 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/iiwa/transport_lowdim_source_iiwa_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20454 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/iiwa/transport_lowdim_target_iiwa_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name IIWA --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20455 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/iiwa/transport_lowdim_source_iiwa_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20455 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/iiwa/transport_lowdim_target_iiwa_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name IIWA --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20456 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/iiwa/transport_lowdim_source_iiwa_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20456 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/iiwa/transport_lowdim_target_iiwa_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20457 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/iiwa/transport_lowdim_source_iiwa_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20457 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/iiwa/transport_lowdim_target_iiwa_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20458 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/iiwa/transport_lowdim_source_iiwa_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20458 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/iiwa/transport_lowdim_target_iiwa_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20459 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/iiwa/transport_lowdim_source_iiwa_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 20459 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/passive_target/iiwa/transport_lowdim_target_iiwa_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name IIWA --passive

