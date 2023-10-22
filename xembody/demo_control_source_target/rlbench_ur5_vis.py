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
    return ARM_ACTION_MODES[possible_modes[mode_choice_index]]()


def setup_robot_environment():
    obs_config = ObservationConfig()
    obs_config.set_all(True)
    obs_config.gripper_touch_forces = False
    
    robot_type = select_robot_to_use()
    arm_action_mode = select_action_mode_arm()
    
    action_mode = MoveArmThenGripper(
        arm_action_mode=arm_action_mode, gripper_action_mode=Discrete())
    env = Environment(
        action_mode, obs_config=obs_config, headless=True,
        robot_setup=robot_type)
    env.launch()
    return env

def execute_agent(agent, task: TaskEnvironment, task_recorder: TaskRecorder):
    training_steps = 10000
    episode_length = 10000
    obs = None
    # import pdb; pdb.set_trace()
    try:
        descriptions, obs = task.reset()
        task._task.robot.arm.set_joint_positions([-1.57, 1.57, 0, 1.57, 0, 0], disable_dynamics=True)
    except Exception as e:
        print(e)
        print("Failed to reset task")
    # print(descriptions)
    print(task._task.robot.arm.get_joint_positions())
    while True:
        from tracikpy import TracIKSolver
        import robosuite.utils.transform_utils as T
        ik_solver = TracIKSolver(
                "/home/lawrence/Downloads/ur5_4/ur5.urdf",
                "robot_base",
                "UR5link3",
            )
        received_joints = task._task.robot.arm.get_joint_positions()
        print("URDF FK: ", T.mat2pose(ik_solver.fk(received_joints[:2])))
        print("Robot joints: ", received_joints) # task._task.robot.arm.get_joint_positions(), task._scene.get_observation().joint_positions
        print("Gripper pose: ", task._scene.get_observation().gripper_pose) # task._scene.get_observation().gripper_pose
        task.step([0,0,0,0,0,0,1])

    task_recorder.take_snap(obs)
    # input("Press Enter to continue...")
    # task_recorder.save()
    
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

    def act(self, obs):
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
    # source_robot_env.shutdown()
    # while True:
    #     pass
    
if __name__ == "__main__":
    main()