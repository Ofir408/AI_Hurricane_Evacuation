from bl.search_tree.IGeneralSearchTree import IGeneralSearchTree
from data_structures.Edge import Edge
from data_structures.Vertex import Vertex


class UniformCostSearchTree(IGeneralSearchTree):

    def step_cost(self, parent_node: Vertex, action: Edge, new_node: Vertex) -> int:
        return action.get_weight()
