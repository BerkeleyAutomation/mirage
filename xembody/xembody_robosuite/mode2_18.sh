# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33100 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/jaco/transport_lowdim_source_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33100 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/jaco/transport_lowdim_target_jaco_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33101 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/jaco/transport_lowdim_source_jaco_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33101 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/jaco/transport_lowdim_target_jaco_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33102 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/jaco/transport_lowdim_source_jaco_0.04_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33102 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/jaco/transport_lowdim_target_jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33103 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/jaco/transport_lowdim_source_jaco_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33103 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/jaco/transport_lowdim_target_jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33104 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/jaco/transport_lowdim_source_jaco_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33104 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/jaco/transport_lowdim_target_jaco_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Jaco

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33105 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/jaco/transport_lowdim_source_jaco_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33105 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/jaco/transport_lowdim_target_jaco_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Jaco

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33106 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/iiwa/transport_lowdim_source_iiwa_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33106 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/iiwa/transport_lowdim_target_iiwa_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33107 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/iiwa/transport_lowdim_source_iiwa_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33107 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/iiwa/transport_lowdim_target_iiwa_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33108 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/iiwa/transport_lowdim_source_iiwa_0.04_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33108 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/iiwa/transport_lowdim_target_iiwa_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name IIWA

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33109 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/iiwa/transport_lowdim_source_iiwa_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33109 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/iiwa/transport_lowdim_target_iiwa_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name IIWA

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33110 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/iiwa/transport_lowdim_source_iiwa_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33110 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/iiwa/transport_lowdim_target_iiwa_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name IIWA

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33111 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/iiwa/transport_lowdim_source_iiwa_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 700 --seeds 0 --connection --port 33111 --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/transport/active_target/iiwa/transport_lowdim_target_iiwa_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name IIWA

