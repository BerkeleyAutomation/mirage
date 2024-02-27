from omni.isaac.orbit_envs.isaac_env_cfg import IsaacEnvCfg
from omni.isaac.orbit.robots.config.franka import FRANKA_PANDA_ARM_WITH_PANDA_HAND_CFG
from omni.isaac.orbit.robots.config.universal_robots import UR5_CFG
from omni.isaac.orbit.robots.config.kinova import JACO_CFG


ROBOT_TO_CONFIG = {
    "jaco": JACO_CFG,
    "franka": FRANKA_PANDA_ARM_WITH_PANDA_HAND_CFG,
    "ur5": UR5_CFG
}

def set_robot_configuration(robot_name: str, environment_config: IsaacEnvCfg):
    if robot_name not in ROBOT_TO_CONFIG:
        raise ValueError(f"Robot name {robot_name} not supported.")
    environment_config.robot = ROBOT_TO_CONFIG[robot_name]