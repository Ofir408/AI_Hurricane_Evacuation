from typing import Dict

from data_structures.Edge import Edge
from data_structures.Vertex import Vertex


class EnvironmentConfiguration:

    def __init__(self, vertices_num: int, deadline: float, vertex: Dict[str, Vertex], edges: Dict[str, Edge]):
        self.__vertices_num = vertices_num
        self.__deadline = deadline
        self.__vertexes = vertex
        self.__edges = edges

    def get_vertices_num(self):
        return self.__vertices_num

    def get_deadline(self):
        return self.__deadline

    def get_vertexes(self):
        return self.__vertexes

    def get_edges(self):
        return self.__edges
