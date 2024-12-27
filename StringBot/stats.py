# Copyright (C) 2024 by Badhacker98@Github, < https://github.com/Badhacker98 >.
#
# This file is part of < https://github.com/Badhacker98/StringBot > project,
# and is released under the license agreement specified in:
# < https://github.com/Badhacker98/StringBot/blob/main/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client, filters

from config import OWNER_ID
from StringBot.utils import get_served_users


@Client.on_message(filters.command(["stats", "users"]) & filters.user(OWNER_ID))
async def get_stats(_, message: Message):
    users = len(await get_served_users())
    await message.reply_text(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ {Bad.name} :\n\n {users} ᴜsᴇʀs")
