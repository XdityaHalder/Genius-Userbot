from pyrogram import filters, Client
from traceback import format_exc
from typing import Tuple
import asyncio
import random
from pyrogram import Client
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import (
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message)
from AdityaHalder.config import *
from AdityaHalder.modules.helpers.filters import *
from AdityaHalder.modules.helpers.decorators import errors, sudo_users_only
from AdityaHalder.modules.helpers.program import get_arg
from AdityaHalder.modules.helpers.admins import CheckAdmin


@Client.on_message(command("gcast"))
@errors
@sudo_users_only
async def gbroadcast(client: Client, message: Message):
    msg_ = await message.edit_text("`Processing..`")
    failed = 0
    if not message.reply_to_message:
        await msg_.edit("`Reply To Message Boss!`")
        return
    chat_dict = await iter_chats(client)
    chat_len = len(chat_dict)
    await msg_.edit("`Now Sending To All Chats Possible!`")
    if not chat_dict:
        msg_.edit("`You Have No Chats! So Sad`")
        return
    for c in chat_dict:
        try:
            msg = await message.reply_to_message.copy(c)
        except:
            failed += 1
    await msg_.edit(
        f"`Message Sucessfully Send To {chat_len-failed} Chats! Failed In {failed} Chats.`"
    )


__MODULE__ = "Gʟᴏʙᴀʟ"
__HELP__ = f"""
**🥀 Gʙᴀɴ & Gᴍᴜᴛᴇ Mᴏᴅᴜʟᴇ ✨**

**ᴜsᴀɢᴇ:**
`.gmute` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Gᴍᴜᴛᴇ.**

`.ungmute` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ UɴGᴍᴜᴛᴇ.**

`.gban` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Gʙᴀɴ.**

`.ungban` - ** Rᴇᴘʟʏ Tᴏ Aɴʏᴏɴᴇ Wɪᴛʜ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ UɴGʙᴀɴ.**

`.gcast` - ** Rᴇᴘʟʏ Tᴏ Aɴʏ Mᴇssᴀɢᴇ Tᴏ Gʟᴏʙᴀʟʏ Bʀᴏᴀᴅᴄᴀsᴛ**
"""
