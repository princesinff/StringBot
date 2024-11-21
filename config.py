import os
import re
from os import getenv
from dotenv import load_dotenv

load_dotenv()


API_ID = "6435225"
API_HASH = "4e984ea35f854762dcde906dce426c2d"

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID", 7009601543))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/PBX_CHAT")

MUST_JOIN = getenv("MUST_JOIN", "https://t.me/PBX_CHAT")
