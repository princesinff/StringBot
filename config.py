import os
import re
from os import getenv
from dotenv import load_dotenv

load_dotenv()


API_ID = "6435225"
API_HASH = "4e984ea35f854762dcde906dce426c2d"

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = "mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/"

OWNER_ID = getenv("OWNER_ID", 7009601543)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/PBX_CHAT")

MUST_JOIN = getenv("MUST_JOIN", "https://t.me/PBX_CHAT")
