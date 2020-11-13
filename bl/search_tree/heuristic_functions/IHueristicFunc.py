from abc import ABC, abstractmethod

from data_structures.State import State


class IHueristicFunc(ABC):

    @abstractmethod
    def calc_estimation_from_goal(self, current_state: State, goal_state: State):
        """

        :param current_state: the current state to estimate the heuristic from.
        :param goal_state: the goal state of the problem.
        :return: a number that represents the estimation from the current state to the goal state.
        """
        pass
