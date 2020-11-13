import copy
from abc import ABC
from typing import List, Tuple

from bl.agents.ICostCalculator import ICostCalculator
from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.State import State
from data_structures.Vertex import Vertex
from utils.EnvironmentUtils import EnvironmentUtils


class IGeneralSearchTree(ICostCalculator, ABC):
    SOLUTION_NOT_FOUND = "No Path"
    SOLUTION_FOUND = "Solution found"

    def __init__(self):
        self._expansions_num = 0
        self._was_terminate = False

    def search(self, problem: Tuple[State, State, EnvironmentConfiguration], fringe: List):
        initial_state, goal_state, env_conf = problem
        backup_env_conf = copy.deepcopy(env_conf)
        initial_node = self.__make_node(initial_state, backup_env_conf)
        self.__insert_to_fringe(fringe, initial_node, 0)
        last_node = copy.deepcopy(initial_node)
        self._was_terminate = False
        self._expansions_num = 0
        while len(fringe) > 0 and not self._was_terminate:
            node, _ = self.__pop_from_fringe(fringe)
            last_node = node
            if self.goal_test(problem, node.get_state()):
                print("goal was found!")
                print("Expansions num: ", self._expansions_num)
                fringe.clear()
                return node, IGeneralSearchTree.SOLUTION_FOUND
            for edge_name, vertex in sorted(self.__successor_func(node, backup_env_conf)):
                self.__insert_to_fringe(fringe, vertex, vertex.get_cost())
        print("last_node: ", last_node.get_vertex_name())
        return last_node, IGeneralSearchTree.SOLUTION_NOT_FOUND

    def restore_solution(self, goal_node: Vertex, env_conf: EnvironmentConfiguration) -> Tuple[List, int]:
        vertexes_path = []
        current_node = goal_node
        edges = env_conf.get_edges()
        edges_of_path = []
        cost = 0
        while current_node is not None:
            edges_of_path += current_node.get_action() if current_node.get_action() is not None else ""
            vertexes_path.append(copy.deepcopy(current_node))
            current_node = current_node.get_parent_vertex()
        vertexes_path.reverse()

        # calculate the cost to the solution
        for edge_name in filter(None, edges_of_path):
            cost += edges[edge_name].get_weight()
        return vertexes_path, cost

    def __expand(self, node: Vertex, env_conf: EnvironmentConfiguration) -> List[Vertex]:
        successors = []
        for _, result in self.__successor_func(node, env_conf):
            successors.append(result)
        return successors

    def __successor_func(self, node: Vertex, env_conf: EnvironmentConfiguration) -> List[Tuple[str, Vertex]]:
        current_state = node.get_state()
        edges_list = EnvironmentUtils.get_possible_moves(current_state, env_conf)
        self._expansions_num += 1

        names_of_edges = [edge.get_edge_name() for edge in edges_list]
        edge_to_next_state_list = []
        for edge_name in names_of_edges:
            next_vertex = EnvironmentUtils.get_next_vertex(node, edge_name, self.step_cost, env_conf)
            env_conf.get_vertexes()[next_vertex.get_vertex_name()] = next_vertex
            edge_to_next_state_list.append((edge_name, next_vertex))
        return edge_to_next_state_list

    def goal_test(self, problem: Tuple[State, State, EnvironmentConfiguration], current_state: State):
        _, goal_state, _ = problem
        return goal_state == current_state

    def __make_node(self, state: State, env_conf: EnvironmentConfiguration):
        name = state.get_current_vertex_name()
        vertex = env_conf.get_vertexes()[name]
        vertex.set_state(state)
        return vertex

    def __insert_to_fringe(self, fringe: List, key, priority):
        to_insert = True
        for k, p in fringe:
            if key == k and p < priority:
                to_insert = False
        if to_insert:
            fringe.append((copy.deepcopy(key), priority))

    def __pop_from_fringe(self, fringe: List):
        fringe.sort(key=lambda x: (x[1], x[0].get_vertex_name()))

        print("------------------------------------------")

        for f in fringe:
            print("priority= ", f[1], " vertex: ", f[0].get_vertex_name())

        top_element = fringe[0]
        print("poped: ", top_element[0].get_vertex_name())
        print("------------------------------------------")
        fringe.remove(top_element)
        return top_element
