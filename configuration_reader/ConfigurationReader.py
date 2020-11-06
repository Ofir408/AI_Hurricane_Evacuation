from typing import Optional, Tuple

from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.Edge import Edge
from data_structures.State import State
from data_structures.Vertex import Vertex


class ConfigurationReader:
    COMMENT_SEPARATOR = ";"
    SPACE_SEPARATOR = " "

    @staticmethod
    def read_configuration(file_path: str):
        with open(file_path, 'r') as f:
            lines = [line.split(ConfigurationReader.COMMENT_SEPARATOR)[0].strip() for line in f if
                     line.strip()]  # removes comments & empty lines.

        vertexes_dict = {}
        edges_dict = {}
        vertices_num = -1
        deadline = -1  # default values.
        for current_line in lines:
            if current_line.startswith("#N"):
                vertices_num = int(current_line.split(ConfigurationReader.SPACE_SEPARATOR)[1])
            elif current_line.startswith("#D"):
                deadline = float(current_line.split(ConfigurationReader.SPACE_SEPARATOR)[1])
            elif current_line.startswith("#V"):
                name, vertex = ConfigurationReader.create_vertex(current_line)
                vertexes_dict[name] = vertex
            elif current_line.startswith("#E"):
                name, edge = ConfigurationReader.create_edge(current_line)
                edges_dict[name] = edge
                # add the edge name to relevant vertexes
                first_vertex, second_vertex = edge.get_vertex_names()
                vertexes_dict[first_vertex].add_edge_name(edge.get_edge_name())
                vertexes_dict[second_vertex].add_edge_name(edge.get_edge_name())
        return EnvironmentConfiguration(vertices_num, deadline, vertexes_dict, edges_dict)

    @staticmethod
    # Example input: #E1 1 2 W1
    def create_edge(input_line: str) -> Optional[Tuple[str, Edge]]:
        parts = input_line.split(ConfigurationReader.SPACE_SEPARATOR)
        if len(parts) != 4:
            print(f'input line: {input_line} is invalid. Correct format: #E1 1 2 W1')
            return None
        name = parts[0].replace("#E", "")
        first_vertex = parts[1]
        second_vertex = parts[2]
        weight = int(parts[3].replace("W", ""))
        return name, Edge(name, weight, (first_vertex, second_vertex))

    @staticmethod
    # Example input: #V4 P2 or #V4
    def create_vertex(input_line: str) -> Optional[Tuple[str, Vertex]]:
        parts = input_line.split(ConfigurationReader.SPACE_SEPARATOR)
        parts_length = len(parts)
        peoples_in_vertex = 0
        if parts_length > 2 or parts_length == 0:
            print(f'input line: {input_line} is invalid. Correct format: #V4 P2 or #V4')
            return None
        if parts_length == 2:
            peoples_in_vertex = int(parts[1].replace("P", ""))
        name = parts[0].replace("#V", "")
        return name, Vertex(peoples_in_vertex, State(name), [])
