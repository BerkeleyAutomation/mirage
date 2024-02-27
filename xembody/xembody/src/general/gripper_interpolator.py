import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from typing import List

class GripperInterpolator:
    """
    Interpolates the gripper angles given the current robot gripper angles
    """

    GRIPPER_TYPE_TO_ROBOT_MAPPING = {
        "PandaGripper": "Panda",
        "Robotiq85Gripper": "UR5e",
        "Robotiq140Gripper": "IIWA"
    }
    
    def __init__(self, 
                 source_info: str, 
                 target_info: str,
                 interpolations_files: List[str] = []
                 ):
        """
        Initializes the gripper interpolator
        """
        self.source_robot = source_info
        self.target_robot = target_info

        if source_info in GripperInterpolator.GRIPPER_TYPE_TO_ROBOT_MAPPING:
            self.source_robot = GripperInterpolator.GRIPPER_TYPE_TO_ROBOT_MAPPING[source_info]

        if target_info in GripperInterpolator.GRIPPER_TYPE_TO_ROBOT_MAPPING:
            self.target_robot =  GripperInterpolator.GRIPPER_TYPE_TO_ROBOT_MAPPING[target_info]

        self.interpolators = {}
        for interpolation_file in interpolations_files:
            with open(interpolation_file, "rb") as f:
                task_specific_interpolators = pickle.load(f)
                print(task_specific_interpolators)
                for interpolator_key, coefficients in task_specific_interpolators.items():
                    print(interpolator_key)
                    self.interpolators[(interpolator_key[0], interpolator_key[1])] = coefficients

    
    def interpolate_gripper(self, gripper_angles: np.array) -> np.array:
        """
        Interpolates gripper angles

        Args:
            gripper_angles (np.array): gripper angles of the source robot
        """
        if self.source_robot == self.target_robot:
            print("Returning angles")
            return 1 * gripper_angles
        
        relevant_interpoolator = self.interpolators[(self.source_robot, self.target_robot)]
        regression_model = LinearRegression()


        regression_model.coef_ = relevant_interpoolator["coef"]
        regression_model.intercept_ = relevant_interpoolator["intercept"]

        return regression_model.predict(gripper_angles.reshape(1, -1)).flatten()