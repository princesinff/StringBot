# Copyright (C) 2024 by Badhacker98@Github, < https://github.com/Badhacker98 >.
#
# This file is part of < https://github.com/Badhacker98/StringBot > project,
# and is released under the license agreement specified in:
# < https://github.com/Badhacker98/StringBot/blob/main/LICENSE >
#
# All rights reserved.

from StringBot.utils import db

usersdb = db.users


async def is_served_user(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def get_served_users() -> list:
    users_list = []
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list


async def add_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await usersdb.insert_one({"user_id": user_id})
