"""
A convenience script to playback random demonstrations from
a set of demonstrations stored in a hdf5 file.

Arguments:
    --folder (str): Path to demonstrations
    --use-actions (optional): If this flag is provided, the actions are played back
        through the MuJoCo simulator, instead of loading the simulator states
        one by one.
    --visualize-gripper (optional): If set, will visualize the gripper site

Example:
    $ python playback_demonstrations_from_hdf5.py --hdf5_path ../models/assets/demonstrations/lift/demo.hdf5
"""
# python /home/lawrence/xembody/xembody/xembody_robosuite/playback_demonstrations_from_hdf5.py --hdf5_path /home/lawrence/xembody/robomimic/datasets/lift/mh/demo_v141.hdf5 --camera_names "sideview"

import argparse
import json
import os
import random

import h5py
import numpy as np
from copy import deepcopy

import robosuite


import robomimic.utils.tensor_utils as TensorUtils
import robomimic.utils.file_utils as FileUtils
import robomimic.utils.env_utils as EnvUtils
from robomimic.envs.env_base import EnvBase

def extract_trajectory(
    env, 
    initial_state, 
    states, 
    actions,
    done_mode,
):
    """
    Helper function to extract observations, rewards, and dones along a trajectory using
    the simulator environment.

    Args:
        env (instance of EnvBase): environment
        initial_state (dict): initial simulation state to load
        states (np.array): array of simulation states to load to extract information
        actions (np.array): array of actions
        done_mode (int): how to write done signal. If 0, done is 1 whenever s' is a 
            success state. If 1, done is 1 at the end of each trajectory. 
            If 2, do both.
    """
    assert isinstance(env, EnvBase)
    assert states.shape[0] == actions.shape[0]

    # load the initial state
    env.reset()
    obs = env.reset_to(initial_state)

    traj = dict(
        obs=[], 
        next_obs=[], 
        rewards=[], 
        dones=[], 
        actions=np.array(actions), 
        states=np.array(states), 
        initial_state_dict=initial_state,
    )
    traj_len = states.shape[0]
    # iteration variable @t is over "next obs" indices
    for t in range(1, traj_len + 1):
        # get next observation
        if t == traj_len:
            # play final action to get next observation for last timestep
            next_obs, _, _, _ = env.step(actions[t - 1])
            env.render(mode="human", camera_name=args.camera_names[0])
        else:
            # reset to simulator state to get observation
            next_obs = env.reset_to({"states" : states[t]})
            env.render(mode="human", camera_name=args.camera_names[0])

        # infer reward signal
        # note: our tasks use reward r(s'), reward AFTER transition, so this is
        #       the reward for the current timestep
        r = env.get_reward()
        print("Success", env.is_success()["task"])
        # infer done signal
        done = False
        if (done_mode == 1) or (done_mode == 2):
            # done = 1 at end of trajectory
            done = done or (t == traj_len)
        if (done_mode == 0) or (done_mode == 2):
            # done = 1 when s' is task success state
            done = done or env.is_success()["task"]
        done = int(done)

        # collect transition
        traj["obs"].append(obs)
        traj["next_obs"].append(next_obs)
        traj["rewards"].append(r)
        traj["dones"].append(done)

        # update for next iter
        obs = deepcopy(next_obs)

    # convert list of dict to dict of list for obs dictionaries (for convenient writes to hdf5 dataset)
    traj["obs"] = TensorUtils.list_of_flat_dict_to_dict_of_list(traj["obs"])
    traj["next_obs"] = TensorUtils.list_of_flat_dict_to_dict_of_list(traj["next_obs"])

    # list to numpy array
    for k in traj:
        if k == "initial_state_dict":
            continue
        if isinstance(traj[k], dict):
            for kp in traj[k]:
                traj[k][kp] = np.array(traj[k][kp])
        else:
            traj[k] = np.array(traj[k])

    return traj





