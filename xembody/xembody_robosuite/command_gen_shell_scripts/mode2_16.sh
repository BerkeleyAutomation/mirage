# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33000 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/panda/transport_lowdim_source_panda_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33000 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/panda/transport_lowdim_target_panda_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Panda --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33001 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/panda/transport_lowdim_source_panda_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33001 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/panda/transport_lowdim_target_panda_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Panda


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33002 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/panda/transport_lowdim_source_panda_0.04_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33002 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/panda/transport_lowdim_target_panda_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Panda

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33003 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/panda/transport_lowdim_source_panda_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33003 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/panda/transport_lowdim_target_panda_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Panda

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33004 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/panda/transport_lowdim_source_panda_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33004 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/panda/transport_lowdim_target_panda_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Panda

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33005 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/panda/transport_lowdim_source_panda_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33005 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/panda/transport_lowdim_target_panda_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Panda

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33006 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/sawyer/transport_lowdim_source_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33006 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/sawyer/transport_lowdim_target_sawyer_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33007 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/sawyer/transport_lowdim_source_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33007 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/sawyer/transport_lowdim_target_sawyer_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33008 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/sawyer/transport_lowdim_source_sawyer_0.04_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33008 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/sawyer/transport_lowdim_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33009 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/sawyer/transport_lowdim_source_sawyer_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33009 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/sawyer/transport_lowdim_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33010 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/sawyer/transport_lowdim_source_sawyer_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33010 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/sawyer/transport_lowdim_target_sawyer_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33011 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/sawyer/transport_lowdim_source_sawyer_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33011 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/sawyer/transport_lowdim_target_sawyer_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Sawyer

