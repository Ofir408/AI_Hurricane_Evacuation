import copy
from abc import ABC
from typing import List, Tuple, Union

from heapdict import heapdict

from bl.ICostCalculator import ICostCalculator
from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.State import State
from data_structures.Vertex import Vertex
from utils.EnvironmentUtils import EnvironmentUtils


class IGeneralTreeSearch(ICostCalculator, ABC):
    NO_PATH = "No Path"

    def search(self, problem: Tuple[State, State, EnvironmentConfiguration], fringe=heapdict()) -> Union[Vertex, str]:
        initial_state, goal_state, env_conf = problem
        initial_node = self.__make_node(initial_state, env_conf)

        fringe[initial_node] = 0  # add initial node to the fringe with the best priority
        while len(fringe) > 0:
            node, _ = fringe.popitem()
            if self.__goal_test(problem, node.get_state()):
                print("goal was found!")
                fringe.clear()
                return node
            for edge_name, vertex in self.__successor_func(node, env_conf):
                fringe[vertex] = vertex.get_cost()
        return IGeneralTreeSearch.NO_PATH

    def restore_solution(self, goal_node: Vertex) -> Tuple[List, int]:
        vertexes_path = []
        current_node = goal_node
        while current_node is not None:
            vertexes_path.append(copy.deepcopy(current_node))
            current_node = current_node.get_parent_vertex()
        vertexes_path.reverse()
        return vertexes_path, goal_node.get_cost()

    def __expand(self, node: Vertex, env_conf: EnvironmentConfiguration) -> List[Vertex]:
        successors = []
        for _, result in self.__successor_func(node, env_conf):
            successors.append(result)
        return successors

    def __successor_func(self, node: Vertex, env_conf: EnvironmentConfiguration) -> List[Tuple[str, Vertex]]:
        current_state = node.get_state()
        edges_list = EnvironmentUtils.get_possible_moves(current_state, env_conf)
        names_of_edges = [edge.get_edge_name() for edge in edges_list]
        edge_to_next_state_list = []
        for edge_name in names_of_edges:
            next_vertex = EnvironmentUtils.get_next_vertex(current_state, edge_name, self.step_cost, env_conf)
            env_conf.get_vertexes()[next_vertex.get_vertex_name()] = next_vertex
            edge_to_next_state_list.append((edge_name, next_vertex))
        return edge_to_next_state_list

    def __goal_test(self, problem: Tuple[State, State, EnvironmentConfiguration], current_state: State):
        _, goal_state, _ = problem
        return goal_state == current_state

    def __make_node(self, state: State, env_conf: EnvironmentConfiguration):
        name = state.get_current_vertex_name()
        return env_conf.get_vertexes()[name]
