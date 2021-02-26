import os

from BookManager.utilities.env import load_env

version = "1.0.0"

env_file = os.path.dirname(__file__) + "/../.env"
load_env(env_file)
