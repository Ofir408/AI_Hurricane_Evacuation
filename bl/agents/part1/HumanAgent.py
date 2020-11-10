from typing import Tuple

from bl.agents.IAgent import IAgent
from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.Edge import Edge
from data_structures.State import State
from data_structures.Vertex import Vertex
from utils.EnvironmentUtils import EnvironmentUtils


class HumanAgent(IAgent):

    def step_cost(self, parent_node: Vertex, action: Edge, new_node: Vertex) -> int:
        return action.get_weight()

    def get_action(self, percepts: Tuple[State, EnvironmentConfiguration]) -> str:
        current_state, env_config = percepts
        print("Current Environment:")
        EnvironmentUtils.print_environment(env_config)
        print(current_state)
        possible_edges = EnvironmentUtils.get_possible_moves(current_state, env_config)
        user_input_edge = self.__get_input_from_user(possible_edges)
        return user_input_edge

    def __get_input_from_user(self, possible_edges):
        print("Possible edges: ")
        print(*possible_edges, sep='\n')
        edge = input("Enter Required Edge:\n")
        possible_names_of_edges = [edge.get_edge_name() for edge in possible_edges]
        while edge not in possible_names_of_edges:
            print("Invalid Edge. Choose edge from the possible edges: ")
            print(*possible_edges, sep='\n')
            edge = input("Enter Required Edge:\n")
        return edge
