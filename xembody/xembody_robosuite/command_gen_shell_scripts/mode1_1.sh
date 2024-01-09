# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20200 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_lowdim_source_sawyer_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20200 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_lowdim_target_sawyer_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Sawyer --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20201 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_lowdim_source_sawyer_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20201 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_lowdim_target_sawyer_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Sawyer --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20202 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_lowdim_source_sawyer_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20202 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_lowdim_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20203 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_lowdim_source_sawyer_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20203 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_lowdim_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20204 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_lowdim_source_sawyer_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20204 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_lowdim_target_sawyer_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20205 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_lowdim_source_sawyer_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20205 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_lowdim_target_sawyer_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20206 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_lowdim_source_ur5e_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20206 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_lowdim_target_ur5e_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name UR5e --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20207 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_lowdim_source_ur5e_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20207 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_lowdim_target_ur5e_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name UR5e --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20208 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_lowdim_source_ur5e_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20208 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_lowdim_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20209 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_lowdim_source_ur5e_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20209 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_lowdim_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20210 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_lowdim_source_ur5e_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20210 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_lowdim_target_ur5e_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20211 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_lowdim_source_ur5e_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20211 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_lowdim_target_ur5e_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20212 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_lowdim_source_kinova3_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20212 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_lowdim_target_kinova3_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Kinova3 --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20213 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_lowdim_source_kinova3_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20213 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_lowdim_target_kinova3_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Kinova3 --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20214 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_lowdim_source_kinova3_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20214 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_lowdim_target_kinova3_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20215 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_lowdim_source_kinova3_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20215 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_lowdim_target_kinova3_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20216 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_lowdim_source_kinova3_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20216 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_lowdim_target_kinova3_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20217 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_lowdim_source_kinova3_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20217 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_lowdim_target_kinova3_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20218 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_lowdim_source_jaco_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20218 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_lowdim_target_jaco_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Jaco --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20219 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_lowdim_source_jaco_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20219 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_lowdim_target_jaco_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Jaco --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20220 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_lowdim_source_jaco_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20220 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_lowdim_target_jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20221 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_lowdim_source_jaco_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20221 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_lowdim_target_jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20222 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_lowdim_source_jaco_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20222 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_lowdim_target_jaco_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20223 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_lowdim_source_jaco_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20223 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_lowdim_target_jaco_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20224 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_lowdim_source_iiwa_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20224 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_lowdim_target_iiwa_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name IIWA --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20225 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_lowdim_source_iiwa_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20225 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_lowdim_target_iiwa_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name IIWA --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20226 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_lowdim_source_iiwa_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20226 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_lowdim_target_iiwa_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20227 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_lowdim_source_iiwa_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20227 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_lowdim_target_iiwa_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20228 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_lowdim_source_iiwa_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20228 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_lowdim_target_iiwa_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20229 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_lowdim_source_iiwa_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20229 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_lowdim_target_iiwa_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20230 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_highdim_source_sawyer_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20230 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_highdim_target_sawyer_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Sawyer --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20231 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_highdim_source_sawyer_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20231 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_highdim_target_sawyer_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Sawyer --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20232 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_highdim_source_sawyer_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20232 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_highdim_target_sawyer_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20233 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_highdim_source_sawyer_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20233 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_highdim_target_sawyer_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20234 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_highdim_source_sawyer_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20234 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_highdim_target_sawyer_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20235 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_highdim_source_sawyer_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20235 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/sawyer/can_highdim_target_sawyer_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Sawyer --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20236 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_highdim_source_ur5e_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20236 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_highdim_target_ur5e_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name UR5e --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20237 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_highdim_source_ur5e_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20237 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_highdim_target_ur5e_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name UR5e --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20238 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_highdim_source_ur5e_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20238 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_highdim_target_ur5e_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20239 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_highdim_source_ur5e_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20239 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_highdim_target_ur5e_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20240 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_highdim_source_ur5e_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20240 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_highdim_target_ur5e_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20241 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_highdim_source_ur5e_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20241 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/ur5e/can_highdim_target_ur5e_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name UR5e --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20242 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_highdim_source_kinova3_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20242 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_highdim_target_kinova3_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Kinova3 --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20243 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_highdim_source_kinova3_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20243 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_highdim_target_kinova3_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Kinova3 --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20244 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_highdim_source_kinova3_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20244 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_highdim_target_kinova3_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20245 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_highdim_source_kinova3_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20245 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_highdim_target_kinova3_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20246 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_highdim_source_kinova3_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20246 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_highdim_target_kinova3_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20247 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_highdim_source_kinova3_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20247 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/kinova3/can_highdim_target_kinova3_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Kinova3 --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20248 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_highdim_source_jaco_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20248 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_highdim_target_jaco_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Jaco --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20249 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_highdim_source_jaco_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20249 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_highdim_target_jaco_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name Jaco --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20250 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_highdim_source_jaco_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20250 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_highdim_target_jaco_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20251 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_highdim_source_jaco_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20251 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_highdim_target_jaco_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20252 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_highdim_source_jaco_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20252 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_highdim_target_jaco_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20253 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_highdim_source_jaco_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20253 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/jaco/can_highdim_target_jaco_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name Jaco --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20254 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_highdim_source_iiwa_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20254 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_highdim_target_iiwa_1_delta.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name IIWA --passive --delta_action


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20255 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_highdim_source_iiwa_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20255 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_highdim_target_iiwa_1_absolute.txt --tracking_error_threshold 0.02 --num_iter_max 1 --robot_name IIWA --passive


# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20256 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_highdim_source_iiwa_0.04_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20256 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_highdim_target_iiwa_0.04_300.txt --tracking_error_threshold 0.04 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20257 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_highdim_source_iiwa_0.03_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20257 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_highdim_target_iiwa_0.03_300.txt --tracking_error_threshold 0.03 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20258 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_highdim_source_iiwa_0.02_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20258 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_highdim_target_iiwa_0.02_300.txt --tracking_error_threshold 0.02 --num_iter_max 300 --robot_name IIWA --passive

# source
python evaluate_policy_demo_source_robot_server.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20259 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_highdim_source_iiwa_0.01_300.txt &
# target
python evaluate_policy_demo_target_robot_client.py --n_rollouts 100 --horizon 400 --seeds 0 --connection --port 20259 --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --save_stats_path /home/lawrence/xembody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/can/passive_target/iiwa/can_highdim_target_iiwa_0.01_300.txt --tracking_error_threshold 0.01 --num_iter_max 300 --robot_name IIWA --passive

