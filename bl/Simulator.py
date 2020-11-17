from typing import List, Callable, Tuple

from bl.agents import IAgent
from configuration_reader import EnvironmentConfiguration
from data_structures.State import State
from utils.EnvironmentUtils import EnvironmentUtils
from utils.StateUtils import StateUtils


class Simulator:

    def run_simulate(self, agents: List, update_func: Callable, termination_func: Callable,
                     performance_func: Callable,
                     env_conf: EnvironmentConfiguration, states: List[State]):
        """
        :param agents: list of the agents in the environment
        :param update_func: update function, returns the new state
        :param termination_func: termination function that receives the current state and decide if to terminate or not.
        :param performance_func: performance function, return the score given state
        :param env_conf: Environment configuration
        :param states: the states of the agents
        :return: list of the scores of the agents.
        """
        scores = [0] * len(agents)
        costs = [0] * len(agents)
        actions = [[] for _ in range(len(agents))]
        traveled_states = []
        should_terminate = False

        while not should_terminate:
            for agent_num, agent in enumerate(agents):
                percepts = self.__get_percepts(agent_num, states, env_conf)
                action = agent.get_action(percepts)
                actions[agent_num].append(action)
                new_state = update_func(agent, action, states[agent_num], (costs, agent_num), env_conf)
                states[agent_num] = new_state
                scores[agent_num] += performance_func(new_state, traveled_states, env_conf)
                should_terminate = termination_func(states, agents)
                self.__display_word_state(agent_num, len(agents), actions, costs, scores, env_conf)
        return scores

    def __get_percepts(self, agent_num, states, env_conf):
        return states[agent_num], env_conf

    def update_func(self, agent: IAgent, action: str, current_state: State, costs_info: Tuple[List, int],
                    env_conf: EnvironmentConfiguration):
        vertex = env_conf.get_vertexes()[current_state.get_current_vertex_name()]
        vertex.set_state(current_state)
        new_state = EnvironmentUtils.get_next_vertex(vertex, action, agent.step_cost, env_conf).get_state()
        new_state.set_visited_vertex(new_state.get_current_vertex_name())
        costs, agent_num = costs_info
        edges_dict = env_conf.get_edges()
        if action in edges_dict.keys():
            costs[agent_num] += edges_dict[action].get_weight()
        return new_state

    def performance_func(self, new_state: State, traveled_states, env_config: EnvironmentConfiguration):
        return StateUtils.get_saved_people_num(new_state, traveled_states, env_config)

    # TODO: add deadline to terminate func
    def terminate_func(self, states: List[State], agents: List):
        should_terminate = len([agent for agent in agents if agent.was_terminated()]) == len(agents)
        if should_terminate:
            return True
        traveled_states = []
        for state in states:
            traveled_states += StateUtils.get_state_traveled_vertexes(state)
        traveled_states = set().union(traveled_states)
        return len(traveled_states) == len(states[0].get_required_vertexes())

    def __display_word_state(self, current_agent_num, agents_num, actions, costs, scores, env_config):
        if current_agent_num == agents_num - 1:
            print("----------------------------------")
            print("The step is over. Display the state of the world:")
            EnvironmentUtils.print_environment(env_config)
            print("actions: ", actions)
            print("costs: ", costs)
            print("scores: ", scores)
            print("----------------------------------")
