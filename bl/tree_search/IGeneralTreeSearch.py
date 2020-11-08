import copy
from abc import ABC
from operator import itemgetter
from typing import List, Tuple, Union

from bl.ICostCalculator import ICostCalculator
from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.State import State
from data_structures.Vertex import Vertex
from utils.EnvironmentUtils import EnvironmentUtils


class IGeneralTreeSearch(ICostCalculator, ABC):
    NO_PATH = "No Path"

    def search(self, problem: Tuple[State, State, EnvironmentConfiguration], fringe: List) -> Union[Vertex, str]:
        initial_state, goal_state, env_conf = problem
        backup_env_conf = copy.deepcopy(env_conf)

        initial_node = self.__make_node(initial_state, backup_env_conf)

        self.__insert_to_fringe(fringe, initial_node, 0)
        while len(fringe) > 0:
            node, _ = self.__pop_from_fringe(fringe)
            if self.__goal_test(problem, node.get_state()):
                print("goal was found!")
                fringe.clear()
                return node
            for edge_name, vertex in self.__successor_func(node, backup_env_conf):
                self.__insert_to_fringe(fringe, vertex, vertex.get_cost())
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
            next_vertex_current_cost = env_conf.get_vertexes()[next_vertex.get_vertex_name()].get_cost()
            if next_vertex_current_cost == 0 or next_vertex.get_cost() < next_vertex_current_cost:
                env_conf.get_vertexes()[next_vertex.get_vertex_name()] = next_vertex
            edge_to_next_state_list.append((edge_name, next_vertex))
        return edge_to_next_state_list

    def __goal_test(self, problem: Tuple[State, State, EnvironmentConfiguration], current_state: State):
        _, goal_state, _ = problem
        return goal_state == current_state

    def __make_node(self, state: State, env_conf: EnvironmentConfiguration):
        name = state.get_current_vertex_name()
        return env_conf.get_vertexes()[name]

    def __insert_to_fringe(self, fringe: List, key, priority):
        to_insert = True
        for k, _ in fringe:
            if key == k:
                to_insert = False
        if to_insert:
            fringe.append((key, priority))

    def __pop_from_fringe(self, fringe: List):
        fringe.sort(key=itemgetter(1)) # todo: add sort by ab-order
        top_element = fringe[0]
        fringe.remove(top_element)
        return top_element
