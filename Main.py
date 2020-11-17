import os

from Runner import Runner
from configuration_reader.ConfigurationReader import ConfigurationReader

config_path = os.getcwd() + "\initial_configurations\input.txt"
configuration_reader = ConfigurationReader()
config = configuration_reader.read_configuration(config_path)
runner = Runner()
runner.run(config)
