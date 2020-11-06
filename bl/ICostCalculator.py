from abc import ABC, abstractmethod

from data_structures.Edge import Edge
from data_structures.Vertex import Vertex


class ICostCalculator(ABC):

    @abstractmethod
    def step_cost(self, parent_node: Vertex, action: Edge, new_node: Vertex) -> int:
        """

        :param parent_node: the parent node
        :param action: required action to move from parent node to the new node
        :param new_node: the new node
        :return: the step cost to move from parent vertex to the new node
        """
        pass