if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--hdf5_path",
        type=str,
        help="Path to .hdf5 file, e.g.: "
        "'path_to_assets_dir/demonstrations/YOUR_DEMONSTRATION/demo.hdf5'",
    ),
    parser.add_argument(
        "--use-actions",
        action="store_true",
    )
    
    # specify number of demos to process - useful for debugging conversion with a handful
    # of trajectories
    parser.add_argument(
        "--n",
        type=int,
        default=None,
        help="(optional) stop after n trajectories are processed",
    )

    # flag for reward shaping
    parser.add_argument(
        "--shaped", 
        action='store_true',
        help="(optional) use shaped rewards",
    )

    # camera names to use for observations
    parser.add_argument(
        "--camera_names",
        type=str,
        nargs='+',
        default=[],
        help="(optional) camera name(s) to use for image observations. Leave out to not use image observations.",
    )

    parser.add_argument(
        "--camera_height",
        type=int,
        default=84,
        help="(optional) height of image observations",
    )

    parser.add_argument(
        "--camera_width",
        type=int,
        default=84,
        help="(optional) width of image observations",
    )

    # specifies how the "done" signal is written. If "0", then the "done" signal is 1 wherever 
    # the transition (s, a, s') has s' in a task completion state. If "1", the "done" signal 
    # is one at the end of every trajectory. If "2", the "done" signal is 1 at task completion
    # states for successful trajectories and 1 at the end of all trajectories.
    parser.add_argument(
        "--done_mode",
        type=int,
        default=0,
        help="how to write done signal. If 0, done is 1 whenever s' is a success state.\
            If 1, done is 1 at the end of each trajectory. If 2, both.",
    )

    # flag for copying rewards from source file instead of re-writing them
    parser.add_argument(
        "--copy_rewards", 
        action='store_true',
        help="(optional) copy rewards from source file instead of inferring them",
    )

    # flag for copying dones from source file instead of re-writing them
    parser.add_argument(
        "--copy_dones", 
        action='store_true',
        help="(optional) copy dones from source file instead of inferring them",
    )

    # flag to exclude next obs in dataset
    parser.add_argument(
        "--exclude-next-obs", 
        action='store_true',
        help="(optional) exclude next obs in dataset",
    )

    # flag to compress observations with gzip option in hdf5
    parser.add_argument(
        "--compress", 
        action='store_true',
        help="(optional) compress observations with gzip option in hdf5",
    )
    
    args = parser.parse_args()

    # demo_path = args.hdf5_path
    # hdf5_path = os.path.join(demo_path)
    # f = h5py.File(hdf5_path, "r")
    # env_name = f["data"].attrs["env"]
    # env_info = json.loads(f["data"].attrs["env_info"])

    # env = robosuite.make(
    #     **env_info,
    #     has_renderer=True,
    #     has_offscreen_renderer=False,
    #     ignore_done=True,
    #     use_camera_obs=False,
    #     reward_shaping=True,
    #     control_freq=20,
    # )

    
    # create environment to use for data processing
    env_meta = FileUtils.get_env_metadata_from_dataset(dataset_path=args.hdf5_path)
    # env_meta["env_kwargs"]["has_renderer"] = True
    env_meta["env_kwargs"]["has_offscreen_renderer"] = True
    env = EnvUtils.create_env_for_data_processing(
        env_meta=env_meta,
        camera_names=args.camera_names, 
        camera_height=args.camera_height, 
        camera_width=args.camera_width, 
        reward_shaping=args.shaped,
    )

    print("==== Using environment with the following metadata ====")
    print(json.dumps(env.serialize(), indent=4))
    print("")

    # some operations for playback are robosuite-specific, so determine if this environment is a robosuite env
    is_robosuite_env = EnvUtils.is_robosuite_env(env_meta)

    # list of all demonstration episodes (sorted in increasing number order)
    f = h5py.File(args.hdf5_path, "r")
    demos = list(f["data"].keys())
    inds = np.argsort([int(elem[5:]) for elem in demos])
    demos = [demos[i] for i in inds]

    # maybe reduce the number of demonstrations to playback
    if args.n is not None:
        demos = demos[:args.n]

    # demos = [demos[i] for i in np.array([1,51,101,151,201, 251]).astype(int)]
    total_samples = 0
    for ind in range(len(demos)):
        print(ind)
        ep = demos[ind]

        # prepare initial state to reload from
        states = f["data/{}/states".format(ep)][()]
        initial_state = dict(states=states[0])
        if is_robosuite_env:
            initial_state["model"] = f["data/{}".format(ep)].attrs["model_file"]

        # extract obs, rewards, dones
        actions = f["data/{}/actions".format(ep)][()]
        traj = extract_trajectory(
            env=env, 
            initial_state=initial_state, 
            states=states, 
            actions=actions,
            done_mode=0,
        )
    
    
    
    # # list of all demonstrations episodes
    # demos = list(f["data"].keys())

    # while True:
    #     print("Playing back random episode... (press ESC to quit)")

    #     # select an episode randomly
    #     ep = random.choice(demos)

    #     # read the model xml, using the metadata stored in the attribute for this episode
    #     model_xml = f["data/{}".format(ep)].attrs["model_file"]

    #     env.reset()
    #     xml = env.edit_model_xml(model_xml)
    #     env.reset_from_xml_string(xml)
    #     env.sim.reset()
    #     env.viewer.set_camera(0)

    #     # load the flattened mujoco states
    #     states = f["data/{}/states".format(ep)][()]

    #     if args.use_actions:

    #         # load the initial state
    #         env.sim.set_state_from_flattened(states[0])
    #         env.sim.forward()

    #         # load the actions and play them back open-loop
    #         actions = np.array(f["data/{}/actions".format(ep)][()])
    #         num_actions = actions.shape[0]

    #         for j, action in enumerate(actions):
    #             env.step(action)
    #             env.render()

    #             if j < num_actions - 1:
    #                 # ensure that the actions deterministically lead to the same recorded states
    #                 state_playback = env.sim.get_state().flatten()
    #                 if not np.all(np.equal(states[j + 1], state_playback)):
    #                     err = np.linalg.norm(states[j + 1] - state_playback)
    #                     print(f"[warning] playback diverged by {err:.2f} for ep {ep} at step {j}")

    #     else:

    #         # force the sequence of internal mujoco states one by one
    #         for state in states:
    #             env.sim.set_state_from_flattened(state)
    #             env.sim.forward()
    #             env.render()

    # f.close()
