from abc import ABC, abstractmethod

from data_structures.Vertex import Vertex


class IAgent(ABC):

    _was_terminated = False

    @abstractmethod
    def get_action(self, percepts) -> Vertex:
        """
        Should be implemented within each agent.
        :param percepts: percepts about the environment
                         composed from current State & EnvironmentConfiguration
        :return: the next Vertex
        """
        pass

    def was_terminated(self):
        return self._was_terminated
