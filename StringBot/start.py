from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, WebAppInfo

from config import OWNER_ID, SUPPORT_CHAT

API_ID = "25742938"
API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"


@Client.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message: Message):
    me2 = (await client.get_me()).mention
    buttons = [
        [
            InlineKeyboardButton("💢 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 💢", callback_data="generate_session")
        ],
        [
            InlineKeyboardButton("📂 sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ 📂", url=SUPPORT_CHAT),
            InlineKeyboardButton("💫 ᴜᴘᴅᴀᴛᴇs 💫", url="https://t.me/HEROKUBIN_01")
        ],
        [
            InlineKeyboardButton("📌 sᴏᴜʀᴄᴇ 📌", url="https://github.com/Badhacker98/StringBot/fork"),
            InlineKeyboardButton("🎵 ᴍᴜsɪᴄ ʙᴏᴛ 🎶", url="https://t.me/Gaana_MusicBot")
        ]
    ]

    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://files.catbox.moe/td0sdf.jpg",
        caption=f"""❍ ʜᴇʏ {message.from_user.mention} ✤,
❍ ɪ ᴀᴍ {me2},

❍ Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ᴛᴏᴏʟꜱ.

❍ ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴏɴ 'ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇ' ᴛᴏ ꜱᴛᴀʀᴛ.

❍ ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [ʙᴀᴅ ᴹᵁᴺᴰᴬ](tg://user?id={OWNER_ID})!""",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex("generate_session"))
async def generate_session(client, callback_query):
    buttons = [
        [
            InlineKeyboardButton("🔑 Copy API_ID", callback_data="copy_api_id"),
            InlineKeyboardButton("🔑 Copy API_HASH", callback_data="copy_api_hash")
        ],
        [
            InlineKeyboardButton(
                "ᴘʏʀᴏɢʀᴀᴍ 💻",
                web_app=WebAppInfo(url="https://telegram.tools/session-string-generator#pyrogram,user")
            ),
            InlineKeyboardButton(
                "ᴛᴇʟᴇᴛʜᴏɴ 💻",
                web_app=WebAppInfo(url="https://telegram.tools/session-string-generator#telethon,user")
            )
        ]
    ]

    await callback_query.message.edit_text(
        text=f"❖ ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴀ ᴏᴘᴛɪᴏɴ \n❖ API_ID: {API_ID}\n❖ API_HASH: {API_HASH}",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex("copy_api_id"))
async def copy_api_id(client, callback_query):
    await callback_query.answer(f"Copied API_ID: {25742938}", show_alert=True)


@Client.on_callback_query(filters.regex("copy_api_hash"))
async def copy_api_hash(client, callback_query):
    await callback_query.answer(f"Copied API_HASH: {b35b715fe8dc0a58e8048988286fc5b6}", show_alert=True)
