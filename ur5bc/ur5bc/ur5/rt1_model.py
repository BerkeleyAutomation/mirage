from tf_agents.trajectories import time_step as ts
from tf_agents.policies import py_tf_eager_policy
import tf_agents

import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

import os
import pickle
import numpy as np
from pathlib import Path

import matplotlib.pyplot as plt
from PIL import Image

from collections import defaultdict


saved_model_path = '/home/lawrence/robotlerf/ur5bc/berkeley_ur5/xid_58975173/000631960'
saved_model_path = '/home/lawrence/robotlerf/ur5bc/berkeley_ur5/xid_59180571/000568960'

task = 'Take the tiger out of the red bowl and put it in the grey bowl.'

class RT1Model:
    def __init__(self, model_path):
        print("Loading model ...")
        self.tfa_policy = py_tf_eager_policy.SavedModelPyTFEagerPolicy(
            model_path=model_path,
            load_specs_from_pbtxt=True,
            use_tf_function=True)

        self.observation = {
            'image':
                np.zeros(shape=(256, 320, 3), dtype=np.uint8),
            'natural_language_embedding':
                np.zeros(shape=(512), dtype=np.float32),
            'gripper_closed':
                np.zeros(shape=(1), dtype=np.float32),
            'height_to_bottom':
                np.zeros(shape=(1), dtype=np.float32),
            'base_pose_tool_reached':
                np.zeros(shape=(7), dtype=np.float32),
            'workspace_bounds':
                np.zeros(shape=(3, 3), dtype=np.float32),
            'orientation_box':
                np.zeros(shape=(2, 3), dtype=np.float32),
            'orientation_start':
                np.zeros(shape=(4), dtype=np.float32),
            'src_rotation':
                np.zeros(shape=(4), dtype=np.float32),
            'robot_orientation_positions_box':
                np.zeros(shape=(3, 3), dtype=np.float32),
            'natural_language_instruction':
                np.zeros(shape=(), dtype=str),
            'vector_to_go':
                np.zeros(shape=(3), dtype=np.float32),
            'rotation_delta_to_go':
                np.zeros(shape=(3), dtype=np.float32),
            'gripper_closedness_commanded':
                np.zeros(shape=(1), dtype=np.float32),
        }


        self.observation = tf_agents.specs.zero_spec_nest(
            tf_agents.specs.from_spec(self.tfa_policy.time_step_spec.observation))
        self.observation = tf.nest.map_structure(lambda x: x.numpy(), self.observation)

        tfa_time_step = ts.transition(self.observation, reward=np.zeros(()))
        

        # sanity check
        self.policy_state = self.tfa_policy.get_initial_state(batch_size=1)
        action = self.tfa_policy.action(tfa_time_step, self.policy_state)

        self.reset()
        print("Finished initializing the model.")

    def reset(self):
        self.policy_state = self.tfa_policy.get_initial_state(batch_size=1)



    def _normalize_task_name(self, task_name):

        replaced = task_name.replace('_', ' ').replace('1f', ' ').replace(
            '4f', ' ').replace('-', ' ').replace('50',
                                                ' ').replace('55',
                                                                ' ').replace('56', ' ')
        return replaced.lstrip(' ').rstrip(' ')

    def compute_embedding(self, task_name):
        print("Computing embedding ...")
        # Load language model and embed the task string
        # embed = hub.load('https://tfhub.dev/google/universal-sentence-encoder-large/5')
        embed = hub.load('.') # see the top answer: https://stackoverflow.com/questions/62674772/how-to-use-tf-hub-models-locally
        print("Finished loading language model.")
        return embed([self._normalize_task_name(task_name)])[0]



    def predict_action(self, image, natural_language_embedding, scale_model_output=False):
        # images: (480, 640, 3) with values in [0, 255]

        # Run inference to obtain predicted actions for each image in the episode
        # The input to the model is the image and natural_language_embedding.
        image = Image.fromarray(np.uint8(image))
        image = tf.image.resize_with_pad(image, target_width=320, target_height=256)
        image = tf.cast(image, np.uint8)

        self.observation['image'] = image.numpy()
        self.observation['natural_language_embedding'] = natural_language_embedding

        tfa_time_step = ts.transition(self.observation, reward=np.zeros(()))

        policy_step = self.tfa_policy.action(tfa_time_step, self.policy_state)
        action = policy_step.action
        self.policy_state = policy_step.state
        if not scale_model_output:
            return np.concatenate((action['world_vector'], action['rotation_delta'], action['gripper_closedness_action'], action['terminate_episode'][:1]))
        else:
            return np.concatenate((action['world_vector']/100, action['rotation_delta']/15, action['gripper_closedness_action'], action['terminate_episode'][:1]))
