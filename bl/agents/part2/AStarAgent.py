from bl.agents.part2.ITreeSearchAgent import ITreeSearchAgent
from bl.search_tree.AStarSearchTree import AStarSearchTree
from bl.search_tree.heuristic_functions.LeftVertexesToVisitFunc import LeftVertexesToVisitFunc


class AStarAgent(ITreeSearchAgent):

    def __init__(self, limit=10000):
        super().__init__(AStarSearchTree(LeftVertexesToVisitFunc(), limit))
