from abc import abstractmethod
from typing import Tuple

from bl.agents.ICostCalculator import ICostCalculator
from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.State import State


class IAgent(ICostCalculator):

    def __init__(self):
        self._was_terminated = False

    @abstractmethod
    def get_action(self, percepts: Tuple[State, EnvironmentConfiguration]) -> str:
        """
        Should be implemented within each agent.
        :param percepts: percepts about the environment
                         composed from current State & EnvironmentConfiguration
        :return: the next edge name
        """
        pass

    def was_terminated(self):
        return self._was_terminated
