import copy

from bl.agents.tree_search.heuristic_functions.IHueristicFunc import IHueristicFunc
from data_structures.State import State


class LeftVertexesToVisitFunc(IHueristicFunc):

    def calc_estimation_from_goal(self, current_state: State, goal_state: State):
        vertex_to_is_visited = copy.deepcopy(current_state.get_required_vertexes())
        counter = 0
        for _, was_visited in vertex_to_is_visited.items():
            if not was_visited:
                counter += 1
        return counter

