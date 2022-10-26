import asyncio
from pyrogram import filters, Client
from pyrogram.methods import messages
from AdityaHalder.modules.helpers.filters import command
from AdityaHalder.modules.helpers.program import get_arg, denied_users
import AdityaHalder.modules.databases.pmpermit_db as Kaal

FLOOD_CTRL = 0
ALLOWED = []
USERS_AND_WARNS = {}


@Client.on_message(command(["pmguard", "antipm"]) & filters.me)
async def antipm(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**I only understand on or off**")
        return
    if arg == "off":
        await Kaal.set_pm(False)
        await message.edit("**PM Guard Deactivated**")
    if arg == "on":
        await Kaal.set_pm(True)
        await message.edit("**PM Guard Activated**")




@Client.on_message(command("setlimit") & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**Set limit to what?**")
        return
    await Kaal.set_limit(int(arg))
    await message.edit(f"**Limit set to {arg}**")


@Client.on_message(command("setpmmsg") & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**What message to set**")
        return
    if arg == "default":
        await Kaal.set_permit_message(Kaal.PMPERMIT_MESSAGE)
        await message.edit("**Anti_PM message set to default**.")
        return
    await Kaal.set_permit_message(f"`{arg}`")
    await message.edit("**Custom anti-pm message set**")


@Client.on_message(command("setblockmsg") & filters.me)
async def setblkmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**What message to set**")
        return
    if arg == "default":
        await Kaal.set_block_message(Kaal.BLOCKED)
        await message.edit("**Block message set to default**.")
        return
    await Kaal.set_block_message(f"`{arg}`")
    await message.edit("**Custom block message set**")


@Client.on_message(command(["allow", "ap", "approve", "a"]) & filters.me & filters.private)
async def allow(client, message):
    chat_id = message.chat.id
    pmpermit, pm_message, limit, block_message = await Kaal.get_pm_settings()
    await Kaal.allow_user(chat_id)
    await message.edit(f"**I have allowed [you](tg://user?id={chat_id}) to PM me.**")
    async for message in app.search_messages(
        chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
    ):
        await message.delete()
    USERS_AND_WARNS.update({chat_id: 0})


@Client.on_message(command(["deny", "da", "dap", "disapprove", "dapp"]) & filters.me & filters.private)
async def deny(client, message):
    chat_id = message.chat.id
    await Kaal.deny_user(chat_id)
    await message.edit(f"**I have denied [you](tg://user?id={chat_id}) to PM me.**")


@Client.on_message(
    filters.private
    & filters.create(denied_users)
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
)
async def reply_pm(app: Client, message):
    global FLOOD_CTRL
    pmpermit, pm_message, limit, block_message = await Kaal.get_pm_settings()
    user = message.from_user.id
    user_warns = 0 if user not in USERS_AND_WARNS else USERS_AND_WARNS[user]
    if user_warns <= limit - 2:
        user_warns += 1
        USERS_AND_WARNS.update({user: user_warns})
        if not FLOOD_CTRL > 0:
            FLOOD_CTRL += 1
        else:
            FLOOD_CTRL = 0
            return
        async for message in app.search_messages(
            chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
        ):
            await message.delete()
        await message.reply(pm_message, disable_web_page_preview=True)
        return
    await message.reply(block_message, disable_web_page_preview=True)
    await app.block_user(message.chat.id)
    USERS_AND_WARNS.update({user: 0})




__MODULE__ = "Aɴᴛɪ Pᴍ"
__HELP__ = f""" Tʜɪs Mᴏᴅᴜʟᴇ Oɴʟʏ Fᴏʀ Bᴏᴛ Oᴡɴᴇʀ

`.pmguard [on or off]` - Aᴄᴛɪᴠᴀᴛᴇ Oʀ Dᴇᴀᴄᴛɪᴠᴀᴛᴇ Aɴᴛɪ-Pᴍ

`.setpmmsg [message or default]` - Sᴇᴛ Cᴜsᴛᴏᴍ Pᴍ Mᴇssᴀɢᴇ

`.setblockmsg [message or default]` - Sᴇᴛ Cᴜsᴛᴏᴍ Bʟᴏᴄᴋ Mᴇssᴀɢᴇ

`.setlimit [value]` - Sᴇᴛ Mᴀxɪᴍᴜᴍ Pᴍ Mᴇssᴀɢᴇ Lɪᴍɪᴛ.
Ex:- `.setlimit 3` [Dᴇғᴀᴜʟᴛ Vᴀʟᴜᴇ - 5]

`.a/.allow` - Aᴘᴘʀᴏᴠᴇ Aɴ Usᴇʀ Tᴏ Mᴇssᴀɢᴇ.

`.da/.deny` - Dɪs-Aᴘᴘʀᴏᴠᴇ Aɴ Usᴇʀ Tᴏ Mᴇssᴀɢᴇ.

**ɴᴏᴛᴇ:**
-Sᴜᴅᴏ Usᴇʀ Cᴀɴ'ᴛ Cᴏɴᴛʀᴏʟ Tʜɪs Pʟᴜɢɪɴ
"""
