import asyncio
import importlib
import os
import re

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pytgcalls import idle
from rich.console import Console
from rich.table import Table
from youtubesearchpython import VideosSearch

from Royalboycoder.config import LOG_GROUP_ID, STRING_SESSION
from Royalboycoder import client, robot, pytgcalls, ASSID, ASSNAME, BOT_ID, BOT_NAME, OWNER_ID
from Royalboycoder.modules.helpers.filters import command
from Royalboycoder.modules.helpers.decorators import errors, sudo_users_only
from Royalboycoder.plugins import ALL_MODULES
from Royalboycoder.utilities.inline import paginate_modules
from Royalboycoder.utilities.misc import SUDOERS

loop = asyncio.get_event_loop()
console = Console()
HELPABLE = {}


async def initiate_bot():
    with console.status(
        "[magenta] Finalizing Booting...",
    ) as status:
        status.update(
            status="[bold blue]Scanning for Plugins", spinner="earth"
        )
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]Importing Plugins...",
            spinner="bouncingBall",
            spinner_style="yellow",
        )
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module(
                "AdityaHalder.plugins." + all_module
            )
            if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
            ):
                imported_module.__MODULE__ = imported_module.__MODULE__
                if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
                ):
                    HELPABLE[
                        imported_module.__MODULE__.lower()
                    ] = imported_module
            console.print(
                f">> [bold cyan]Successfully imported: [green]{all_module}.py"
            )
        console.print("")
        status.update(
            status="[bold blue]Importation Completed!",
        )
    console.print(
        "[bold green] 🥀 𝐑𝐨𝐲𝐚𝐥 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 ✨\n"
    )
    try:
        await robot.send_message(
            LOG_GROUP_ID,
            "<b> 🥀 𝐑𝐨𝐲𝐚𝐥 𝐔𝐬𝐞𝐫𝐁𝐨𝐭 𝐢𝐬 𝐇𝐞𝐫𝐞 ✨</b>",
        )
    except Exception as e:
        print(
            "\n𝐁𝐨𝐭. 𝐇𝐚𝐬 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐀𝐜𝐜𝐞𝐬𝐬 𝐓𝐡𝐞 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩, 𝐁𝐞 𝐒𝐮𝐫𝐞 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐝𝐝𝐞𝐝 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐋𝐨𝐠 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐀𝐧𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐞𝐝 𝐀𝐬 𝐀𝐝𝐦𝐢𝐧❗"
        )
        console.print(f"\n[red] Stopping Bot")
        return
    a = await robot.get_chat_member(LOG_GROUP_ID, BOT_ID)
    if a.status != "administrator":
        print("Promote Bot As Admin in Logger Group")
        console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
        return
    console.print(f"\n┌[red] Bot Started as {BOT_NAME}")
    console.print(f"├[green] ID :- {BOT_ID}")
    if STRING_SESSION != "None":
        try:
            await client.send_message(
                LOG_GROUP_ID,
                "<b>🥀 𝐑𝐨𝐲𝐚𝐥 𝐔𝐬𝐞𝐫𝐁𝐨𝐭 𝐢𝐬 𝐀𝐜𝐭𝐢𝐯𝐞 ✨</b>",
            )
        except Exception as e:
            print(
                "\n𝐔𝐬𝐞𝐫𝐁𝐨𝐭 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐇𝐚𝐬 𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐀𝐜𝐜𝐞𝐬𝐬 𝐓𝐡𝐞 𝐋𝐨𝐠 𝐆𝐫𝐨𝐮𝐩.❗"
            )
            console.print(f"\n[red] Stopping Bot")
            return
        try:
            await client.join_chat("RoyalServer")
            await client.join_chat("RoyalChatGroup")
        except:
            pass
        console.print(f"├[red] UserBot Started as {ASSNAME}")
        console.print(f"├[green] ID :- {ASSID}")
        console.print(f"└[red] ✅ Royal UserBot Boot Complete 💯 ...")
        await idle()
        console.print(f"\n[red] Userbot Stopped")


home_text_pm = f"""**ʜᴇʟʟᴏ ,
ᴍʏ ɴᴀᴍᴇ ɪs {BOT_NAME}.
I Aᴍ ʀᴏʏᴀʟ, Aɴ Aᴅᴠᴀɴᴄᴇᴅ UsᴇʀBᴏᴛ Wɪᴛʜ Sᴏᴍᴇ Usᴇғᴜʟ Fᴇᴀᴛᴜʀᴇs.**"""


