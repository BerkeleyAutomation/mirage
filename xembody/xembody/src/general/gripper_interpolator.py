import numpy as np

class GripperInterpolator:
    """
    Interpolates the gripper angles given the current robot gripper angles
    """
    
    def __init__(self, source_robot_type: str, target_robot_type: str):
        """
        Initializes the gripper interpolator
        """
        self.source_robot_type = source_robot_type
        self.target_robot_type = target_robot_type
    
    def interpolate_gripper(self, gripper_angles: np.array) -> np.array:
        """
        Interpolates gripper angles

        Args:
            gripper_angles (np.array): gripper angles of the source robot
        """
        # TODO: extend to other robots
        return -0.05702400673569841 * gripper_angles + 0.02670973458948458
        