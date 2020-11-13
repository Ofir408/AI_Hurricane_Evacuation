
from bl.agents.part2.ITreeSearchAgent import ITreeSearchAgent
from bl.search_tree.GreedySearchTree import GreedySearchTree
from bl.search_tree.heuristic_functions.LeftVertexesToVisitFunc import LeftVertexesToVisitFunc


class GreedyAgent(ITreeSearchAgent):

    def __init__(self):
        super().__init__(GreedySearchTree(LeftVertexesToVisitFunc()))
