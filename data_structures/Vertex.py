from typing import List

from data_structures.State import State


class Vertex:
    def __init__(self, people_num: int, state: State, edges: List[str], parent_vertex: 'Vertex' = None,
                 action: str = None, depth: int = 0, cost: int = 0):
        self.__state = state
        self.__people_num = people_num
        self.__edges = edges
        self.__parent_vertex = parent_vertex
        self.__action = action
        self.__depth = depth
        self.__cost = cost

    def add_edge_name(self, edge_name: str):
        self.__edges.append(edge_name)

    def set_parent_vertex(self, parent_vertex: 'Vertex'):
        self.__parent_vertex = parent_vertex

    def set_action(self, action):
        self.__action = action

    def set_depth(self, depth):
        self.__depth = depth

    def set_cost(self, cost):
        self.__cost = cost

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state

    def get_vertex_name(self):
        return self.__state.get_current_vertex_name()

    def get_people_num(self):
        return self.__people_num

    def get_edges(self) -> List[str]:
        return self.__edges

    def get_parent_vertex(self):
        return self.__parent_vertex

    def get_action(self):
        return self.__action

    def get_depth(self):
        return self.__depth

    def get_cost(self):
        return self.__cost
