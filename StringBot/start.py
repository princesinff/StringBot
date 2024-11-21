from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID
from config import SUPPORT_CHAT


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""ʜᴇʏ {message.from_user.first_name},\n\n๏ ɪ ᴀᴍ ᴛʀᴜꜱᴛᴇᴅ ꜱᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ꜰᴜʟʟʏ ꜱᴀꜰᴇ & ꜱᴇᴄᴜʀᴇ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.""",
        [
        [InlineKeyboardButton(text="💢 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 💢", callback_data="generate")],
        [
            InlineKeyboardButton(text="📂 sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ 📂", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="📌sᴏᴜʀᴄᴇ ", url="https://github.com/Badhacker98/StringBot"
            ),
        ],
    ]
        disable_web_page_preview=True,
        )
