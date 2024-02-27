from abc import ABC, abstractmethod

class ExperimentConfig(ABC):

    @abstractmethod
    def validate_config(self):
        """
        Validate the configuration to see if the values are feasible.
        :throws ValueError: If the configuration is not valid.
        """
        pass