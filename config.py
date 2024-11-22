from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","6435225"))

API_HASH = getenv("API_HASH","4e984ea35f854762dcde906dce426c2d")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/")

MUST_JOIN = getenv("MUST_JOIN","https://t.me/PBX_CHAT")
