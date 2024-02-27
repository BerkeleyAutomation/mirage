from typing import Type

from pyrep.objects.dummy import Dummy
from pyrep.objects.vision_sensor import VisionSensor

from rlbench.action_modes.action_mode import ArmActionMode, MoveArmThenGripper
from rlbench.action_modes.gripper_action_modes import Discrete
from rlbench.environment import Environment
from rlbench.backend.task import Task
from rlbench.observation_config import ObservationConfig
from rlbench.tasks import PutRubbishInBin

from utils import select_robot_to_use, select_action_mode_arm, select_task
from task_recorder import TaskRecorder

class XEmbodyEnv(object):
    
    def __init__(self, 
                 save_dir: str,
                 agent = None,
                 robot_type: str = None, 
                 arm_action_mode: ArmActionMode = None, 
                 task_type: Type[Task] = PutRubbishInBin,
                 headless: bool = False,
                 cam_pose = None
                 ):
        self._save_dir = save_dir
        self._agent = agent
        
        self._robot_type = robot_type if robot_type else select_robot_to_use()
        self._arm_action_mode = arm_action_mode if arm_action_mode else select_action_mode_arm()
        self._task_type = task_type if task_type else select_task()
        
        obs_config = ObservationConfig()
        obs_config.set_all(True)
        obs_config.gripper_touch_forces = False
        
        self._action_mode = MoveArmThenGripper(
            arm_action_mode=self._arm_action_mode, gripper_action_mode=Discrete()
        )
                
        self._rlbench_env = Environment(
            self._action_mode, obs_config=obs_config, headless=headless, robot_setup=self._robot_type
        )
        self._rlbench_env.launch()
        
        self._cam_placeholder = Dummy('cam_cinematic_placeholder')
        self._cam_pose = cam_pose if cam_pose is not None else self._cam_placeholder.get_pose()
        
        self.setup_task_recorder(self._cam_pose)
        self._task = self._rlbench_env.get_task(self._task_type)
        
        self._obs = None
        
    def setup_task_recorder(self, cam_pose):
        self._cam = VisionSensor.create([1280, 720])
        self._cam.set_pose(cam_pose)
        self._recorder = TaskRecorder(self._rlbench_env, self._cam, fps=20, save_dir=self._save_dir)
        
    def set_agent(self, agent):
        self._agent = agent
        
    def set_initial_gripper_pose(self, pose):
        # set initial position
        # breakpoint()
        joint_angles = self._task._task.robot.arm.solve_ik_via_jacobian(position=pose[:3], quaternion=pose[3:])
        self._task._task.robot.arm.set_joint_positions(joint_angles, disable_dynamics=True)
        
    def step(self):
        action = self._agent.act(self._obs)
        self._obs, reward, terminate = self._task.step(action)
        
        print("Robot joints: ", self._obs.joint_positions) # task._task.robot.arm.get_joint_positions(), task._scene.get_observation().joint_positions
        print("Gripper pose: ", self._obs.gripper_pose) # task._scene.get_observation().gripper_pose
        print("IK joints", self._task._task.robot.arm.solve_ik_via_jacobian(position=self._obs.gripper_pose[:3], quaternion=self._obs.gripper_pose[3:]))
        
        self._recorder.take_snap(self._obs)
        
    def reset(self):
        try:
            descriptions, self._obs = self._task.reset()
        except:
            print("Failed to reset task")
        self._recorder.take_snap(self._obs)
        
    def destroy(self):
        self._recorder.save()
        self._rlbench_env.shutdown()
