import os
import shutil
import asyncio
from git import Repo
from pyrogram.types import Message
from pyrogram import filters, Client
from git.exc import GitCommandError, InvalidGitRepositoryError
from AdityaHalder.modules.helpers.basics import edit_or_reply
from AdityaHalder.modules.helpers.filters import command
from AdityaHalder.utilities.misc import SUDOERS


@Client.on_message(command(["restart", "reboot"]) & filters.me)
async def restart(client, m: Message):
    reply = await m.edit("**🔁 Rᴇsᴛᴀʀᴛɪɴɢ 🔥 ...**")
    
    await reply.edit(
        "🥀 SᴜᴄᴄᴇssFᴜʟʟʏ RᴇSᴛᴀʀᴛᴇᴅ\nGᴇɴɪᴜs シ︎ UsᴇʀBᴏᴛ 🔥 ...\n\n💕 Pʟᴇᴀsᴇ Wᴀɪᴛ 1-2 MɪN Fᴏʀ\nLᴏᴀᴅ Usᴇʀ Pʟᴜɢɪɴs ✨ ...</b>"
    )
    os.system(f"kill -9 {os.getpid()} && python3 -m modules")





__MODULE__ = "Rᴇsᴛᴀʀᴛ"
__HELP__ = f"""
`.restart` **- Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ Tᴏ Rᴇsᴛᴀʀᴛ Gᴇɴɪᴜs UsᴇʀBᴏᴛ**

"""
