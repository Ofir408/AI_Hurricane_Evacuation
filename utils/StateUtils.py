from typing import List

from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.State import State


class StateUtils:

    @staticmethod
    def get_saved_people_num(state: State, env_conf: EnvironmentConfiguration) -> List[int]:
        score = 0
        traveled_vertexes = StateUtils.get_traveled_vertexes(state)
        vertexes_dict = env_conf.get_vertexes()

        for vertex in traveled_vertexes:
            score += vertexes_dict[vertex].get_people_num()
        return score

    @staticmethod
    def get_traveled_vertexes(state: State) -> List[str]:
        required_vertexes_dict = state.get_required_vertexes()
        return [vertex_name for vertex_name in required_vertexes_dict.keys()
                if required_vertexes_dict[vertex_name]]

