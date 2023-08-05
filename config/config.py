from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN")

HOST = env.str("HOST")
DBNAME = env.str("DBNAME")
USER = env.str("USER")
PORT = env.int("PORT")
PASSWORD = env.str("PASSWORD")