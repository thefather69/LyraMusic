#
# Copyright (C) 2022-2023 by NitricXd@Github, < https://github.com/NitricXd >.
#
# This file is part of < https://github.com/NitricXd/LyraMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/NitricXd/LyraMusic/blob/master/LICENSE >
#
# All rights reserved.
#

import os
import aiohttp
import aiofiles
from LyraMusic.plugins.xcodebots.thumbnail import generate_thumb

from config import MUSIC_BOT_NAME, YOUTUBE_IMG_URL

async def gen_thumb(videoid):
    return await generate_thumb(videoid,MUSIC_BOT_NAME)
