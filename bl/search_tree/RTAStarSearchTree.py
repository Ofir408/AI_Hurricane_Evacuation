import copy
from typing import Tuple, List

from bl.search_tree.AStarSearchTree import AStarSearchTree
from bl.search_tree.IGeneralSearchTree import IGeneralSearchTree
from bl.search_tree.heuristic_functions.IHueristicFunc import IHueristicFunc
from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.Edge import Edge
from data_structures.State import State
from data_structures.Vertex import Vertex


class RTAStarSearchTree(IGeneralSearchTree):

    def __init__(self, heuristic_func: IHueristicFunc, limit: int = 10):
        super().__init__()
        self.__heuristic_func = heuristic_func
        self.__limit = limit

    def search(self, problem: Tuple[State, State, EnvironmentConfiguration], fringe: List):
        backup_problem = copy.deepcopy(problem)
        initial_state, goal_state, env_conf = backup_problem
        result = None
        was_solution_found = IGeneralSearchTree.SOLUTION_NOT_FOUND
        path = []
        while not self._was_terminate:
            search_algo = AStarSearchTree(self.__heuristic_func, self.__limit)
            temp, was_solution_found = search_algo.search(backup_problem, [])
            path.append(temp)
            if result is None:
                result = copy.deepcopy(temp)
            temp.set_parent_vertex(result.get_parent_vertex())
            result.set_parent_vertex(copy.deepcopy(temp))
            backup_problem = (temp.get_state(), goal_state, env_conf)
            if was_solution_found == IGeneralSearchTree.SOLUTION_FOUND:
                self._was_terminate = True
        return path[len(path)-1], was_solution_found

    def goal_test(self, problem: Tuple[State, State, EnvironmentConfiguration], current_state: State):
        _, goal_state, _ = problem
        return goal_state.get_required_vertexes() == current_state.get_required_vertexes()

    def step_cost(self, parent_node: Vertex, action: Edge, new_node: Vertex) -> int:
        g_value = action.get_weight()  # weights until g was calculated within get_next_vertex
        h_value = self.__heuristic_func.calc_estimation_from_goal(new_node.get_state(), None)
        return g_value + h_value
