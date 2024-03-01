import numpy as np
from collections import deque

class FrameStackWrapper:
    """
    Copied from R2D2 repo for Robomimic policies
    Wrapper for frame stacking observations during rollouts. The agent
    receives a sequence of past observations instead of a single observation
    when it calls @env.reset, @env.reset_to, or @env.step in the rollout loop.
    """
    def __init__(self, num_frames):
        """
        Args:
            env (EnvBase instance): The environment to wrap.
            num_frames (int): number of past observations (including current observation)
                to stack together. Must be greater than 1 (otherwise this wrapper would
                be a no-op).
        """
        self.num_frames = num_frames

        ### TODO: add action padding option + adding action to obs to include action history in obs ###

        # keep track of last @num_frames observations for each obs key
        self.obs_history = None

    def _set_initial_obs_history(self, init_obs):
        """
        Helper method to get observation history from the initial observation, by
        repeating it.

        Returns:
            obs_history (dict): a deque for each observation key, with an extra
                leading dimension of 1 for each key (for easy concatenation later)
        """
        self.obs_history = {}
        for k in init_obs:
            self.obs_history[k] = deque(
                [init_obs[k][None] for _ in range(self.num_frames)], 
                maxlen=self.num_frames,
            )

    def reset(self):
        self.obs_history = None

    def get_obs_history(self):
        """
        Helper method to convert internal variable @self.obs_history to a 
        stacked observation where each key is a numpy array with leading dimension
        @self.num_frames.
        """
        # concatenate all frames per key so we return a numpy array per key
        if self.num_frames == 1:
            return { k : np.concatenate(self.obs_history[k], axis=0)[0] for k in self.obs_history }
        else:
            return { k : np.concatenate(self.obs_history[k], axis=0) for k in self.obs_history }

    def add_obs(self, obs):
        if self.obs_history is None:
            self._set_initial_obs_history(obs)

        # update frame history
        for k in obs:
            # make sure to have leading dim of 1 for easy concatenation
            self.obs_history[k].append(obs[k][None])
