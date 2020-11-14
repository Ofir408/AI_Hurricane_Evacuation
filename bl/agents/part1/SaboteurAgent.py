from typing import Tuple

from bl.agents.IAgent import IAgent
from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.Edge import Edge
from data_structures.State import State
from data_structures.Vertex import Vertex
from utils.EnvironmentUtils import EnvironmentUtils


class SaboteurAgent(IAgent):
    NO_OPS = "NO-OPS"
    BLOCK = "BLOCK"
    TRAVERSE = "TRAVERSE"

    def __init__(self, vertexes_num):
        super().__init__()
        self.__operations = [SaboteurAgent.NO_OPS] * vertexes_num + [SaboteurAgent.BLOCK, SaboteurAgent.TRAVERSE]
        self.__operation_inx = 0

    def get_action(self, percepts: Tuple[State, EnvironmentConfiguration]) -> str:
        current_state, env_conf = percepts
        print(EnvironmentUtils.print_environment(env_conf))
        if self.__operation_inx == len(self.__operations):
            self.__operation_inx = 0
        operation = self.__operations[self.__operation_inx]
        self.__operation_inx += 1

        if operation == SaboteurAgent.NO_OPS:
            return SaboteurAgent.NO_OPS
        if operation == SaboteurAgent.BLOCK:
            edge, is_exist = self.__get_lowest_cost_edge_adjacent(current_state, env_conf)
            if is_exist:
                self.__block_edge(edge.get_edge_name(), env_conf)
            return SaboteurAgent.NO_OPS
        else:
            # traverses a lowest-cost remaining edge
            edge, is_exist = self.__get_lowest_cost_edge_adjacent(current_state, env_conf)
            if is_exist:
                print("traverse to edge: ", edge.get_edge_name())
                return edge.get_edge_name()
            return SaboteurAgent.NO_OPS

    def step_cost(self, parent_node: Vertex, action: Edge, new_node: Vertex) -> int:
        operation = self.__operations[self.__operation_inx - 1]

        if operation == SaboteurAgent.NO_OPS:
            return 0  # does nothing
        if operation == SaboteurAgent.BLOCK:
            return 1  # takes 1 time unit
        else:
            # traverses a lowest-cost remaining edge
            return action.get_weight()

    # Return Tuple[edge:Edge, was_edge_found:bool]
    def __get_lowest_cost_edge_adjacent(self, current_state: State, env_conf: EnvironmentConfiguration):
        edges = EnvironmentUtils.get_possible_moves(current_state, env_conf)
        edges.sort(key=lambda edge: (edge.get_weight(), int(edge.get_edge_name())))
        if edges:
            return edges[0], True
        else:
            print("saboteur agent was terminated")
            self._was_terminated = True
            return None, False

    def __block_edge(self, edge_name, env_conf):
        print("blocking edge: ", edge_name)
        env_conf.set_blocked_edge(edge_name)