@robot.on_message(command(["start"]) & filters.private)
async def start(_, message):
    await message.reply_photo(
        photo=f"",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 Hᴇʟʟᴏ, I Aᴍ ʀᴏʏᴀʟ ᴜsᴇʀʙᴏᴛ » Aɴ Aᴅᴠᴀɴᴄᴇᴅ
Pʀᴇᴍɪᴜᴍ Tᴇʟᴇɢʀᴀᴍ Usᴇʀ Bᴏᴛ.

┏━━━━━━━━━━━━━━━━━━━┓
┣★ Oᴡɴᴇʀ'xD ›> : [ʀᴏʏᴀʟ ʙᴏʏ ᴀᴍɪᴛ](https://t.me/royal_boy_amit)
┣★ Uᴘᴅᴀᴛᴇs ›› : [ʀᴏʏᴀʟ Sᴇʀᴠᴇʀ](https://t.me/royalkifeelings)
┣★ Sᴜᴘᴘᴏʀᴛ >> : [ʀᴏʏᴀʟ ᴄʜᴀᴛ ɢʀᴏᴜᴘ](https://t.me/royalkifeelings12)
┗━━━━━━━━━━━━━━━━━━━┛

💞 Cʟɪᴄᴋ Oɴ Dᴇᴘʟᴏʏ Bᴜᴛᴛᴏɴ Tᴏ Mᴀᴋᴇ
Yᴏᴜʀ Oᴡɴ » ʀᴏʏᴀʟ Usᴇʀ Bᴏᴛ.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Dᴇᴘʟᴏʏ ʀᴏʏᴀʟ UsᴇʀBᴏᴛ ✨", url=f"https://github.com/royalboycoder/Royal-Userbot-Repo")
                ]
                
           ]
        ),
    )
    
    
    
@robot.on_message(command(["help"]) & SUDOERS)
async def help_command(_, message):
    text, keyboard = await help_parser(message.from_user.mention)
    await robot.send_message(LOG_GROUP_ID, text, reply_markup=keyboard)




async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
        """**🥀 Wᴇʟᴄᴏᴍᴇ Tᴏ Hᴇʟᴘ Mᴇɴᴜ Oғ :
ʀᴏʏᴀʟ UsᴇʀBᴏᴛ 🔥...

💞 Jᴜsᴛ Cʟɪᴄᴋ Oɴ Bᴇʟᴏᴡ Iɴʟɪɴᴇ
Tᴏ Gᴇᴛ ʀᴏʏᴀʟ ᴜsᴇʀʙᴏᴛ  Cᴏᴍᴍᴀɴᴅs ✨...**
""".format(
            first_name=name
        ),
        keyboard,
    )

@robot.on_callback_query(filters.regex("close") & SUDOERS)
async def close(_, CallbackQuery):
    await CallbackQuery.message.delete()

@robot.on_callback_query(filters.regex("aditya") & SUDOERS)
async def aditya(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await CallbackQuery.message.edit(text, reply_markup=keyboard)


@robot.on_callback_query(filters.regex(r"help_(.*?)") & SUDOERS)
async def help_button(client, query):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = f"""**🥀 Wᴇʟᴄᴏᴍᴇ Tᴏ Hᴇʟᴘ Mᴇɴᴜ Oғ :
ʀᴏʏᴀʟ ᴜsᴇʀʙᴏᴛ 🔥...

💞 Jᴜsᴛ Cʟɪᴄᴋ Oɴ Bᴇʟᴏᴡ Iɴʟɪɴᴇ
Tᴏ Gᴇᴛ ʀᴏʏᴀʟ ᴜsᴇʀʙᴏᴛ Cᴏᴍᴍᴀɴᴅs ✨...**
 """
    if mod_match:
        module = mod_match.group(1)
        text = (
            "{} **{}**:\n".format(
                "**🥀 Wᴇʟᴄᴏᴍᴇ Tᴏ Hᴇʟᴘ Mᴇɴᴜ Oғ :** ", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
        )
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="↪️ 𝐁𝐚𝐜𝐤", callback_data="help_back"
                    ),
                    InlineKeyboardButton(
                        text="🔄 𝐂𝐥𝐨𝐬𝐞", callback_data="close"
                    ),
                ],
            ]
        )

        await query.message.edit(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    elif home_match:
        out = private_panel()
        await robot.send_message(
            query.from_user.id,
            text=home_text_pm,
            reply_markup=InlineKeyboardMarkup(out[1]),
        )
        await query.message.delete()
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit(
            text=text,
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )

    return await client.answer_callback_query(query.id)


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
