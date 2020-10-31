class State:
    """
    Represent a state, contains:
    1) vertex with people that the agent has to go through them, with binary flag (did we reach everyone or not)
    2) current vertex name.
    """
    def __init__(self, current_vertex_name, required_vertexes: dict = None):
        self.__required_vertexes = required_vertexes
        self.__current_vertex = current_vertex_name

    def set_visited_vertex(self, vertex_name: str):
        self.__required_vertexes[vertex_name] = True

    def set_required_vertexes(self, require_vertexes):
        self.__required_vertexes = require_vertexes

    def get_required_vertexes(self):
        return self.__required_vertexes

    def get_current_vertex_name(self):
        return self.__current_vertex

