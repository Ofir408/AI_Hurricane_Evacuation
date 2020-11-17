from bl.agents.part2.ITreeSearchAgent import ITreeSearchAgent
from bl.search_tree.AStarSearchTree import AStarSearchTree
from bl.search_tree.heuristic_functions.LeftVertexesToVisitFunc import LeftVertexesToVisitFunc
from utils.EnvironmentUtils import EnvironmentUtils


class RTAStarAgent(ITreeSearchAgent):

    def __init__(self, limit=10):
        super().__init__(AStarSearchTree(LeftVertexesToVisitFunc(), limit))

    def _get_path(self, percepts):
        vertexes_path = super()._get_path(percepts)
        last_vertex = vertexes_path[-1]
        initial_state, env_config = percepts
        goal_state = EnvironmentUtils.get_goal_state(env_config)
        problem = (initial_state, goal_state, env_config)
        self._search_tree_algo._was_terminate = False
        was_solution_found = self._search_tree_algo.goal_test(problem, last_vertex.get_state())
        if was_solution_found:
            # found a solution in the A* within the time limit.
            return vertexes_path
        else:
            # No solution in the A* within the time limit, move to the first step according the last expended node.
            if len(vertexes_path) > 1:
                return [vertexes_path[1]]
            return [vertexes_path[0]]
