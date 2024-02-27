"""
A convenience script to playback random demonstrations from
a set of demonstrations stored in a hdf5 file.

Arguments:
    --folder (str): Path to demonstrations

Example:
    $ python convert_to_size_256_images --folder ../models/assets/demonstrations/lift/
"""

import argparse
import json
import os
import random

import h5py
import numpy as np

import robosuite
import robomimic.utils.file_utils as FileUtils

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file",
        type=str,
        help="Path to your demonstration folder that contains the demo.hdf5 file, e.g.: "
        "'path_to_assets_dir/demonstrations/YOUR_DEMONSTRATION'",
    ),
    parser.add_argument(
        "--checkpoint",
        type=str,
        help="Path to checkpoint to get the environment "
        "'path_to_assets_dir/demonstrations/YOUR_DEMONSTRATION'",
    ),
    args = parser.parse_args()

    hdf5_path = args.file
    f = h5py.File(hdf5_path, "r")

    new_hdf5_path = hdf5_path.replace('.hdf5', '_256.hdf5')
    data_writer = h5py.File(new_hdf5_path, "w")
    data_grp = data_writer.create_group("data")

    policy, ckpt_dict = FileUtils.policy_from_checkpoint(ckpt_path=args.checkpoint)
    env, _ = FileUtils.env_from_checkpoint(ckpt_dict=ckpt_dict,
                                           render=False,
                                           render_offscreen=True,
                                           verbose=True)

    # list of all demonstrations episodes
    demos = list(f["data"].keys())

    for i, ep in enumerate(demos):
        states = f["data/{}/states".format(ep)][()]
        ep_data_grp = data_grp.create_group("demo_{}".format(i))

        # load the initial state
        env.env.sim.set_state_from_flattened(states[0])
        env.env.sim.forward()

        # load the actions and play them back open-loop
        actions = np.array(f["data/{}/actions".format(ep)][()])
        num_actions = actions.shape[0]

        for j, action in enumerate(actions):
            next_obs, r, done, _ = env.env.step(action)
            
            if j < num_actions - 1:
                # ensure that the actions deterministically lead to the same recorded states
                state_playback = env.env.sim.get_state().flatten()
                if not np.all(np.equal(states[j + 1], state_playback)):
                    err = np.linalg.norm(states[j + 1] - state_playback)
                    print(f"[warning] playback diverged by {err:.2f} for ep {ep} at step {j}")

    data_writer.close()
    f.close()
