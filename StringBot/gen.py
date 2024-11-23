from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from telethon import TelegramClient
from asyncio import TimeoutError
from telethon.sessions import StringSession
from telethon.errors import (
    ApiIdInvalidError, PhoneNumberInvalidError, PhoneCodeInvalidError,
    PhoneCodeExpiredError, SessionPasswordNeededError, PasswordHashInvalidError
)
from pyrogram.errors import (
    ApiIdInvalid, PhoneNumberInvalid, PhoneCodeInvalid,
    PhoneCodeExpired, SessionPasswordNeeded, PasswordHashInvalid
)
from asyncio.exceptions import TimeoutError
import config

ask_ques = "**「 Choose one option to generate a session 」**"
buttons_ques = [
    [
        InlineKeyboardButton("Pyrogram", callback_data="pyrogram"),
        InlineKeyboardButton("Telethon", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("Pyrogram v2", callback_data="pyrogram_v2"),
        InlineKeyboardButton("Pyrogram v3", callback_data="pyrogram_v3"),
    ],
    [
        InlineKeyboardButton("Pyrogram Bot", callback_data="pyrogram_bot"),
        InlineKeyboardButton("Telethon Bot", callback_data="telethon_bot"),
    ],
]

@Client.on_message(filters.private & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg: Message):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))

async def cancelled(msg):
    if msg.text.lower() in ["/cancel", "/restart"]:
        await msg.reply("**Process cancelled or restarted.**", reply_markup=InlineKeyboardMarkup(buttons_ques))
        return True
    return False

async def listen_for_input(bot, msg, prompt, timeout=300):
    """Prompt the user and wait for their response."""
    chat_id = msg.chat.id
    user_id = msg.from_user.id

    # Send the prompt message
    await bot.send_message(chat_id, prompt)

    # Wait for user input using an event listener
    try:
        await bot.send_message(chat_id, "❍ Time limit exceeded. Please try again.")
        return None
async def generate_session(bot, msg: Message, telethon=False, old_pyro=False, is_bot=False, pyro_v3=False):
    session_type = "Telethon" if telethon else "Pyrogram"
    if pyro_v3:
        session_type += " v3"
    elif not old_pyro:
        session_type += " v2"
    if is_bot:
        session_type += " Bot"

    await msg.reply(f"**Starting {session_type} session generation...**")

    # Ask for API ID
    api_id_msg = await listen_for_input(bot, msg, "❍ Please send your **API_ID** to proceed.\n\n❍ Click on /skip to use the bot's API.")
    if not api_id_msg or api_id_msg.text == "/skip":
        api_id, api_hash = config.API_ID, config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await msg.reply("**API_ID must be an integer! Restart the process.**", reply_markup=InlineKeyboardMarkup(buttons_ques))
            return
        api_hash_msg = await listen_for_input(bot, msg, "**Send your API_HASH:**")
        if not api_hash_msg:
            return
        api_hash = api_hash_msg.text

    # Ask for phone number or bot token
    phone_prompt = "**Enter your bot token (e.g., 12345:ABC):**" if is_bot else "**Enter your phone number (e.g., +123456789):**"
    phone_number_msg = await listen_for_input(bot, msg, phone_prompt)
    if not phone_number_msg:
        return
    phone_number = phone_number_msg.text

    # Initialize the client
    try:
        if telethon:
            client = TelegramClient(StringSession(), api_id, api_hash)
        else:
            client = Client("session", api_id=api_id, api_hash=api_hash, bot_token=phone_number if is_bot else None, in_memory=True)

        await client.connect()
        if not is_bot and telethon:
            await client.send_code_request(phone_number)
        elif not is_bot:
            await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply("**Invalid API_ID/API_HASH combination. Restart the process.**")
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply("**Invalid phone number. Restart the process.**")
        return

    # Handle OTP input
    if not is_bot:
        otp_msg = await listen_for_input(bot, msg, "**Enter the OTP received on your phone:**")
        if not otp_msg:
            return
        otp = otp_msg.text.strip()
        try:
            if telethon:
                await client.sign_in(phone_number, otp)
            else:
                await client.sign_in(phone_number, otp)
        except (PhoneCodeInvalid, PhoneCodeInvalidError):
            await msg.reply("**Invalid OTP. Restart the process.**")
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError):
            await msg.reply("**OTP expired. Restart the process.**")
            return

    # Generate session string
    try:
        session_string = client.session.save() if telethon else await client.export_session_string()
        await msg.reply(f"**Session generated successfully:**\n\n`{session_string}`\n\n**Keep it safe!**")
    finally:
        await client.disconnect()



