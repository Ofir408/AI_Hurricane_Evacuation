from agents.HumanAgent import HumanAgent
from configuration_reader.ConfigurationReader import ConfigurationReader
from data_structures.State import State
from utils.EnvironmentUtils import EnvironmentUtils

config_path = "C:/Users/Ofir/PycharmProjects/AI_Hurricane_Evacuation/initial_configurations/example.ascii"
configuration_reader = ConfigurationReader()
config = configuration_reader.read_configuration(config_path)
print("Done to read configuration")
print("Printing state:")
EnvironmentUtils.print_state(config)
initial_vertex = input("Enter initial vertex\n")
agent = HumanAgent()
required_vertexes = EnvironmentUtils.get_required_vertexes(config)
# percepts: Tuple[State, EnvironmentConfiguration]
percepts = (State(initial_vertex, required_vertexes), config)
agent.get_action(percepts)
