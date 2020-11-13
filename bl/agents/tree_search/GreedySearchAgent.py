from typing import Tuple

from bl.agents.tree_search.IGeneralTreeSearch import IGeneralTreeSearch
from bl.agents.tree_search.heuristic_functions.IHueristicFunc import IHueristicFunc
from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.Edge import Edge
from data_structures.State import State
from data_structures.Vertex import Vertex


class GreedySearchAgent(IGeneralTreeSearch):

    def __init__(self, heuristic_func: IHueristicFunc):
        super().__init__()
        self.__heuristic_func = heuristic_func

    def step_cost(self, parent_node: Vertex, action: Edge, new_node: Vertex) -> int:
        return self.__heuristic_func.calc_estimation_from_goal(new_node.get_state(), None)

    def _goal_test(self, problem: Tuple[State, State, EnvironmentConfiguration], current_state: State):
        _, goal_state, _ = problem
        return goal_state.get_required_vertexes() == current_state.get_required_vertexes()
