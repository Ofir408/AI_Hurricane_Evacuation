import copy
from typing import List, Dict

from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.Edge import Edge
from data_structures.State import State
from data_structures.Vertex import Vertex


class EnvironmentUtils:
    _EDGE_PREFIX = "#E"
    _VERTEX_PREFIX = "#V"
    _WEIGHT_PREFIX = "W"
    _SPACE_SEPARATOR = " "
    _DEADLINE_PREFIX = "#D"
    _NUMBER_OF_VERTICES_PREFIX = "#N"
    _PERSONS_NUM_PREFIX = "P"

    @staticmethod
    def print_environment(env_config: EnvironmentConfiguration):
        num_of_vertex = env_config.get_vertices_num()
        deadline = env_config.get_deadline()
        edges_dict = env_config.get_edges()
        vertexes_dict = env_config.get_vertexes()

        print(EnvironmentUtils._NUMBER_OF_VERTICES_PREFIX + EnvironmentUtils._SPACE_SEPARATOR + str(
            num_of_vertex))
        print(EnvironmentUtils._DEADLINE_PREFIX + EnvironmentUtils._SPACE_SEPARATOR + str(deadline))

        for vertex in vertexes_dict.values():
            EnvironmentUtils.__print_vertex(vertex)
        for edge in edges_dict.values():
            EnvironmentUtils.__print_edge(edge)

    @staticmethod
    def get_possible_moves(current_state: State, env_config: EnvironmentConfiguration) -> List[Edge]:
        current_vertex_name = current_state.get_current_vertex_name()
        vertexes_dict = env_config.get_vertexes()
        edges_dict = env_config.get_edges()
        current_vertex = vertexes_dict[current_vertex_name]
        names_of_edges = current_vertex.get_edges()
        possible_edges = []
        for edge_name in names_of_edges:
            possible_edges.append(edges_dict[edge_name])
        return possible_edges

    @staticmethod
    def get_required_vertexes(env_config: EnvironmentConfiguration) -> Dict[str, bool]:
        required_vertexes = {}
        for vertex_name in env_config.get_vertexes().values():
            if vertex_name.get_people_num() > 0:
                required_vertexes[vertex_name.get_vertex_name()] = False
        return required_vertexes

    @staticmethod
    def get_next_state(current_state: State, edge_name: str, env_config: EnvironmentConfiguration):
        """

        :param current_state: the current state
        :param edge_name: edge name from current vertex to the next vertex
        :param env_config: environment configuration
        :return: The new vertex
        """
        current_vertex_name = current_state.get_current_vertex_name()
        edges_dict = env_config.get_edges()
        edge = edges_dict[edge_name]
        first_vertex, sec_vertex = edge.get_vertex_names()
        next_vertex_name = first_vertex if sec_vertex == current_vertex_name else sec_vertex
        vertexes_dict = env_config.get_vertexes()
        current_vertex = vertexes_dict[current_vertex_name]
        next_vertex = vertexes_dict[next_vertex_name]
        people_in_next_vertex = next_vertex.get_people_num()

        # TODO: check if next_vertex really change env_config
        next_vertex = Vertex(people_in_next_vertex, State(next_vertex_name), current_vertex.get_parent_vertex(),
                             current_vertex.get_depth(), current_vertex.get_cost() + edge.get_weight())
        return next_vertex.get_state()

    @staticmethod
    def __print_vertex(vertex: Vertex):
        print(
            EnvironmentUtils._VERTEX_PREFIX + vertex.get_vertex_name() + EnvironmentUtils._SPACE_SEPARATOR
            + EnvironmentUtils._PERSONS_NUM_PREFIX + str(vertex.get_people_num()))

    @staticmethod
    def __print_edge(edge: Edge):
        first_vertex_name, second_vertex_name = edge.get_vertex_names()
        print(
            EnvironmentUtils._EDGE_PREFIX + edge.get_edge_name() + EnvironmentUtils._SPACE_SEPARATOR + first_vertex_name
            + EnvironmentUtils._SPACE_SEPARATOR +
            second_vertex_name + EnvironmentUtils._SPACE_SEPARATOR + EnvironmentUtils._WEIGHT_PREFIX + str(
                edge.get_weight()))
