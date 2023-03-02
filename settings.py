from environs import Env
from pathlib import Path

env = Env()
env.read_env()

REPLICATE_API_TOKEN = env.str('REPLICATE_API_TOKEN')
TELEGRAM_TOKEN = env.str('TELEGRAM_TOKEN')
BASE_DIR = Path(__file__).resolve().parent
