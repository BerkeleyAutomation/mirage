# can high dim
echo "can high dim"
python evaluate_policy_varying_dynamics_robots.py --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_image_epoch_300_succ_100.pth --n_rollouts 50 --horizon 400 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_can_highdim.mp4 --camera_names agentview robot0_eye_in_hand 
# can low dim
echo "can low dim"
python evaluate_policy_varying_dynamics_robots.py --agent /home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth --n_rollouts 50 --horizon 400 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_can_low_dim.mp4

# lift high dim
echo "lift high dim"
python evaluate_policy_varying_dynamics_robots.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_image_epoch_500_succ_100.pth --n_rollouts 50 --horizon 400 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_lift_high_dim.mp4 --camera_names agentview robot0_eye_in_hand
# lift low dim
echo "lift low dim"
python evaluate_policy_varying_dynamics_robots.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 50 --horizon 400 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_lift_low_dim.mp4

# square high dim
echo "square high dim"
python evaluate_policy_varying_dynamics_robots.py --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_image_epoch_540_succ_78.pth --n_rollouts 50 --horizon 400 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_square_high_dim.mp4 --camera_names agentview robot0_eye_in_hand
# square low dim
echo "square low dim"
python evaluate_policy_varying_dynamics_robots.py --agent /home/lawrence/xembody/robomimic/pretrained_models/square_ph_low_dim_epoch_1850_succ_84.pth --n_rollouts 50 --horizon 400 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_square_low_dim.mp4

# tool hang high dim
echo "tool hang high dim"
python evaluate_policy_varying_dynamics_robots.py --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_image_epoch_440_succ_74.pth --n_rollouts 50 --horizon 700 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_toolhang_high_dim.mp4 --camera_names agentview robot0_eye_in_hand
# tool hang low dim
echo "tool hang low dim"
python evaluate_policy_varying_dynamics_robots.py --agent /home/lawrence/xembody/robomimic/pretrained_models/tool_hang_ph_low_dim_epoch_2000_succ_14.pth --n_rollouts 50 --horizon 700 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_toolhang_low_dim.mp4 

# transport high dim
echo "transport high dim"
python evaluate_policy_varying_dynamics_robots.py --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_image_epoch_580_succ_70.pth --n_rollouts 50 --horizon 700 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_transport_high_dim.mp4 --camera_names agentview robot0_eye_in_hand
# transport low dim
echo "transport low dim"
python evaluate_policy_varying_dynamics_robots.py --agent /home/lawrence/xembody/robomimic/pretrained_models/transport_ph_low_dim_epoch_1000_succ_78.pth --n_rollouts 50 --horizon 700 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_transport_low_dim.mp4 