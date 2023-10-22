import numpy as np
import os
import pickle
import time
import imageio

from pyrep.objects.dummy import Dummy
from pyrep.objects.vision_sensor import VisionSensor

from rlbench.action_modes.action_mode import MoveArmThenGripper
from rlbench.action_modes.arm_action_modes import JointVelocity, JointPosition, JointTorque, EndEffectorPoseViaIK, EndEffectorPoseViaPlanning
from rlbench.action_modes.gripper_action_modes import Discrete
from rlbench.environment import Environment
from rlbench.observation_config import ObservationConfig
from rlbench.tasks import PutRubbishInBin
from rlbench.task_environment import TaskEnvironment
from rlbench.const import SUPPORTED_ROBOTS

from rlbench.backend.observation import Observation

class TaskRecorder(object):

    def __init__(self, env: Environment, cam: VisionSensor, fps=30, save_dir=None):
        self._env = env
        self._fps = fps
        self._cam = cam
        self._snaps = []
        self._obs = []
        self._current_snaps = []
        self._save_dir = save_dir

    def take_snap(self, obs: Observation):
        self._current_snaps.append(
            (self._cam.capture_rgb() * 255.).astype(np.uint8))
        self._obs.append(obs.gripper_pose)

    def save(self, path=None):
        """
        Args:
            path str: path to directory that will store the data
        """
        print('Converting to video ...')
        if self._save_dir:
            path = self._save_dir
        os.makedirs(path, exist_ok=True)
        
        video_path = os.path.join(path, "video.mp4")
        obs_path = os.path.join(path, "obs.pkl")
        # OpenCV QT version can conflict with PyRep, so import here
        # import cv2
        # video = cv2.VideoWriter(
        #         video_path, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), self._fps,
        #         tuple(self._cam.get_resolution()))
        print(f'Saving video to {video_path}')
        writer = imageio.get_writer(video_path, fps=self._fps)
        for image in self._current_snaps:
            writer.append_data(image)
        writer.close()
        self._current_snaps = []
        with open(obs_path, "wb") as f:
            pickle.dump(self._obs, f)
        self._obs = []

def select_robot_to_use():
    possible_robots = list(SUPPORTED_ROBOTS.keys())
    for i in range(len(possible_robots)):
        print(f"[{i}]: {possible_robots[i]}")
    robot_choice = input("Robot selection: ")
    robot_choice_index = int(robot_choice)
    return possible_robots[robot_choice_index]

ARM_ACTION_MODES = {
    'joint_velocity': JointVelocity,
    'joint_position': JointPosition,
    'joint_torque': JointTorque,
    'planner': EndEffectorPoseViaPlanning,
    'ik': EndEffectorPoseViaIK
}

def select_action_mode_arm():
    possible_modes = list(ARM_ACTION_MODES.keys())
    for i in range(len(possible_modes)):
        print(f"[{i}]: {possible_modes[i]}")
    mode_choice = input("Robot selection: ")
    mode_choice_index = int(mode_choice)
    if mode_choice_index in {0, 2}:
        return ARM_ACTION_MODES[possible_modes[mode_choice_index]]()
    else:
        absolute_mode = input("Absolute mode? (y/n): ")
        if absolute_mode in {'y', 'Y'}:
            absolute_mode = True
        else:
            absolute_mode = False
        return ARM_ACTION_MODES[possible_modes[mode_choice_index]](absolute_mode=absolute_mode)


def setup_robot_environment():
    obs_config = ObservationConfig()
    obs_config.set_all(True)
    obs_config.gripper_touch_forces = False
    
    robot_type = select_robot_to_use()
    arm_action_mode = select_action_mode_arm()
    
    action_mode = MoveArmThenGripper(
        arm_action_mode=arm_action_mode, gripper_action_mode=Discrete())
    env = Environment(
        action_mode, obs_config=obs_config, headless=False,
        robot_setup=robot_type)
    env.launch()
    return env

