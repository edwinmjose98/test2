import os

from dotenv import load_dotenv
# from flask.cli import load_dotenv


def load_env(file=".env"):
    # file = '.env'
    if os.path.exists(file):
        load_dotenv()
        print(os.getenv("TEST", "Default"))
    else:
        print("Pls set .env file. (You can copy from .env.example)")
        exit(1)


def load():
    print("Loading env")
    env_file = os.path.dirname(__file__) + "/../.env"
    load_env(env_file)
