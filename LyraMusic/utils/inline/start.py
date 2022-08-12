#
# Copyright (C) 2022-2023 by NitricXd@Github, < https://github.com/NitricXd >.
#
# This file is part of < https://github.com/NitricXd/LyraMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/NitricXd/LyraMusic/blob/master/LICENSE >
#
# All rights reserved.
#

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO
from LyraMusic import app


def start_pannel(_):
    return


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):   
    return 