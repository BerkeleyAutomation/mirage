from xembody.xembody_robosuite.benchmark.robosuite_experiment_config import ExperimentRobotsuiteConfig

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
        pass

    def stop(self) -> None:
        """
        Stops the experiment
        """
        pass

    def get_results(self, blocking = False) -> None:
        """
        Returns the results of the experiment
        :param blocking: If True, waits for the results to be available
        """
        pass