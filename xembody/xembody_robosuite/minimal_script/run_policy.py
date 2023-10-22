# https://github.com/ARISE-Initiative/robomimic/blob/master/examples/notebooks/run_policy.ipynb
import argparse
import json
import h5py
import imageio
import numpy as np
import os
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
import urllib.request




# Now let's define the main rollout loop. The loop runs the policy to a target horizon and optionally writes the rollout to a video.
def rollout(policy, env, horizon, render=False, video_writer=None, video_skip=5, camera_names=None):
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
        camera_names (list): determines which camera(s) are used for rendering. Pass more than
            one to output a video with multiple camera views concatenated horizontally.
    Returns:
        stats (dict): some statistics for the rollout - such as return, horizon, and task success
    """
    assert isinstance(env, EnvBase)
    assert isinstance(policy, RolloutPolicy)
    assert not (render and (video_writer is not None))

    policy.start_episode()
    obs = env.reset()
    state_dict = env.get_state()
    # breakpoint()

    # hack that is necessary for robosuite tasks for deterministic action playback
    obs = env.reset_to(state_dict)
    
    env.env.robots[0].controller.use_delta = False # change to absolute pose
    for _ in range(100):
        state = np.array([-0.09123698, -0.03099231,  1.01004142,  0.75205779,  0.65589058,
        0.04676371,  0.04505361])
        action = np.zeros(7)
        action[:3] = state[:3]
        action[3:6] = T.quat2axisangle(state[3:])
        obs, _, _, _ = env.step(action)

    eef_site_name = env.env.robots[0].controller.eef_name
    curr_pos = np.array(env.env.sim.data.site_xpos[env.env.sim.model.site_name2id(eef_site_name)])
    curr_rot = np.array(T.mat2quat(env.env.sim.data.site_xmat[env.env.sim.model.site_name2id(eef_site_name)].reshape([3, 3])))
    new_state = np.concatenate((curr_pos, curr_rot))
    new_state = np.concatenate((new_state, [-1]))
    print("Starting state:", new_state)
    
    env.env.robots[0].controller.use_delta = True # change back to delta pose
    results = {}
    video_count = 0  # video frame counter
    total_reward = 0.
    
    target_state_history = np.load("/home/lawrence/xembody/xembody/state_history.npy")
    state_history = []
    try:
        for step_i in range(horizon):#range(len(target_state_history)):# range(horizon):
            # breakpoint()
            # get action from policy
            action = policy(ob=obs)
            print("Action: ", action)
            
            # target_state = target_state_history[step_i]
            # print("Target state: ", target_state)
            # action = np.zeros(7)
            # action[:3] = target_state[:3]
            # action[3:6] = T.quat2axisangle(target_state[3:])
            # action[-1] = target_state[-1]
            # print("Action: ", action)
            # # play action
            # for i in range(10):
            next_obs, r, done, _ = env.step(action)
            
            
            eef_site_name = env.env.robots[0].controller.eef_name
            curr_pos = np.array(env.env.sim.data.site_xpos[env.env.sim.model.site_name2id(eef_site_name)])
            curr_rot = np.array(T.mat2quat(env.env.sim.data.site_xmat[env.env.sim.model.site_name2id(eef_site_name)].reshape([3, 3])))
            new_state = np.concatenate((curr_pos, curr_rot))
            new_state = np.concatenate((new_state, action[[-1]]))
            state_history.append(new_state)
            # print("Actual state: ", new_state)
            

            # compute reward
            total_reward += r
            success = env.is_success()["task"]

            # visualization
            if render:
                env.render(mode="human", camera_name=camera_names[0])
            if video_writer is not None:
                if video_count % video_skip == 0:
                    video_img = []
                    for cam_name in camera_names:
                        video_img.append(env.render(mode="rgb_array", height=512, width=512, camera_name=cam_name))
                    video_img = np.concatenate(video_img, axis=1) # concatenate horizontally
                    video_writer.append_data(video_img)
                video_count += 1

            # break if done or if success
            if done or success:
                break

            # update for next iter
            obs = deepcopy(next_obs)
            state_dict = env.get_state()

    except env.rollout_exceptions as e:
        print("WARNING: got rollout exception {}".format(e))

    stats = dict(Return=total_reward, Horizon=(step_i + 1), Success_Rate=float(success))
    
    # save state_history
    state_history = np.array(state_history)
    # np.save("state_history_mimic.npy", state_history)

    return stats



# main
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--hdf5_path",
        type=str,
        help="Path to .hdf5 file, e.g.: "
        "'path_to_assets_dir/demonstrations/YOUR_DEMONSTRATION/demo.hdf5'",
    ),
    parser.add_argument(
        "--render",
        action="store_true",
    )
    args = parser.parse_args()
    
    ckpt_path = "/home/lawrence/xembody/robomimic/pretrained_models/lift_ph_low_dim_epoch_1000_succ_100.pth"
    # ckpt_path = "/home/lawrence/xembody/robomimic/pretrained_models/can_ph_low_dim_epoch_1150_succ_100.pth"
    device = TorchUtils.get_torch_device(try_to_use_cuda=True)

    # restore policy
    policy, ckpt_dict = FileUtils.policy_from_checkpoint(ckpt_path=ckpt_path, device=device, verbose=True)


    # create environment from saved checkpoint
    env, _ = FileUtils.env_from_checkpoint(
        ckpt_dict=ckpt_dict, 
        render=args.render, # we won't do on-screen rendering in the notebook
        render_offscreen=True, # render to RGB images for video
        verbose=True,
    )

    # Now let's rollout the policy!

    rollout_horizon = 400
    np.random.seed(1)
    torch.manual_seed(1)
    video_path = "rollout.mp4"
    video_writer = imageio.get_writer(video_path, fps=20)
    stats = rollout(
        policy=policy, 
        env=env, 
        horizon=rollout_horizon, 
        render=args.render, 
        video_writer=video_writer, 
        video_skip=5, 
        camera_names=["agentview"]
    )
    print(stats)
    video_writer.close()
    
    
    # use another robot
    