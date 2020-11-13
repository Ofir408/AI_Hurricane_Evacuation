from bl.Simulator import Simulator
from bl.agents.part2.AStarAgent import AStarAgent
from bl.agents.part2.GreedyAgent import GreedyAgent
from bl.agents.part2.RTAStarAgent import RTAStarAgent
from bl.search_tree.AStarSearchTree import AStarSearchTree
from bl.search_tree.GreedySearchTree import GreedySearchTree
from bl.search_tree.IGeneralSearchTree import IGeneralSearchTree
from bl.search_tree.RTAStarSearchTree import RTAStarSearchTree
from bl.search_tree.heuristic_functions.LeftVertexesToVisitFunc import LeftVertexesToVisitFunc
from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.State import State
from utils.EnvironmentUtils import EnvironmentUtils


class Runner:

    def run(self, env_config: EnvironmentConfiguration):
        #agents = [HumanAgent(), GreedyAgent(), SaboteurAgent(env_config.get_vertices_num())]
        agents = [GreedyAgent(), AStarAgent(), RTAStarAgent()]
        chosen_agents = []
        states = []
        for _ in range(1):
            agent_num = int(input("Choose Agent: \n 1) Greedy Agent\n 2) A* Agent\n 3) RTA* agent\n"))
            while agent_num > 4 or agent_num < 1:
                print("Invalid agent number")
                agent_num = input("Choose Agent: \n 1) Greedy Agent\n 2) A* Agent\n 3) RTA* agent\n")
            chosen_agents.append(agents[agent_num - 1])
            EnvironmentUtils.print_environment(env_config)
            initial_state_name = input("Choose initial state\n")
            states.append(State(initial_state_name, EnvironmentUtils.get_required_vertexes(env_config)))

        simulator = Simulator()
        scores = simulator.run_simulate(chosen_agents, simulator.update_func, simulator.terminate_func,
                                        simulator.performance_func, env_config, states)
        print("--------------------------------------")
        print("Scores:")
        print(scores)

    def search_agents_runner(self, env_config: EnvironmentConfiguration):
        agents = [AStarSearchTree(LeftVertexesToVisitFunc()), GreedySearchTree(LeftVertexesToVisitFunc()),
                  RTAStarSearchTree(LeftVertexesToVisitFunc())]
        chosen_agents = []
        states = []
        for i in range(1):
            agent_num = int(input("Choose Agent: \n 1) AStarSearchAgent\n 2) GreedySearchAgent\n 3) Real Time A*\n"))
            while agent_num > 4 or agent_num < 1:
                print("Invalid agent number")
                agent_num = int(
                    input("Choose Agent: \n 1) AStarSearchAgent\n 2) GreedySearchAgent\n 3) Real Time A* agent\n"))
            chosen_agents.append(agents[agent_num - 1])
            EnvironmentUtils.print_environment(env_config)
            initial_state_name = input("Choose initial state\n")
            state = State(initial_state_name, EnvironmentUtils.get_required_vertexes(env_config))
            state.set_visited_vertex(initial_state_name)
            states.append(state)

            print("Start searching...")
            search_agent = agents[agent_num - 1]
            goal_state = EnvironmentUtils.get_goal_state(env_config)
            initial_state = states[i]
            problem = (initial_state, goal_state, env_config)
            search_result, was_solution_found = search_agent.search(problem, [])
            if was_solution_found == IGeneralSearchTree.SOLUTION_NOT_FOUND:
                print("No solution was found")
                return
            path, cost = search_agent.restore_solution(search_result, env_config)
            print("path= ", [vertex.get_vertex_name() for vertex in path])
            print("cost= ", cost)
            print("Done!")
