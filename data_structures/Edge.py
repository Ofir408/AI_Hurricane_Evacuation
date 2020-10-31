class Edge:

    def __init__(self, edge_name: str, weight: int, vertex_names: tuple):
        self.__edge_name = edge_name
        self.__weight = weight
        self.__vertex_names = vertex_names

    def get_edge_name(self):
        return self.__edge_name

    def get_weight(self):
        return self.__weight

    def get_vertex_names(self):
        return self.__vertex_names
