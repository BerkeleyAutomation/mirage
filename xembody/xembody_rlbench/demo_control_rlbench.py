import numpy as np
import os
import pickle
import time

from rlbench.backend.observation import Observation
from xembody_env import XEmbodyEnv

def execute_agent(env: XEmbodyEnv):
    training_steps = 5
    episode_length = 5
    for i in range(training_steps):
        if i % episode_length == 0:
            print('Reset Episode')
            env.reset()
        env.step()
    
class Agent(object):

    def __init__(self, action_shape):
        self.action_shape = action_shape

    def act(self, obs: Observation):
        print(obs.gripper_pose)
        arm_action = np.random.normal(0.0, 0.5, size=(self.action_shape[0] - 1,))
        gripper_action = [1.0]  # Always open
        return np.concatenate([arm_action, gripper_action], axis=-1)

class ReplayAgent(object):

    def __init__(self, action_shape, source_robot_data_dir: str):
        self.action_shape = action_shape
        self.source_robot_data_dir = source_robot_data_dir
        obs_path = os.path.join(self.source_robot_data_dir, "obs.pkl")

        # Load up the data
        with open(obs_path, 'rb') as f: 
            self.data = pickle.load(f)
            
        self.step = 0

    def get_initial_gripper_pose(self):
        return self.data[0]
    
    def act(self, obs):
        action = np.zeros(self.action_shape)
        if self.step < len(self.data):
            action = self.data[self.step]
        self.step += 1
        # gripper = [1.0]  # Always open
        # return np.concatenate([action, gripper], axis=-1)
        return action

def main():
    curr_time = time.time()
    save_dir = f'/home/lawrence/xembody/xembody/xembody_rlbench/runs/{curr_time}/source_robot'

    source_robot_env = XEmbodyEnv(
                            save_dir=save_dir 
                        )
    agent = Agent(source_robot_env._rlbench_env.action_shape)  # 6DoF + 1 for gripper        
    source_robot_env.set_agent(agent)
    execute_agent(source_robot_env)
    source_robot_env.destroy()
    
    
    save_dir_target = f'/home/lawrence/xembody/xembody/xembody_rlbench/runs/{curr_time}/target_robot'
    target_robot_env = XEmbodyEnv(
                            save_dir=save_dir_target,
                            cam_pose=source_robot_env._cam_pose,
                            task_type=source_robot_env._task_type
                        )
    agent = ReplayAgent(target_robot_env._rlbench_env.action_shape, save_dir)  # 6DoF + 1 for gripper
    target_robot_env.set_agent(agent)
    target_robot_env.set_initial_gripper_pose(agent.get_initial_gripper_pose())
    execute_agent(target_robot_env)

    print('Target Robot Execution Done')
    target_robot_env.destroy()
    
if __name__ == "__main__":
    main()