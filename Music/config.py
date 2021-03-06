##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
get_queue = {}
SESSION_NAME = getenv('SESSION_NAME', 'kabos')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "10470922"))
API_HASH = getenv('API_HASH')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '30'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '').split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001655300809'))
ASS_ID = int(getenv("ASS_ID", '5362243403'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '').split()))
BOT_IMG = getenv("BOT_IMG")
GROUP = getenv("GROUP", None)
CHANNEL = getenv("CHANNEL", None)
