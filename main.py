import config
import time
import logging
import sys
from pyrogram import Client, idle
from pyromod import listen  # Ab ye properly work karega
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

StartTime = time.time()

app = Client(
    "Anonymous",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="StringBot"),
)

if __name__ == "__main__":
    print("StringBot Starting...")
    try:
        app.start()
    except ApiIdInvalid:
        print("Error: Invalid API_ID or API_HASH. Please check config.py")
        sys.exit(1)
    except ApiIdPublishedFlood:
        print("Error: API_ID is reported as spam. Use a new API_ID.")
        sys.exit(1)
    except AccessTokenInvalid:
        print("Error: Invalid BOT_TOKEN. Please check config.py")
        sys.exit(1)

    try:
        uname = app.get_me().username
        print(f"@{uname} Started Successfully!")
    except Exception as e:
        print(f"Error getting bot username: {e}")
        sys.exit(1)

    idle()  # Keep bot running
    app.stop()
    print("Stopping StringBot...")
