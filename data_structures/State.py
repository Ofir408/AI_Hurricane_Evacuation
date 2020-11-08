from typing import Dict


class State:
    """
    Represent a state, contains:
    1) names of vertexes with people that the agent has to go through them, with binary flag (did we reach everyone or not)
    2) current vertex name.
    """

    def __init__(self, current_vertex_name: str, required_vertexes: Dict[str, int] = None):
        self.__current_vertex = current_vertex_name
        self.__required_vertexes = required_vertexes

    def set_visited_vertex(self, vertex_name: str):
        self.__required_vertexes[vertex_name] = True

    def set_required_vertexes(self, require_vertexes):
        self.__required_vertexes = require_vertexes

    def get_required_vertexes(self):
        return self.__required_vertexes

    def get_current_vertex_name(self):
        return self.__current_vertex

    def __eq__(self, other):
        return self.__current_vertex == other.get_current_vertex_name()

    def __str__(self) -> str:
        return "Current State={0}. Required State={1}".format(self.__current_vertex, self.__required_vertexes)
