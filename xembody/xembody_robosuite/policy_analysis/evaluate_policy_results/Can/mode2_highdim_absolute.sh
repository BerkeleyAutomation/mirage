################################################################################################################################################
################################################################################################################################################
# can high dim
# source
# python evaluate_policy_demo_source_robot_server.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/can/image/trained_models/can_image/20240113010406/models/model_epoch_160_PickPlaceCan_success_0.94.pth --n_rollouts 100 --seeds 0 --connection --port 10137 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/can_highdim_source_panda_0.03_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive --device cuda:3 &
# # target
# python evaluate_policy_demo_target_robot_client.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/can/image/trained_models/can_image/20240113010406/models/model_epoch_160_PickPlaceCan_success_0.94.pth --n_rollouts 100 --seeds 0 --connection --port 10137 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/can_highdim_target_panda_0.03_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Panda --device cuda:3

# source
python evaluate_policy_demo_source_robot_server.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/can/image/trained_models/can_image/20240113010406/models/model_epoch_160_PickPlaceCan_success_0.94.pth --n_rollouts 100 --seeds 0 --connection --port 10138 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/can_highdim_source_sawyer_0.03_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive --device cuda:3 &
# target
python evaluate_policy_demo_target_robot_client.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/can/image/trained_models/can_image/20240113010406/models/model_epoch_160_PickPlaceCan_success_0.94.pth --n_rollouts 100 --seeds 0 --connection --port 10138 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/can_highdim_target_sawyer_0.03_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Sawyer --device cuda:3

# source
# python evaluate_policy_demo_source_robot_server.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/can/image/trained_models/can_image/20240113010406/models/model_epoch_160_PickPlaceCan_success_0.94.pth --n_rollouts 100 --seeds 0 --connection --port 10139 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/can_highdim_source_ur5e_0.03_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive --device cuda:3 &
# # target
# python evaluate_policy_demo_target_robot_client.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/can/image/trained_models/can_image/20240113010406/models/model_epoch_160_PickPlaceCan_success_0.94.pth --n_rollouts 100 --seeds 0 --connection --port 10139 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/can_highdim_target_ur5e_0.03_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name UR5e --device cuda:3

# source
# python evaluate_policy_demo_source_robot_server.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/can/image/trained_models/can_image/20240113010406/models/model_epoch_160_PickPlaceCan_success_0.94.pth --n_rollouts 100 --seeds 0 --connection --port 10140 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/can_highdim_source_kinova3_0.03_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive --device cuda:3 &
# # target
# python evaluate_policy_demo_target_robot_client.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/can/image/trained_models/can_image/20240113010406/models/model_epoch_160_PickPlaceCan_success_0.94.pth --n_rollouts 100 --seeds 0 --connection --port 10140 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/can_highdim_target_kinova3_0.03_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Kinova3 --device cuda:3

# # source
# python evaluate_policy_demo_source_robot_server.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/can/image/trained_models/can_image/20240113010406/models/model_epoch_160_PickPlaceCan_success_0.94.pth --n_rollouts 100 --seeds 0 --connection --port 10141 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/can_highdim_source_jaco_0.03_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive --device cuda:3 &
# # target
# python evaluate_policy_demo_target_robot_client.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/can/image/trained_models/can_image/20240113010406/models/model_epoch_160_PickPlaceCan_success_0.94.pth --n_rollouts 100 --seeds 0 --connection --port 10141 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/can_highdim_target_jaco_0.03_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name Jaco --device cuda:3

# source
# python evaluate_policy_demo_source_robot_server.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/can/image/trained_models/can_image/20240113010406/models/model_epoch_160_PickPlaceCan_success_0.94.pth --n_rollouts 100 --seeds 0 --connection --port 10142 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/can_highdim_source_iiwa_0.03_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --passive --device cuda:3 &
# # target
# python evaluate_policy_demo_target_robot_client.py --agent /home/kdharmarajan/x-embody/mimicgen_environments/training_results/core/can/image/trained_models/can_image/20240113010406/models/model_epoch_160_PickPlaceCan_success_0.94.pth --n_rollouts 100 --seeds 0 --connection --port 10142 --save_stats_path /home/kdharmarajan/x-embody/xembody/xembody_robosuite/policy_analysis/evaluate_policy_results/active_target/can_highdim_target_iiwa_0.03_1_absolute.txt --tracking_error_threshold 0.03 --num_iter_max 1 --robot_name IIWA --device cuda:3