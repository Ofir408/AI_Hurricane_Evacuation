import os
import sys

from Runner import Runner
from configuration_reader.ConfigurationReader import ConfigurationReader

configuration_reader = ConfigurationReader()
config_path = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(os.curdir) + "\initial_configurations\input.txt"
config = configuration_reader.read_configuration(config_path)
runner = Runner()
runner.run(config)