def execute_agent(agent, task: TaskEnvironment, task_recorder: TaskRecorder):
    training_steps = 20
    episode_length = 20
    obs = None
    # import pdb; pdb.set_trace()
    for i in range(training_steps):
        if i % episode_length == 0:
            try:
                descriptions, obs = task.reset()
                task._task.robot.arm.set_joint_positions([0,0,0,0,0,], disable_dynamics=True)
                print(task._task.robot.arm.get_joint_positions())
            except:
                print("Failed to reset task")
            # print(descriptions)
        task_recorder.take_snap(obs)
        print("##############################################")
        print("Robot joints: ", obs.joint_positions) # task._task.robot.arm.get_joint_positions(), task._scene.get_observation().joint_positions
        print("Gripper pose: ", obs.gripper_pose) # task._scene.get_observation().gripper_pose
        print("IK joints", task._task.robot.arm.solve_ik_via_jacobian(position=obs.gripper_pose[:3], quaternion=obs.gripper_pose[3:]))
        action = agent.act(obs)
        # action = [-0.01,-0.01,0.02,1,0,0,1, 1]
        print("Action:", action)
        obs, reward, terminate = task.step(action)
        # print("Gripper pose: ", obs.gripper_pose) # task._scene.get_observation().gripper_pose
    task_recorder.save()
    
class Agent(object):

    def __init__(self, action_shape):
        self.action_shape = action_shape

    def act(self, obs: Observation):
        # print("Gripper pose: ", obs.gripper_pose)
        arm = np.random.normal(0.0, 0.5, size=(self.action_shape[0] - 1,))
        gripper = [1.0]  # Always open
        return np.concatenate([arm, gripper], axis=-1)

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
        # breakpoint()
        action = np.zeros(self.action_shape)
        if self.step < len(self.data):
            action = self.data[self.step]
        self.step += 1
        gripper = [1.0]  # Always open
        return np.concatenate([action, gripper], axis=-1)

def main():
    source_robot_env = setup_robot_environment()
    task = source_robot_env.get_task(PutRubbishInBin)
    agent = Agent(source_robot_env.action_shape)  # 6DoF + 1 for gripper
    
    cam_placeholder = Dummy('cam_cinematic_placeholder')
    cam = VisionSensor.create([1280, 720])
    cam.set_pose(cam_placeholder.get_pose())
    cam.set_parent(cam_placeholder)
    
    curr_time = time.time()
    save_dir = f'/home/lawrence/xembody/RLBench/collected_data/{curr_time}/source_robot'
    tr = TaskRecorder(source_robot_env, cam, fps=30, save_dir=save_dir)
    execute_agent(agent, task, tr)

    print('Source Robot Execution Done')
    source_robot_env.shutdown()
    
    target_robot_env = setup_robot_environment()
    task = target_robot_env.get_task(PutRubbishInBin)
    agent = ReplayAgent(target_robot_env.action_shape, save_dir)  # 6DoF + 1 for gripper
    initial_gripper_pose = agent.get_initial_gripper_pose()
    joint_angles = task._task.robot.arm.solve_ik_via_jacobian(position=initial_gripper_pose[:3], quaternion=initial_gripper_pose[3:])
    task._task.robot.arm.set_joint_positions(joint_angles, disable_dynamics=True)
    
    cam_placeholder = Dummy('cam_cinematic_placeholder')
    cam = VisionSensor.create([1280, 720])
    cam.set_pose(cam_placeholder.get_pose())
    cam.set_parent(cam_placeholder)
    
    save_dir_target = f'/home/lawrence/xembody/RLBench/collected_data/{curr_time}/target_robot'
    tr = TaskRecorder(target_robot_env, cam, fps=30, save_dir=save_dir_target)
    
    execute_agent(agent, task, tr)

    print('Target Robot Execution Done')
    target_robot_env.shutdown()
    
if __name__ == "__main__":
    main()