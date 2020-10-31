from data_structures.State import State


class Vertex:
    def __init__(self, people_num: int, state: State, parent_vertex: 'Vertex' = None,
                 depth: int = None, cost: int = None):
        self.__state = state
        self.__people_num = people_num
        self.__edges = []
        self.__parent_vertex = parent_vertex
        self.__depth = depth
        self.__cost = cost

    def add_edge_name(self, edge_name: str):
        self.__edges.append(edge_name)

    def set_parent_vertex(self, parent_vertex: 'Vertex'):
        self.__parent_vertex = parent_vertex

    def set_depth(self, depth):
        self.__depth = depth

    def set_cost(self, cost):
        self.__cost = cost

    def get_vertex_name(self):
        return self.__state.get_current_vertex_name()

    def get_people_num(self):
        return self.__people_num

    def get_edges(self):
        return self.__edges

    def get_parent_vertex(self):
        return self.__parent_vertex

    def get_depth(self):
        return self.__depth

    def get_cost(self):
        return self.__cost
