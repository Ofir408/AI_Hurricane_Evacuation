from typing import List

from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.State import State


class StateUtils:

    @staticmethod
    def get_saved_people_num(state: State, current_traveled_states, env_conf: EnvironmentConfiguration) -> List[int]:
        score = 0
        traveled_vertexes = [vertex_name for vertex_name in StateUtils.get_state_traveled_vertexes(state) if
                             vertex_name not in current_traveled_states]
        current_traveled_states.append(state.get_current_vertex_name())
        vertexes_dict = env_conf.get_vertexes()
        for vertex in traveled_vertexes:
            score += vertexes_dict[vertex].get_people_num()
        return score

    @staticmethod
    def get_state_traveled_vertexes(state: State) -> List[str]:
        required_vertexes_dict = state.get_required_vertexes()
        return [vertex_name for vertex_name in required_vertexes_dict.keys()
                if required_vertexes_dict[vertex_name]]
