from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, WebAppInfo


@Client.on_message(filters.command(["genrate", "gen" ,"generate"]) & filters.private & filters.incoming)
async def generate(client, message: Message):
    me2 = (await client.get_me()).mention
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

    await message.reply_text(
        text=f"""❍ ʜᴇʏ {message.from_user.mention} ✤
        
❍ ɪ ᴀᴍ {me2},

❍ ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴀɴ ᴏᴘᴛɪᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ꜱᴛᴀʀᴛ.

❖ API_ID : `25742938`
❖ API_HASH : `b35b715fe8dc0a58e8048988286fc5b6`""",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
