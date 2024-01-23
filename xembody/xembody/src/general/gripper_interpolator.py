import numpy as np
import pickle
from sklearn.linear_model import LinearRegression

class GripperInterpolator:
    """
    Interpolates the gripper angles given the current robot gripper angles
    """
    
    def __init__(self, 
                 source_robot_type: str, 
                 target_robot_type: str,
                 interpolations_file: str = None
                 ):
        """
        Initializes the gripper interpolator
        """
        self.source_robot_type = source_robot_type
        self.target_robot_type = target_robot_type

        self.interpolators = {}
        if interpolations_file:
            with open(interpolations_file, "rb") as f:
                self.interpolators = pickle.load(f)
    
    def interpolate_gripper(self, gripper_angles: np.array) -> np.array:
        """
        Interpolates gripper angles

        Args:
            gripper_angles (np.array): gripper angles of the source robot
        """
        if self.source_robot_type == self.target_robot_type:
            return gripper_angles
        
        relevant_interpoolator = self.interpolators[(self.source_robot_type, self.target_robot_type)]
        regression_model = LinearRegression()
        regression_model.coef_ = relevant_interpoolator["coef_"]
        regression_model.intercept_ = relevant_interpoolator["intercept_"]

        return regression_model.predict(gripper_angles.reshape(1, -1)).flatten()

        # TODO: add this for real gripper mapping
        return -0.05702400673569841 * gripper_angles + 0.02670973458948458
        