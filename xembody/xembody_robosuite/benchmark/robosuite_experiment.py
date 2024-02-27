import subprocess
import random
import os

from xembody_robosuite.benchmark.robosuite_experiment_config import ExperimentRobotsuiteConfig

class RobosuiteExperiment:
    """
    Used to manage the processes running in the experiments.
    """

    def __init__(self, config: ExperimentRobotsuiteConfig) -> None:
        self._config = config

        # Check for config validity
        self._config.validate()

        self._source_process = None
        self._target_process = None

    def get_config(self) -> ExperimentRobotsuiteConfig:
        """
        Returns configuration used for the experiment.
        """
        return self._config

    def launch(self) -> None:
        """
        Launches the experiment
        """
        source_agent_args = ["python3", 
                            "../policy_analysis/evaluate_policy_source_robot_server.py",
                            "--agent", self._config.source_agent_path,
                            "--n_rollouts", str(self._config.n_rollouts),
                            "--seeds", str(self._config.seed),
                            "--tracking_error_threshold", str(self._config.source_tracking_error_threshold),
                            "--num_iter_max", str(self._config.source_num_iter_max),
                            "--horizon", str(self._config.horizon),
                            "--robot_name", self._config.source_robot_name,
                            "--save_stats_path", os.path.join(self._config.results_folder, "source.txt")
                            ]
        target_agent_args = ["python3", 
                            "../policy_analysis/evaluate_policy_target_robot_server.py",
                            "--agent", self._config.target_agent_path,
                            "--n_rollouts", str(self._config.n_rollouts),
                            "--seeds", str(self._config.seed),
                            "--tracking_error_threshold", str(self._config.target_tracking_error_threshold),
                            "--num_iter_max", str(self._config.target_num_iter_max),
                            "--horizon", str(self._config.horizon),
                            "--robot_name", self._config.target_robot_name,
                            "--save_stats_path", os.path.join(self._config.results_folder, "target.txt")
                            ]
        
        if self._config.source_gripper_type:
            source_agent_args.append("--gripper_type")
            source_agent_args.append(self._config.source_gripper_type)

        if self._config.target_gripper_type:
            target_agent_args.append("--gripper_type")
            target_agent_args.append(self._config.target_gripper_type)
        
        if self._config.connection:
            source_agent_args.append("--connection")
            target_agent_args.append("--connection")

            # TODO(kdharmarajan): This is not actually guaranteed to be random, so this needs to be fixed downstream.
            random_port = random.randint(10000, 65535)
            source_agent_args.append("--port")
            source_agent_args.append(str(random_port))
            target_agent_args.append("--port")
            target_agent_args.append(str(random_port))

        if self._config.delta_action:
            target_agent_args.append("--delta_action")

        if self._config.source_video_path:
            source_agent_args.append("--video_path")
            source_agent_args.append(self._config.source_gripper_type)

        if self._config.target_video_path:
            target_agent_args.append("--video_path")
            target_agent_args.append(self._config.target_gripper_type)
        
        if self._config.enable_inpainting:
            source_agent_args.append("--inpaint_enabled")
            target_agent_args.append("--inpaint_enabled")

            if self._config.use_ros:
                source_agent_args.append("--use_ros")
                target_agent_args.append("--use_ros")

            if self._config.offline_eval:
                source_agent_args.append("--offline_eval")
                target_agent_args.append("--offline_eval")

            if self._config.use_diffusion:
                source_agent_args.append("--use_diffusion")
                target_agent_args.append("--use_diffusion")

                source_agent_args.append("--diffusion_input_type")
                source_agent_args.append(self._config.diffusion_input_type)
                target_agent_args.append("--diffusion_input_type")
                target_agent_args.append(self._config.diffusion_input_type)

        if self._config.passive:
            source_agent_args.append("--passive")

        self._source_process = subprocess.Popen(source_agent_args)
        self._target_process = subprocess.Popen(target_agent_args)

    def stop(self) -> None:
        """
        Stops the experiment
        """
        self._source_process.kill()
        self._target_process.kill()

    def get_results(self, blocking = False) -> None:
        """
        Returns the results of the experiment
        :param blocking: If True, waits for the results to be available
        """
        if blocking:
            self._source_process.wait()
            self._target_process.wait()
        with open(os.path.join(self._config.results_folder, "source.txt"), "r") as source_file:
            source_stats = source_file.read()
        with open(os.path.join(self._config.results_folder, "target.txt"), "r") as target_file:
            target_stats = target_file.read()
        return source_stats, target_stats
