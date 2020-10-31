from typing import Optional

from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.Edge import Edge
from data_structures.Vertex import Vertex


class ConfigurationReader:
    COMMENT_SEPARATOR = ";"
    SPACE_SEPARATOR = " "

    @staticmethod
    def read_configuration(file_path: str):
        with open(file_path, 'r') as f:
            lines = [line.split(ConfigurationReader.COMMENT_SEPARATOR)[0].strip() for line in f if
                     line.strip()]  # removes comments & empty lines.

        vertex = [], edges = []
        vertices_num = -1, deadline = -1  # default values.
        for current_line in lines:
            if current_line.startswith("#N"):
                vertices_num = current_line.split(ConfigurationReader.SPACE_SEPARATOR)[1]
            elif current_line.startswith("#D"):
                deadline = current_line.split(ConfigurationReader.SPACE_SEPARATOR)[1]
            elif current_line.startswith("#V"):
                vertex.append(ConfigurationReader.create_vertex(current_line))
            elif current_line.startswith("#E"):
                edges.append(ConfigurationReader.create_edge(current_line))
        return EnvironmentConfiguration(vertices_num, deadline, vertex, edges)

    @staticmethod
    # Example input: #E1 1 2 W1
    def create_edge(input_line: str) -> Optional[Edge]:
        parts = input_line.split(ConfigurationReader.SPACE_SEPARATOR)
        if len(parts) != 4:
            print(f'input line: {input_line} is invalid. Correct format: #E1 1 2 W1')
            return None
        name = parts[0], weight = parts[1], first_vertex = parts[2], second_vertex = parts[3]
        return Edge(name, weight, (first_vertex, second_vertex))

    @staticmethod
    # Example input: #V4 P2 or #V4
    def create_vertex(input_line: str) -> Optional[Vertex]:
        parts = input_line.split(ConfigurationReader.SPACE_SEPARATOR)
        parts_length = len(parts)
        peoples_in_vertex = 0
        if parts_length > 2 or parts_length == 0:
            print(f'input line: {input_line} is invalid. Correct format: #V4 P2 or #V4')
            return None
        if parts_length == 2:
            peoples_in_vertex = int(parts[1])
        name = parts[0]
        return Vertex(name, peoples_in_vertex)


if __name__ == '__main__':
    config_path = "C:/Users/Ofir/PycharmProjects/AI_Hurricane_Evacuation/initial_configurations/example.ascii"
    configuration_reader = ConfigurationReader()
    configuration_reader.read_configuration(config_path)
