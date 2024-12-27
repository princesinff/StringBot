from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, WebAppInfo

from config import OWNER_ID, SUPPORT_CHAT

@Client.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message: Message):
    me2 = (await client.get_me()).mention
    buttons = [
        [
            InlineKeyboardButton(
                "String Session Generate",
                callback_data="generate_session"
            )
        ],
        [
            InlineKeyboardButton("📂 Support Chat 📂", url=SUPPORT_CHAT),
            InlineKeyboardButton("💫 Updates 💫", url="https://t.me/HEROKUBIN_01")
        ],
        [
            InlineKeyboardButton("📌 Source 📌", url="https://github.com/Badhacker98/StringBot/fork"),
            InlineKeyboardButton("🎵 Music Bot 🎶", url="https://t.me/Gaana_MusicBot")
        ]
    ]

    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://files.catbox.moe/td0sdf.jpg",
        caption=f"""❍ ʜᴇʏ {message.from_user.mention} ✤,
❍ ɪ ᴀᴍ {me2},

❍ Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

❍ ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴏɴ 'ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇ' ᴛᴏ ꜱᴛᴀʀᴛ.

❍ ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [ʙᴀᴅ ᴹᵁᴺᴰᴬ](tg://user?id={OWNER_ID})!""",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex("generate_session"))
async def generate_session(client, callback_query):
    buttons = [
        [
            InlineKeyboardButton(
                "Pyrogram",
                web_app=WebAppInfo(url="https://telegram.tools/session-string-generator#pyrogram,user")
            ),
            InlineKeyboardButton(
                "Telethon",
                web_app=WebAppInfo(url="https://telegram.tools/session-string-generator#telethon,user")
            )
        ]
    ]

    await callback_query.message.edit_text(
        text="Select the Python library for which you want to generate a string session. It will open in a mini web app:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
