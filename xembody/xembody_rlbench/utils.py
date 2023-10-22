import glob
import os

from rlbench.action_modes.arm_action_modes import \
    JointVelocity, JointPosition, JointTorque, EndEffectorPoseViaIK, EndEffectorPoseViaPlanning
from rlbench.const import SUPPORTED_ROBOTS
from rlbench.backend.utils import task_file_to_task_class

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
    mode_choice = input("Action mode selection: ")
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


def get_tasks(task_dir):
    possible_tasks = glob.glob(f"{task_dir}/*.py")
    task_map = {}
    for task in possible_tasks:
        core_name = os.path.basename(task)
        if core_name == "__init__.py":
            continue
        task_class = task_file_to_task_class(core_name)
        task_name = core_name.replace(".py", "")
        task_map[task_name] = task_class
        
    return task_map
    
TASKS = get_tasks("/home/lawrence/xembody/RLBench/rlbench/tasks")

def select_task():
    possible_task_names = list(TASKS.keys())
    for i in range(len(possible_task_names)):
        print(f"[{i}]: {possible_task_names[i]}")
    task_choice = input("Task selection: ")
    task_choice_index = int(task_choice)
    return TASKS[possible_task_names[task_choice_index]]