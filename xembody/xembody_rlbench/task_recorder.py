import numpy as np
import os
import imageio
import pickle
import logging

from pyrep.objects.vision_sensor import VisionSensor
from rlbench.environment import Environment
from rlbench.backend.observation import Observation

class TaskRecorder(object):

    def __init__(self, env: Environment, cam: VisionSensor, fps=30, save_dir=None, logger=None):
        self._env = env
        self._fps = fps
        self._cam = cam
        self._snaps = []
        self._obs = []
        self._current_snaps = []
        self._save_dir = save_dir
        self._logger = logger if logger else logging.getLogger()

    def take_snap(self, obs: Observation):
        self._logger.debug("Task recorder wrote an observation.")
        self._current_snaps.append(
            (self._cam.capture_rgb() * 255.).astype(np.uint8))
        self._obs.append(obs.gripper_pose)

    def save(self, path=None):
        """
        Args:
            path str: path to directory that will store the data
        """
        self._logger.debug('Converting to video ...')
        if self._save_dir:
            path = self._save_dir
        os.makedirs(path, exist_ok=True)
        
        video_path = os.path.join(path, "video.mp4")
        obs_path = os.path.join(path, "obs.pkl")
        self._logger.info(f'Saving video to {video_path}')
        writer = imageio.get_writer(video_path, fps=self._fps)
        for image in self._current_snaps:
            writer.append_data(image)
        writer.close()
        self._current_snaps = []
        with open(obs_path, "wb") as f:
            pickle.dump(self._obs, f)
        self._obs = []
