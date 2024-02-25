from dataclasses import dataclass
from xembody.benchmark.experiment_config import ExperimentConfig
from typing import Optional
from prettytable import PrettyTable

@dataclass
class ExperimentRobotsuiteConfig(ExperimentConfig):
    """
    Used to store the configuration of the Robosuite Experiment.
    """
    source_agent_path: str
    target_agent_path: str
    
    n_rollouts: int
    
    horizon: int
    seed: int
    passive: bool
    connection: bool

    source_robot_name: str
    target_robot_name: str
    
    source_tracking_error_threshold: float
    target_tracking_error_threshold: float

    source_num_iter_max: int
    target_num_iter_max: int

    delta_action: bool
    
    # Inpaint related configuration
    enable_inpainting: bool
    use_ros: bool
    offline_eval: bool

    # Diffusion related configuration
    use_diffusion: bool
    diffusion_input_type: str

    # Optional video paths for source and target
    source_video_path: Optional[str] = None
    target_video_path: Optional[str] = None

    # Optional gripper type for source and target
    source_gripper_type: Optional[str] = None
    target_gripper_type: Optional[str] = None

    def validate(self):
        """
        Validates the configuration to see if the values are feasible.
        :throws ValueError: If the configuration is not valid.
        """
        if self.n_rollouts <= 0:
            raise ValueError("Number of rollouts should be a positive integer")

        if self.horizon <= 0:
            raise ValueError("Horizon should be a positive integer")

        if self.seed < 0:
            raise ValueError("Seed should be a non-negative integer")

        if self.source_tracking_error_threshold < 0:
            raise ValueError("Source tracking error threshold should be a non-negative float")

        if self.target_tracking_error_threshold < 0:
            raise ValueError("Target tracking error threshold should be a non-negative float")

        if self.source_num_iter_max <= 0:
            raise ValueError("Source number of iterations should be a positive integer")

        if self.target_num_iter_max <= 0:
            raise ValueError("Target number of iterations should be a positive integer")
        
        # TODO(kdharmarajan): Properly validate everything

    def __str__(self):
        table = PrettyTable()
        table.field_names = ["Parameter", "Value"]
        table.add_row(["Source Agent Path", self.source_agent_path])
        table.add_row(["Target Agent Path", self.target_agent_path])
        table.add_row(["Number of Rollouts", self.n_rollouts])
        table.add_row(["Horizon", self.horizon])
        table.add_row(["Seed", self.seed])
        table.add_row(["Passive", self.passive])
        table.add_row(["Connection", self.connection])
        table.add_row(["Source Robot Name", self.source_robot_name])
        table.add_row(["Target Robot Name", self.target_robot_name])
        table.add_row(["Source Tracking Error Threshold", self.source_tracking_error_threshold])
        table.add_row(["Target Tracking Error Threshold", self.target_tracking_error_threshold])
        table.add_row(["Source Number of Iterations", self.source_num_iter_max])
        table.add_row(["Target Number of Iterations", self.target_num_iter_max])
        table.add_row(["Delta Action", self.delta_action])
        table.add_row(["Enable Inpainting", self.enable_inpainting])
        table.add_row(["Use ROS", self.use_ros])
        table.add_row(["Offline Eval", self.offline_eval])
        table.add_row(["Use Diffusion", self.use_diffusion])
        table.add_row(["Diffusion Input Type", self.diffusion_input_type])
        table.add_row(["Source Video Path", self.source_video_path])
        table.add_row(["Target Video Path", self.target_video_path])
        table.add_row(["Source Gripper Type", self.source_gripper_type])
        table.add_row(["Target Gripper Type", self.target_gripper_type])
        return table.get_formatted_string()