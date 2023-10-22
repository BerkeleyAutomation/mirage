"""
The main script for evaluating a policy in an environment.

Args:
    agent (str): path to saved checkpoint pth file

    horizon (int): if provided, override maximum horizon of rollout from the one 
        in the checkpoint

    env (str): if provided, override name of env from the one in the checkpoint,
        and use it for rollouts

    render (bool): if flag is provided, use on-screen rendering during rollouts

    video_path (str): if provided, render trajectories to this video file path

    video_skip (int): render frames to a video every @video_skip steps

    camera_names (str or [str]): camera name(s) to use for rendering on-screen or to video

    dataset_path (str): if provided, an hdf5 file will be written at this path with the
        rollout data

    dataset_obs (bool): if flag is provided, and @dataset_path is provided, include 
        possible high-dimensional observations in output dataset hdf5 file (by default,
        observations are excluded and only simulator states are saved).

    seed (int): if provided, set seed for rollouts

Example usage:

    # Evaluate a policy with 50 rollouts of maximum horizon 400 and save the rollouts to a video.
    # Visualize the agentview and wrist cameras during the rollout.
    
    python run_trained_agent.py --agent /path/to/model.pth \
        --n_rollouts 50 --horizon 400 --seed 0 \
        --video_path /path/to/output.mp4 \
        --camera_names agentview robot0_eye_in_hand 

    # Write the 50 agent rollouts to a new dataset hdf5.

    python run_trained_agent.py --agent /path/to/model.pth \
        --n_rollouts 50 --horizon 400 --seed 0 \
        --dataset_path /path/to/output.hdf5 --dataset_obs 

    # Write the 50 agent rollouts to a new dataset hdf5, but exclude the dataset observations
    # since they might be high-dimensional (they can be extracted again using the
    # dataset_states_to_obs.py script).

    python run_trained_agent.py --agent /path/to/model.pth \
        --n_rollouts 50 --horizon 400 --seed 0 \
        --dataset_path /path/to/output.hdf5
"""
"""
Change in  /home/lawrence/xembody/robomimic/robomimic/algo/algo.py(323)
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
"""


"""
python evaluate_policy_varying_dynamics_robots.py --agent /home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth --n_rollouts 1 --horizon 400 --seed 0 --video_path /home/lawrence/xembody/robosuite/collected_data/output_lift_low_dim.mp4 --target_robot Sawyer --inner_iters 10

"""




import argparse
import json
import h5py
import imageio
import numpy as np
from copy import deepcopy

import torch

import robomimic
import robomimic.utils.file_utils as FileUtils
import robomimic.utils.torch_utils as TorchUtils
import robomimic.utils.tensor_utils as TensorUtils
import robomimic.utils.obs_utils as ObsUtils
from robomimic.envs.env_base import EnvBase
from robomimic.algo import RolloutPolicy
import robosuite.utils.transform_utils as T
from robosuite.utils.mjcf_utils import array_to_string, string_to_array

