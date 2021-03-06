import copy
from typing import List, Dict, Callable

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
        print("Blocked edges: ", env_config.get_blocked_edges())

    @staticmethod
    def get_possible_moves(current_state: State, env_config: EnvironmentConfiguration) -> List[Edge]:
        current_vertex_name = current_state.get_current_vertex_name()
        vertexes_dict = env_config.get_vertexes()
        edges_dict = {k: v for k, v in env_config.get_edges().items() if k not in env_config.get_blocked_edges()}
        current_vertex = vertexes_dict[current_vertex_name]
        names_of_edges = [edge for edge in current_vertex.get_edges() if edge not in env_config.get_blocked_edges()]
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
    def get_next_vertex(current_vertex: Vertex, edge_name: str, step_cost: Callable,
                        env_config: EnvironmentConfiguration) -> Vertex:
        """

        :param current_vertex: the current state
        :param edge_name: edge name from current vertex to the next vertex
        :param step_cost: function that receives parent_vertex, action, new_node and returns the step cost.
        :param env_config: environment configuration
        :return: The new vertex
        """
        current_state = current_vertex.get_state()
        current_vertex_name = current_vertex.get_vertex_name()
        edges_dict = env_config.get_edges()
        vertexes_dict = env_config.get_vertexes()
        if edge_name not in edges_dict:
            current_vertex.set_state(current_state)
            print("No operation for this agent")
            current_vertex.set_cost(
                current_vertex.get_cost() + step_cost(current_vertex, Edge("", 0, ("", "")), current_vertex))
            return current_vertex  # No operation

        edge = edges_dict[edge_name]
        first_vertex, sec_vertex = edge.get_vertex_names()
        next_vertex_name = first_vertex if sec_vertex == current_vertex_name else sec_vertex
        next_vertex = vertexes_dict[next_vertex_name]
        next_state = State(next_vertex_name, copy.deepcopy(current_state.get_required_vertexes()))
        if next_vertex_name in current_state.get_required_vertexes():
            next_state.set_visited_vertex(next_vertex_name)
        next_vertex.set_state(next_state)
        people_in_next_vertex = next_vertex.get_people_num()

        new_next_vertex = Vertex(people_in_next_vertex, next_state, next_vertex.get_edges(),
                                 current_vertex, edge.get_edge_name(), current_vertex.get_depth(),
                                 EnvironmentUtils.g(current_vertex, env_config) + step_cost(current_vertex, edge, next_vertex))
        return new_next_vertex

    @staticmethod
    def g(node: Vertex, env_conf: EnvironmentConfiguration) -> int:
        current_node = copy.deepcopy(node)
        edges = env_conf.get_edges()
        edges_of_path = []
        cost = 0
        while current_node is not None:
            edges_of_path.append(current_node.get_action() if current_node.get_action() is not None else "")
            current_node = current_node.get_parent_vertex()
        # calculate the cost to the solution
        for edge_name in filter(None, edges_of_path):
            cost += edges[edge_name].get_weight()
        return cost

    @staticmethod
    def get_goal_state(env_config: EnvironmentConfiguration) -> State:
        temp_dict = EnvironmentUtils.get_required_vertexes(env_config)
        goal_dict = {}
        for k, v in temp_dict.items():
            goal_dict[k] = True
        goal_state = State("", goal_dict)
        return goal_state

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
