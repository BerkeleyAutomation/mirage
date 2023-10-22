
################################################################################################################################################
################################################################################################################################################
# lift low dim
# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50010 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_source_jaco_0.003_300.txt --tracking_error_threshold 0.003 --num_iter_max 300 &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50010 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_target_jaco_0.003_300.txt --tracking_error_threshold 0.003 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50040 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_source_jaco_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50040 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_target_jaco_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name Jaco --passive

################################################################################################################################################
################################################################################################################################################
# lift low dim
# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50006 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_source_panda_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50006 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_target_panda_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name Panda --passive 

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50007 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_source_sawyer_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50007 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_target_sawyer_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50008 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_source_ur5e_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50008 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_target_ur5e_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50009 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_source_kinova3_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50009 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_target_kinova3_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50010 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_source_jaco_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50010 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_target_jaco_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50011 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_source_iiwa_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50011 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_lowdim_target_iiwa_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name IIWA --passive

################################################################################################################################################
# lift high dim
# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50006 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_highdim_source_panda_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50006 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_highdim_target_panda_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name Panda --passive

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50007 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_highdim_source_sawyer_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50007 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_highdim_target_sawyer_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50008 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_highdim_source_ur5e_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50008 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_highdim_target_ur5e_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50009 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_highdim_source_kinova3_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50009 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_highdim_target_kinova3_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50010 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_highdim_source_jaco_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50010 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_highdim_target_jaco_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_source_robot_server.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50011 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_highdim_source_iiwa_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 &
# target
python evaluate_policy_target_robot_client.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 100 --seeds 0 --connection --port 50011 --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/passive_target/lift_highdim_target_iiwa_0.001_300.txt --tracking_error_threshold 0.001 --num_iter_max 300 --robot_name IIWA --passive

################################################################################################################################################
################################################################################################################################################


