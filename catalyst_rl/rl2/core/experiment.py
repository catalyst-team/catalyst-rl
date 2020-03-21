from abc import abstractmethod

from catalyst_rl.core import _Experiment
from catalyst_rl.rl2 import AlgorithmSpec, EnvironmentSpec


class RLExperiment(_Experiment):
    @property
    @abstractmethod
    def min_num_transitions(self) -> int:
        pass

    def get_algorithm(self, stage: str) -> AlgorithmSpec:
        """Returns the algorithm for a given stage"""
        pass

    def get_environment(self, stage: str) -> EnvironmentSpec:
        """Returns the environment for a given stage"""
        pass


__all__ = ["RLExperiment"]