def rollout_source_target_robots(policy, env_source, env_target, horizon, render=False, video_writer_source=None, video_writer_target=None, video_skip=5, return_obs=False, camera_names=None, use_delta=True, inner_iters=10):
    """
    Helper function to carry out rollouts. Supports on-screen rendering, off-screen rendering to a video, 
    and returns the rollout trajectory.

    Args:
        policy (instance of RolloutPolicy): policy loaded from a checkpoint
        env (instance of EnvBase): env loaded from a checkpoint or demonstration metadata
        horizon (int): maximum horizon for the rollout
        render (bool): whether to render rollout on-screen
        video_writer (imageio writer): if provided, use to write rollout to video
        video_skip (int): how often to write video frames
        return_obs (bool): if True, return possibly high-dimensional observations along the trajectoryu. 
            They are excluded by default because the low-dimensional simulation states should be a minimal 
            representation of the environment. 
        camera_names (list): determines which camera(s) are used for rendering. Pass more than
            one to output a video with multiple camera views concatenated horizontally.
        use_delta (bool): if True, use delta control instead of absolute control
        
    Returns:
        stats (dict): some statistics for the rollout - such as return, horizon, and task success
        traj (dict): dictionary that corresponds to the rollout trajectory
    """
    assert isinstance(env_source, EnvBase)
    assert isinstance(policy, RolloutPolicy)
    assert not (render and (video_writer_source is not None))

    policy.start_episode()
    obs_source = env_source.reset()
    state_dict_source = env_source.get_state()
    # hack that is necessary for robosuite tasks for deterministic action playback
    obs_source = env_source.reset_to(state_dict_source)
    # breakpoint()
    # print(env_source.env.sim.data.body_xpos[env_source.env.cube_body_id])
    # env_source.env.model.mujoco_objects[0].get_obj().set("pos", array_to_string(obs_source['object'][:3]))
    # env_source.env.model.mujoco_objects[0].get_obj().set("quat", array_to_string(obs_source['object'][3:7]))
    # print(env_source.env.sim.data.body_xpos[env_source.env.cube_body_id])
    eef_site_name_source = env_source.env.robots[0].controller.eef_name
    
    starting_pos_source = np.array(env_source.env.sim.data.site_xpos[env_source.env.sim.model.site_name2id(eef_site_name_source)])
    starting_rot_source = np.array(T.mat2quat(env_source.env.sim.data.site_xmat[env_source.env.sim.model.site_name2id(eef_site_name_source)].reshape([3, 3])))
    starting_state_source = np.concatenate((starting_pos_source, starting_rot_source))
    
    if env_target is not None:
        obs_target = env_target.reset()
        state_dict_target = env_target.get_state()
        # hack that is necessary for robosuite tasks for deterministic action playback
        
        # method 1
        # state_dict_target['states'][10:18] = state_dict_source['states'][10:18] # set the object state to be the same 10 = 1 + 7 (robot0_joint_pos) + 2 (robot0_gripper_qpos)
        # obs_target = env_target.reset_to(state_dict_target)
        # method 2
        cube_pos = env_source.env.sim.data.get_joint_qpos("cube_joint0")
        env_target.env.sim.data.set_joint_qpos("cube_joint0", cube_pos)
        env_target.env.sim.forward()
        
        eef_site_name_target = env_target.env.robots[0].controller.eef_name
        
        # breakpoint()
        # print(env_target.env.sim.data.body_xpos[env_target.env.cube_body_id])
        # env_target.env.model.mujoco_objects[0].get_obj().set("pos", array_to_string(obs_source['object'][:3]))
        # env_target.env.model.mujoco_objects[0].get_obj().set("quat", array_to_string(obs_source['object'][3:7]))
        # env_target.env.sim.forward()
        # print(env_target.env.sim.data.body_xpos[env_target.env.cube_body_id])
    
        env_target.env.robots[0].controller.use_delta = False # change to absolute pose for setting the initial state
        
        for _ in range(100):
            action = np.zeros(7)
            action[:3] = starting_state_source[:3]
            action[3:6] = T.quat2axisangle(starting_state_source[3:])
            obs_target, _, _, _ = env_target.step(action)

        
        starting_pos_target = np.array(env_target.env.sim.data.site_xpos[env_target.env.sim.model.site_name2id(eef_site_name_target)])
        starting_rot_target = np.array(T.mat2quat(env_target.env.sim.data.site_xmat[env_target.env.sim.model.site_name2id(eef_site_name_target)].reshape([3, 3])))
        starting_state_target = np.concatenate((starting_pos_target, starting_rot_target))
        
        try:
            assert np.allclose(starting_state_source, starting_state_target, atol=0.005), "Starting states are not the same"
        except:
            print("Starting states are not the same"
                  "Source: ", starting_state_source,
                  "Target: ", starting_state_target)
            breakpoint()
        env_target.env.robots[0].controller.use_delta = use_delta # change back to delta pose
    
    
    video_count = 0  # video frame counter
    total_reward_source = 0.
    traj_source = dict(actions=[], rewards=[], dones=[], states=[], initial_state_dict=state_dict_source)
    if return_obs:
        # store observations too
        traj_source.update(dict(obs=[], next_obs=[]))
    
    
    if env_target is not None:
        total_reward_target = 0.
        traj_target = dict(actions=[], rewards=[], dones=[], states=[], initial_state_dict=state_dict_target)
        if return_obs:
            # store observations too
            traj_target.update(dict(obs=[], next_obs=[]))
    else:
        traj_target = None
    
    
    try:
        # breakpoint()
        for step_i in range(horizon):
            print("Step: ", step_i)
            # source robot
            action_source = policy(ob=obs_source) # get action from policy            
            next_obs_source, r_source, done_source, _ = env_source.step(action_source) # execute action            
            total_reward_source += r_source # compute reward
            success_source = env_source.is_success()["task"]
            
            curr_pos_source = np.array(env_source.env.sim.data.site_xpos[env_source.env.sim.model.site_name2id(eef_site_name_source)])
            curr_rot_source = np.array(T.mat2quat(env_source.env.sim.data.site_xmat[env_source.env.sim.model.site_name2id(eef_site_name_source)].reshape([3, 3])))
            current_state_source = np.concatenate((curr_pos_source, curr_rot_source))
            
            # target robot
            if env_target is not None:
                if use_delta:
                    # execute the same action
                    action_target = action_source
                    next_obs_target, r_target, done_target, _ = env_target.step(action_target) # execute action
                else:
                    action_target = np.zeros(7)
                    action_target[:3] = current_state_source[:3]
                    action_target[3:6] = T.quat2axisangle(current_state_source[3:])
                    action_target[-1] = action_source[-1]
                    for i in range(inner_iters):
                        next_obs_target, r_target, done_target, _ = env_target.step(action_target)
                
                curr_pos_target = np.array(env_target.env.sim.data.site_xpos[env_target.env.sim.model.site_name2id(eef_site_name_target)])
                curr_rot_target = np.array(T.mat2quat(env_target.env.sim.data.site_xmat[env_target.env.sim.model.site_name2id(eef_site_name_target)].reshape([3, 3])))
                current_state_target = np.concatenate((curr_pos_target, curr_rot_target))
                error = np.linalg.norm(current_state_source - current_state_target)
                print("Error: ", error)
                total_reward_target += r_target # compute reward
                success_target = env_target.is_success()["task"]

            # visualization
            # breakpoint()
            # env_source.render(mode="human", camera_name=camera_names[0])
            if render:
                if env_target is not None:
                    env_target.render(mode="human", camera_name=camera_names[0])
                else:
                    env_source.render(mode="human", camera_name=camera_names[0])
            if video_writer_source is not None:
                if video_count % video_skip == 0:
                    video_img_source = []
                    for cam_name in camera_names:
                        video_img_source.append(env_source.render(mode="rgb_array", height=512, width=512, camera_name=cam_name))
                    video_img_source = np.concatenate(video_img_source, axis=1) # concatenate horizontally
                    video_writer_source.append_data(video_img_source)
                    # breakpoint()
                    
                    if env_target is not None:
                        video_img_target = []
                        for cam_name in camera_names:
                            video_img_target.append(env_target.render(mode="rgb_array", height=512, width=512, camera_name=cam_name))
                        video_img_target = np.concatenate(video_img_target, axis=1) # concatenate horizontally
                        video_writer_target.append_data(video_img_target)
                video_count += 1

            # collect transition
            traj_source["actions"].append(action_source)
            traj_source["rewards"].append(r_source)
            traj_source["dones"].append(done_source)
            traj_source["states"].append(state_dict_source["states"])
            if return_obs:
                # Note: We need to "unprocess" the observations to prepare to write them to dataset.
                #       This includes operations like channel swapping and float to uint8 conversion
                #       for saving disk space.
                traj_source["obs"].append(ObsUtils.unprocess_obs_dict(obs_source))
                traj_source["next_obs"].append(ObsUtils.unprocess_obs_dict(next_obs_source))
                
            if env_target is not None:
                traj_target["actions"].append(action_target)
                traj_target["rewards"].append(r_target)
                traj_target["dones"].append(done_target)
                traj_target["states"].append(state_dict_target["states"])
                if return_obs:
                    # Note: We need to "unprocess" the observations to prepare to write them to dataset.
                    #       This includes operations like channel swapping and float to uint8 conversion
                    #       for saving disk space.
                    traj_target["obs"].append(ObsUtils.unprocess_obs_dict(obs_target))
                    traj_target["next_obs"].append(ObsUtils.unprocess_obs_dict(next_obs_target))

            # break if done or if success
            if env_target is None:
                if done_source or success_source:
                    break
            else:
                if done_source and done_target or success_source and success_target:
                    break
                elif done_source and not done_target or success_source and not success_target:
                    print("Source robot done and target robot is not!")
                    # break
                elif not done_source and done_target or not success_source and success_target:
                    print("Target robot done and source robot is not!")

            # update for next iter
            obs_source = deepcopy(next_obs_source)
            state_dict_source = env_source.get_state()
            
            if env_target is not None:
                obs_target = deepcopy(next_obs_target)
                state_dict_target = env_target.get_state()

    except:
        if env_source.rollout_exceptions:
            print("WARNING: got source robot rollout exception {}".format(env_source.rollout_exceptions))
        if env_target is not None:
            if env_target.rollout_exceptions:
                print("WARNING: got target robot rollout exception {}".format(env_target.rollout_exceptions))

    stats_source = dict(Return=total_reward_source, Horizon=(step_i + 1), Success_Rate=float(success_source))
    
    if env_target is not None:
        stats_target = dict(Return=total_reward_target, Horizon=(step_i + 1), Success_Rate=float(success_target))
    else:
        stats_target = None

    if return_obs:
        # convert list of dict to dict of list for obs dictionaries (for convenient writes to hdf5 dataset)
        traj_source["obs"] = TensorUtils.list_of_flat_dict_to_dict_of_list(traj_source["obs"])
        traj_source["next_obs"] = TensorUtils.list_of_flat_dict_to_dict_of_list(traj_source["next_obs"])
        
        if env_target is not None:
            # convert list of dict to dict of list for obs dictionaries (for convenient writes to hdf5 dataset)
            traj_target["obs"] = TensorUtils.list_of_flat_dict_to_dict_of_list(traj_target["obs"])
            traj_target["next_obs"] = TensorUtils.list_of_flat_dict_to_dict_of_list(traj_target["next_obs"])

    # list to numpy array
    for k in traj_source:
        if k == "initial_state_dict":
            continue
        if isinstance(traj_source[k], dict):
            for kp in traj_source[k]:
                traj_source[k][kp] = np.array(traj_source[k][kp])
        else:
            traj_source[k] = np.array(traj_source[k])

    if env_target is not None:
        # list to numpy array
        for k in traj_target:
            if k == "initial_state_dict":
                continue
            if isinstance(traj_target[k], dict):
                for kp in traj_target[k]:
                    traj_target[k][kp] = np.array(traj_target[k][kp])
            else:
                traj_target[k] = np.array(traj_target[k])
    
    return stats_source, traj_source, stats_target, traj_target


