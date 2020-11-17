from bl.Simulator import Simulator
from bl.agents.part1.SaboteurAgent import SaboteurAgent
from bl.agents.part2.AStarAgent import AStarAgent
from bl.agents.part2.GreedyAgent import GreedyAgent
from bl.agents.part2.RTAStarAgent import RTAStarAgent
from configuration_reader.EnvironmentConfiguration import EnvironmentConfiguration
from data_structures.State import State
from utils.EnvironmentUtils import EnvironmentUtils


class Runner:

    def run(self, env_config: EnvironmentConfiguration):
        chosen_agents = []
        states = []
        output_msg = "Choose Agent: \n 1) Greedy Agent\n 2) A* Agent\n 3) RTA* agent\n 4) Bonus: SaboteurAgent\n"
        num_of_agent = int(input("Enter number of agents\n"))
        for _ in range(num_of_agent):
            agent_num = int(input(output_msg))
            while agent_num > 4 or agent_num < 1:
                print("Invalid agent number")
                agent_num = int(input(output_msg))
            chosen_agents.append(self.__get_agent(agent_num))
            EnvironmentUtils.print_environment(env_config)
            initial_state_name = input("Choose initial state\n")
            states.append(State(initial_state_name, EnvironmentUtils.get_required_vertexes(env_config)))

        simulator = Simulator()
        simulator.run_simulate(chosen_agents, simulator.update_func, simulator.terminate_func,
                               simulator.performance_func, env_config, states)

    def __get_agent(self, agent_num):
        if agent_num == 1:
            return GreedyAgent()
        elif agent_num == 2:
            return AStarAgent()
        elif agent_num == 3:
            return RTAStarAgent()
        elif agent_num == 4:
            return SaboteurAgent()
