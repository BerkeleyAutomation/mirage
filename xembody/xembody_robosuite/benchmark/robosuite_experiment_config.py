from dataclasses import dataclass
from xembody.benchmark.experiment_config import ExperimentConfig
from typing import Optional

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