def run_trained_agent(args):
    # some arg checking
    write_video = (args.video_path is not None)
    assert not (args.render and write_video) # either on-screen or video but not both
    if args.render:
        # on-screen rendering can only support one camera
        assert len(args.camera_names) == 1

    # relative path to agent
    ckpt_path = args.agent

    # device
    device = TorchUtils.get_torch_device(try_to_use_cuda=True)

    # restore policy
    policy, ckpt_dict = FileUtils.policy_from_checkpoint(ckpt_path=ckpt_path, device=device, verbose=True)

    # read rollout settings
    rollout_num_episodes = args.n_rollouts
    rollout_horizon = args.horizon
    if rollout_horizon is None:
        # read horizon from config
        config, _ = FileUtils.config_from_checkpoint(ckpt_dict=ckpt_dict)
        rollout_horizon = config.experiment.rollout.horizon

    # breakpoint()
    # create environment from saved checkpoint
    env_source, _ = FileUtils.env_from_checkpoint(
        ckpt_dict=ckpt_dict, 
        env_name=args.env, 
        render=args.render, 
        render_offscreen=(args.video_path is not None), 
        verbose=True,
    )
    
    if args.target_robot:
        env_target, _ = FileUtils.env_from_checkpoint(
            ckpt_dict=ckpt_dict, 
            env_name=args.env, 
            render=args.render, 
            render_offscreen=(args.video_path is not None), 
            verbose=True,
            robot=args.target_robot
        )
    else:
        env_target = None
    

    # maybe set seed
    if args.seed is not None:
        np.random.seed(args.seed)
        torch.manual_seed(args.seed)

    # maybe create video writer
    video_writer_source = None
    video_writer_target = None
    if write_video:
        video_writer_source = imageio.get_writer(args.video_path, fps=20)
        if args.target_robot:
            video_writer_target = imageio.get_writer(args.video_path.replace(".mp4", "_target.mp4"), fps=20)

    # maybe open hdf5 to write rollouts
    write_dataset = (args.dataset_path is not None)
    if write_dataset:
        data_writer = h5py.File(args.dataset_path, "w")
        data_grp = data_writer.create_group("data")
        total_samples = 0

    rollout_stats_source = []
    if args.target_robot:
        rollout_stats_target = []
    for i in range(rollout_num_episodes):
        print("Rollout {}/{}".format(i + 1, rollout_num_episodes))
        stats_source, traj_source, stats_target, traj_target = rollout_source_target_robots(
            policy=policy, 
            env_source=env_source, 
            env_target=env_target,
            horizon=rollout_horizon, 
            render=args.render, 
            video_writer_source=video_writer_source, 
            video_writer_target=video_writer_target,
            video_skip=args.video_skip, 
            return_obs=(write_dataset and args.dataset_obs),
            camera_names=args.camera_names,
            use_delta=args.use_delta,
            inner_iters=args.inner_iters
        )
        rollout_stats_source.append(stats_source)
        if args.target_robot:
            rollout_stats_target.append(stats_target)

        if write_dataset:
            # store transitions
            ep_data_grp = data_grp.create_group("demo_{}".format(i))
            ep_data_grp.create_dataset("actions", data=np.array(traj_source["actions"]))
            ep_data_grp.create_dataset("states", data=np.array(traj_source["states"]))
            ep_data_grp.create_dataset("rewards", data=np.array(traj_source["rewards"]))
            ep_data_grp.create_dataset("dones", data=np.array(traj_source["dones"]))
            if args.dataset_obs:
                for k in traj_source["obs"]:
                    ep_data_grp.create_dataset("obs/{}".format(k), data=np.array(traj_source["obs"][k]))
                    ep_data_grp.create_dataset("next_obs/{}".format(k), data=np.array(traj_source["next_obs"][k]))

            # episode metadata
            if "model" in traj_source["initial_state_dict"]:
                ep_data_grp.attrs["model_file"] = traj_source["initial_state_dict"]["model"] # model xml for this episode
            ep_data_grp.attrs["num_samples"] = traj_source["actions"].shape[0] # number of transitions in this episode
            total_samples += traj_source["actions"].shape[0]

    rollout_stats_source = TensorUtils.list_of_flat_dict_to_dict_of_list(rollout_stats_source)
    avg_rollout_stats_source = { k : np.mean(rollout_stats_source[k]) for k in rollout_stats_source }
    avg_rollout_stats_source["Num_Success"] = np.sum(rollout_stats_source["Success_Rate"])
    print("Average Rollout Stats Source")
    print(json.dumps(avg_rollout_stats_source, indent=4))
    
    if args.target_robot:
        rollout_stats_target = TensorUtils.list_of_flat_dict_to_dict_of_list(rollout_stats_target)
        avg_rollout_stats_target = { k : np.mean(rollout_stats_target[k]) for k in rollout_stats_target }
        avg_rollout_stats_target["Num_Success"] = np.sum(rollout_stats_target["Success_Rate"])
        print("Average Rollout Stats Target")
        print(json.dumps(avg_rollout_stats_target, indent=4))

    if write_video:
        video_writer_source.close()
        if args.target_robot:
            video_writer_target.close()

    if write_dataset:
        # global metadata
        data_grp.attrs["total"] = total_samples
        data_grp.attrs["env_args"] = json.dumps(env_source.serialize(), indent=4) # environment info
        data_writer.close()
        print("Wrote dataset trajectories to {}".format(args.dataset_path))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Path to trained model
    parser.add_argument(
        "--agent",
        type=str,
        required=True,
        help="path to saved checkpoint pth file",
    )

    # number of rollouts
    parser.add_argument(
        "--n_rollouts",
        type=int,
        default=27,
        help="number of rollouts",
    )

    # maximum horizon of rollout, to override the one stored in the model checkpoint
    parser.add_argument(
        "--horizon",
        type=int,
        default=None,
        help="(optional) override maximum horizon of rollout from the one in the checkpoint",
    )

    # Env Name (to override the one stored in model checkpoint)
    parser.add_argument(
        "--env",
        type=str,
        default=None,
        help="(optional) override name of env from the one in the checkpoint, and use\
            it for rollouts",
    )

    # Whether to render rollouts to screen
    parser.add_argument(
        "--render",
        action='store_true',
        help="on-screen rendering",
    )

    # Dump a video of the rollouts to the specified path
    parser.add_argument(
        "--video_path",
        type=str,
        default=None,
        help="(optional) render rollouts to this video file path",
    )

    # How often to write video frames during the rollout
    parser.add_argument(
        "--video_skip",
        type=int,
        default=5,
        help="render frames to video every n steps",
    )

    # camera names to render
    parser.add_argument(
        "--camera_names",
        type=str,
        nargs='+',
        default=["agentview"],
        help="(optional) camera name(s) to use for rendering on-screen or to video",
    )

    # If provided, an hdf5 file will be written with the rollout data
    parser.add_argument(
        "--dataset_path",
        type=str,
        default=None,
        help="(optional) if provided, an hdf5 file will be written at this path with the rollout data",
    )

    # If True and @dataset_path is supplied, will write possibly high-dimensional observations to dataset.
    parser.add_argument(
        "--dataset_obs",
        action='store_true',
        help="include possibly high-dimensional observations in output dataset hdf5 file (by default,\
            observations are excluded and only simulator states are saved)",
    )

    # for seeding before starting rollouts
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="(optional) set seed for rollouts",
    )

    # If provided, an hdf5 file will be written with the rollout data
    parser.add_argument(
        "--target_robot",
        type=str,
        default=None,
        help="(optional) if provided, there will be a second robot tracking the panda robot where the policy is executed with,\
            [Sawyer, UR5e, Panda, Kinova3, Jaco, IIWA]",
    )
    
    parser.add_argument(
        "--use_delta",
        action='store_true',
        help="whether let the target robot execute the same delta action or track the absolute pose of the source robot",
    )
    
    parser.add_argument(
        "--inner_iters",
        type=int,
        default=10,
        help="for absolute pose tracking, how many inner iterations to use",
    )
    
    
    args = parser.parse_args()
    run_trained_agent(args)

