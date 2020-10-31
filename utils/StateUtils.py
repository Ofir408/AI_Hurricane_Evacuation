from data_structures.Edge import Edge
from data_structures.Vertex import Vertex


class StateUtils:
    EDGE_PREFIX = "#E"
    VERTEX_PREFIX = "#V"
    WEIGHT_PREFIX = "W"
    SPACE_SEPARATOR = " "
    DEADLINE_PREFIX = "#D"
    NUMBER_OF_VERTICES_PREFIX = "#N"
    PERSONS_NUM_PREFIX = "P"

    @staticmethod
    def print_state(num_of_vertex: int, deadline: float, edges: list, vertex: list):
        print(StateUtils.NUMBER_OF_VERTICES_PREFIX + StateUtils.SPACE_SEPARATOR + str(num_of_vertex))
        print(StateUtils.DEADLINE_PREFIX + StateUtils.SPACE_SEPARATOR + str(deadline))

        for vertex in vertex:
            StateUtils.__print_vertex(vertex)
        for edge in edges:
            StateUtils.__print_edge(edge)

    @staticmethod
    def __print_vertex(vertex: Vertex):
        print(
            StateUtils.VERTEX_PREFIX + vertex.get_vertex_name() + StateUtils.SPACE_SEPARATOR
            + StateUtils.PERSONS_NUM_PREFIX + str(vertex.get_people_num()))

    @staticmethod
    def __print_edge(edge: Edge):
        first_vertex_name, second_vertex_name = edge.get_vertex_names()
        print(
            StateUtils.EDGE_PREFIX + edge.get_edge_name() + StateUtils.SPACE_SEPARATOR + first_vertex_name
            + StateUtils.SPACE_SEPARATOR +
            second_vertex_name + StateUtils.SPACE_SEPARATOR + StateUtils.WEIGHT_PREFIX + str(edge.get_weight()))
