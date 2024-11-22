from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID
from config import SUPPORT_CHAT


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://files.catbox.moe/td0sdf.jpg",
        caption=f"""❍ ʜᴇʏ  {msg.from_user.mention}  ✤,
❍ ɪ ᴀᴍ{me2},

❍ Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

❍ ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

❍ ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [ʙᴀᴅ ᴹᵁᴺᴰᴬ](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text=""💢 ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ 💢", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("📂 sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ 📂", url=SUPPORT_CHAT),
                    InlineKeyboardButton("💫 ᴜᴘᴅᴀᴛᴇs 💫", url="https://t.me/HEROKUBIN_01")
                ],
                [
                    InlineKeyboardButton("📌sᴏᴜʀᴄᴇ 📌", url="https://github.com/Badhacker98/StringBot/fork"),
                    InlineKeyboardButton("🎵 ᴍᴜsɪᴄ ʙᴏᴛ 🎶", url="https://t.me/ShizuuMusicBot")
                ]                
            ]
        )
    )
