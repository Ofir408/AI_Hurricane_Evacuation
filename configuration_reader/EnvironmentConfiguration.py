class EnvironmentConfiguration:

    def __init__(self, vertices_num: int, deadline: float, vertex: list, edges: list):
        self.__vertices_num = vertices_num
        self.__deadline = deadline
        self.__vertex = vertex
        self.__edges = edges

    def get_vertices_num(self):
        return self.__vertices_num

    def get_deadline(self):
        return self.__deadline

    def get_vertex(self):
        return self.__vertex

    def get_edges(self):
        return self.__edges
