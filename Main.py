from Runner import Runner
from configuration_reader.ConfigurationReader import ConfigurationReader

config_path = "C:/Users/Ofir/PycharmProjects/AI_Hurricane_Evacuation/initial_configurations/example.ascii"
configuration_reader = ConfigurationReader()
config = configuration_reader.read_configuration(config_path)
runner = Runner()

runner.run(config) # part1
#runner.search_agents_runner(config) # part2
