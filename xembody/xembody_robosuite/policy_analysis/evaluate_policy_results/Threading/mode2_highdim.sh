################################################################################################################################################
################################################################################################################################################
# threading high dim
# source
python evaluate_policy_demo_source_robot_server.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/threading_d0/image/trained_models/core_threading_d0_image/20240108082159/models/model_epoch_360_Threading_D0_success_0.9.pth --n_rollouts 100 --seeds 0 --connection --port 51113 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_demo_analysis/evaluate_policy_demo_results/active_target/threading_highdim_source_panda_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/threading_d0/image/trained_models/core_threading_d0_image/20240108082159/models/model_epoch_360_Threading_D0_success_0.9.pth --n_rollouts 100 --seeds 0 --connection --port 51113 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_demo_analysis/evaluate_policy_demo_results/active_target/threading_highdim_target_panda_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Panda

# source
python evaluate_policy_demo_source_robot_server.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/threading_d0/image/trained_models/core_threading_d0_image/20240108082159/models/model_epoch_360_Threading_D0_success_0.9.pth --n_rollouts 100 --seeds 0 --connection --port 51113 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_demo_analysis/evaluate_policy_demo_results/active_target/threading_highdim_source_sawyer_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/threading_d0/image/trained_models/core_threading_d0_image/20240108082159/models/model_epoch_360_Threading_D0_success_0.9.pth --n_rollouts 100 --seeds 0 --connection --port 51113 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_demo_analysis/evaluate_policy_demo_results/active_target/threading_highdim_target_sawyer_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Sawyer

# source
python evaluate_policy_demo_source_robot_server.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/threading_d0/image/trained_models/core_threading_d0_image/20240108082159/models/model_epoch_360_Threading_D0_success_0.9.pth --n_rollouts 100 --seeds 0 --connection --port 51113 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_demo_analysis/evaluate_policy_demo_results/active_target/threading_highdim_source_ur5e_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/threading_d0/image/trained_models/core_threading_d0_image/20240108082159/models/model_epoch_360_Threading_D0_success_0.9.pth --n_rollouts 100 --seeds 0 --connection --port 51113 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_demo_analysis/evaluate_policy_demo_results/active_target/threading_highdim_target_ur5e_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name UR5e

# source
python evaluate_policy_demo_source_robot_server.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/threading_d0/image/trained_models/core_threading_d0_image/20240108082159/models/model_epoch_360_Threading_D0_success_0.9.pth --n_rollouts 100 --seeds 0 --connection --port 51113 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_demo_analysis/evaluate_policy_demo_results/active_target/threading_highdim_source_kinova3_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/threading_d0/image/trained_models/core_threading_d0_image/20240108082159/models/model_epoch_360_Threading_D0_success_0.9.pth --n_rollouts 100 --seeds 0 --connection --port 51113 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_demo_analysis/evaluate_policy_demo_results/active_target/threading_highdim_target_kinova3_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Kinova3

# source
python evaluate_policy_demo_source_robot_server.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/threading_d0/image/trained_models/core_threading_d0_image/20240108082159/models/model_epoch_360_Threading_D0_success_0.9.pth --n_rollouts 100 --seeds 0 --connection --port 51113 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_demo_analysis/evaluate_policy_demo_results/active_target/threading_highdim_source_jaco_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/threading_d0/image/trained_models/core_threading_d0_image/20240108082159/models/model_epoch_360_Threading_D0_success_0.9.pth --n_rollouts 100 --seeds 0 --connection --port 51113 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_demo_analysis/evaluate_policy_demo_results/active_target/threading_highdim_target_jaco_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name Jaco

# source
python evaluate_policy_demo_source_robot_server.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/threading_d0/image/trained_models/core_threading_d0_image/20240108082159/models/model_epoch_360_Threading_D0_success_0.9.pth --n_rollouts 100 --seeds 0 --connection --port 51113 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_demo_analysis/evaluate_policy_demo_results/active_target/threading_highdim_source_iiwa_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --passive &
# target
python evaluate_policy_demo_target_robot_client.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/threading_d0/image/trained_models/core_threading_d0_image/20240108082159/models/model_epoch_360_Threading_D0_success_0.9.pth --n_rollouts 100 --seeds 0 --connection --port 51113 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_demo_analysis/evaluate_policy_demo_results/active_target/threading_highdim_target_iiwa_0.015_300.txt --tracking_error_threshold 0.015 --num_iter_max 300 --robot_name IIWA