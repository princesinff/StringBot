from os import getenv
from dotenv import load_dotenv

load_dotenv()

# -------------------------------------------------------------
API_ID = "22084906"
# -------------------------------------------------------------
API_HASH = "4ea89573b2ffa4b66154c7cf8c6fdd48"
# -------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN")
# -------------------------------------------------------------
OWNER_ID = getenv("OWNER_ID", 7009601543)
# -------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/")
# -------------------------------------------------------------
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/PBX_CHAT")
# -------------------------------------------------------------
MUST_JOIN = getenv("MUST_JOIN","https://t.me/PBX_CHAT")
# -------------------------------------------------------------
