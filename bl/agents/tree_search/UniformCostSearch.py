from bl.agents.tree_search.IGeneralTreeSearch import IGeneralTreeSearch
from data_structures.Edge import Edge
from data_structures.Vertex import Vertex


class UniformCostSearch(IGeneralTreeSearch):

    def step_cost(self, parent_node: Vertex, action: Edge, new_node: Vertex) -> int:
        return action.get_weight()
