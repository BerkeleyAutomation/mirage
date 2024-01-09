# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31200 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_lowdim_source_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31200 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_lowdim_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31201 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_lowdim_source_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31201 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_lowdim_target_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31202 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_lowdim_source_ur5e_0.04_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31202 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_lowdim_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31203 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_lowdim_source_ur5e_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31203 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_lowdim_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31204 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_lowdim_source_ur5e_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31204 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_lowdim_target_ur5e_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31205 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_lowdim_source_ur5e_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31205 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_lowdim_target_ur5e_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31206 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_highdim_source_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31206 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_highdim_target_ur5e_1_delta.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31207 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_highdim_source_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31207 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_highdim_target_ur5e_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31208 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_highdim_source_ur5e_0.04_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31208 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_highdim_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31209 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_highdim_source_ur5e_0.03_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31209 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_highdim_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31210 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_highdim_source_ur5e_0.02_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31210 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_highdim_target_ur5e_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31211 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_highdim_source_ur5e_0.01_300.txt --passive &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 31211 --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/square/active_target/ur5e/square_highdim_target_ur5e_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name UR5e

