import copy
import sys
from collections import deque
from typing import Tuple

from bl.agents.IAgent import IAgent
from bl.tree_search.UniformCostSearch import UniformCostSearch
from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.Edge import Edge
from data_structures.State import State
from data_structures.Vertex import Vertex


class GreedyAgent(IAgent):

    def __init__(self):
        super().__init__()
        self.__path_queue = deque()
        self.__searcher = UniformCostSearch()

    def get_action(self, percepts: Tuple[State, EnvironmentConfiguration]) -> str:
        if len(self.__path_queue) == 0:
            was_path_found = self.__init_path(percepts)
            if not was_path_found:
                print("path not found")
                self._was_terminated = True
                return "NO-OPS"
        vertex = self.__get_next_vertex()
        return vertex.get_action()

    def step_cost(self, parent_node: Vertex, action: Edge, new_node: Vertex) -> int:
        return self.__searcher.step_cost(parent_node, action, new_node)

    def __get_next_vertex(self) -> Vertex:
        return self.__path_queue.popleft()

    def __init_path(self, percepts: Tuple[State, EnvironmentConfiguration]) -> bool:
        initial_state, env_conf = percepts
        vertexes_for_visit = dict(
            (k, v) for k, v in initial_state.get_required_vertexes().items() if not v)
        print("vertexes_for_visit = ", vertexes_for_visit)

        if len(vertexes_for_visit) == 0:
            self._was_terminated = True  # path was not found

        # choose the shortest path to the next vertex with people to be rescued
        env_conf_backup = copy.deepcopy(env_conf)
        min_cost = sys.maxsize
        shortest_path = []
        for vertex_name in sorted(vertexes_for_visit.keys()):
            vertex = env_conf_backup.get_vertexes()[vertex_name]
            solution_vertex = self.__searcher.search((initial_state, vertex.get_state(), env_conf_backup), [])
            if solution_vertex.get_cost() < min_cost:
                min_cost = solution_vertex.get_cost()
                shortest_path, _ = self.__searcher.restore_solution(solution_vertex)
        print("path:", [vertex.get_vertex_name() for vertex in shortest_path], "cost: ", min_cost)
        for vertex in shortest_path:
            self.__path_queue.append(vertex)
        return True  # path was found
