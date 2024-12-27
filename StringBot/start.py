from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, WebAppInfo

from config import OWNER_ID, SUPPORT_CHAT

@Client.on_message(filters.command("start") & filters.private & filters.incoming)
async def start(client, message: Message):
    me2 = (await client.get_me()).mention
    buttons = [
        [
            InlineKeyboardButton(
                "▪️ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ▪️",
                callback_data="generate_session"
            )
        ],
        [
            InlineKeyboardButton("▪️sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ▪️", url=SUPPORT_CHAT),
            InlineKeyboardButton("▪️ᴜᴘᴅᴀᴛᴇs ▪️", url="https://t.me/HEROKUBIN_01")
        ],
        [
            InlineKeyboardButton("▪️ sᴏᴜʀᴄᴇ ▪️", url="https://github.com/Badhacker98/StringBot/fork"),
            InlineKeyboardButton("▪️ ᴍᴜsɪᴄ ʙᴏᴛ ▪️", url="https://t.me/Gaana_MusicBot")
        ]
    ]

    # Send a message to the user who started the bot
    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://files.catbox.moe/bl1can.jpg",
        caption=f"""❍ ʜᴇʏ {message.from_user.mention} 
        
❍ ɪ ᴀᴍ {me2}

❍ Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ᴛᴏᴏʟꜱ.

❍ ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴏɴ 'ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇ' ᴛᴏ ꜱᴛᴀʀᴛ.

❍ ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [⏤͟͟͞͞🥀➣Bᴀᴅ❤︎ ᴍᴜɴᴅᴀ ➻ >•⏤͟͟͞͞‌](tg://user?id={OWNER_ID}) """,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

    # Notify the owner about the new user
    await client.send_message(
        chat_id=OWNER_ID,
        text=f"❍ ɴᴇᴡ ᴜsᴇʀ ꜱᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ\n\n❍ ᴜsᴇʀɴᴀᴍᴇ: @{message.from_user.username or 'N/A'}\n❍ ɴᴀᴍᴇ: {message.from_user.first_name} {message.from_user.last_name or ''}\n❍ ᴜsᴇʀ ɪᴅ: `{message.from_user.id}`"
    )

@Client.on_callback_query(filters.regex("generate_session"))
async def generate_session(client, callback_query):
    buttons = [
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
        text="❖ ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴀ ᴏᴘᴛɪᴏɴ \n❖ API_ID : `25742938`\n❖ API_HASH : `b35b715fe8dc0a58e8048988286fc5b6`",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
