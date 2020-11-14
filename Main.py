import os

from Runner import Runner
from configuration_reader.ConfigurationReader import ConfigurationReader

config_path = os.getcwd() + "\initial_configurations\example2.ascii"
print("config_path= ", config_path)
configuration_reader = ConfigurationReader()
config = configuration_reader.read_configuration(config_path)
runner = Runner()
runner.run(config)
