# Copyright (C) 2024 by Badhacker98@Github, < https://github.com/Badhacker98 >.
#
# This file is part of < https://github.com/Badhacker98/StringBot > project,
# and is released under the license agreement specified in:
# < https://github.com/Badhacker98/StringBot/blob/main/LICENSE >
#
# All rights reserved.

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

import config


mongo = MongoCli(config.MONGO_DB_URI)
db = mongo.StringGen

from .users import *
from .bot_users import *
