import asyncio
import os
import time
from os import listdir, mkdir

import heroku3
from aiohttp import ClientSession
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from rich.console import Console
from rich.table import Table
from motor.motor_asyncio import AsyncIOMotorClient as KaalXD

from AdityaHalder.config import MONGO_DB_URL, LOG_GROUP_ID, OWNER_ID, STRING_SESSION, SUDO_USERS, UPSTREAM_BRANCH, UPSTREAM_REPO
from AdityaHalder.modules.clientbot.clientbot import client, robot, pytgcalls
from AdityaHalder.utilities.misc import sudo
from AdityaHalder.utilities.times import time_to_seconds
from AdityaHalder.utilities.tasks import install_requirements


loop = asyncio.get_event_loop()
console = Console()


### Heroku Shit
UPSTREAM_BRANCH = UPSTREAM_BRANCH
UPSTREAM_REPO = UPSTREAM_REPO

### Modules
MOD_LOAD = []
MOD_NOLOAD = []

### Mongo DB
MONGODB_CLI = KaalXD(MONGO_DB_URL)
db = MONGODB_CLI.Aditya

### Sudo Users
sudo()

### Boot Time
boottime = time.time()

### Clients
aiohttpsession = ClientSession()
robot = robot
pytgcalls = pytgcalls

### Config
SUDOERS = SUDO_USERS
OWNER_ID = OWNER_ID
LOG_GROUP_ID = LOG_GROUP_ID

### Bot Info
BOT_ID = 0
BOT_NAME = ""
BOT_USERNAME = ""

### Assistant Info
ASSIDS = []
ASSID = 0
ASSNAME = ""
ASSUSERNAME = ""
ASSMENTION = ""
random_assistant = []


async def initiate_bot():
    global SUDOERS, OWNER_ID, ASSIDS
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global ASSID, ASSNAME, ASSMENTION, ASSUSERNAME
    global Heroku_cli, Heroku_app
    os.system("clear")
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(
        "Genius Userbot : Best Ever Userbot"
    )
    console.print(header)
    with console.status(
        "[magenta] Genius UserBot Booting...",
    ) as status:
        console.print("┌ [red]Booting Up The Bot Clients...\n")
        await robot.start()
        console.print("└ [green]Booted Bot Client")
        console.print("\n┌ [red]Booting Up The User Client...")
        if STRING_SESSION != "None":
            await pytgcalls.start()
            random_assistant.append(1)
            console.print("├ [yellow]Booted User Client")
        
        console.print("└ [green]All Client Bots Booted Successfully!")
        if "raw_files" not in listdir():
            mkdir("raw_files")
        if "downloads" not in listdir():
            mkdir("downloads")
        if "cache" not in listdir():
            mkdir("cache")
        if "search" not in listdir():
            mkdir("search")
        console.print("\n┌ [red]Loading Clients Information...")
        getme = await robot.get_me()
        BOT_ID = getme.id
        if getme.last_name:
            BOT_NAME = getme.first_name + " " + getme.last_name
        else:
            BOT_NAME = getme.first_name
        BOT_USERNAME = getme.username
        if STRING_SESSION != "None":
            getme = await client.get_me()
            ASSID = getme.id
            ASSIDS.append(ASSID)
            ASSNAME = (
                f"{getme.first_name} {getme.last_name}"
                if getme.last_name
                else getme.first_name
            )
            ASSUSERNAME = getme.username
            ASSMENTION = getme.mention
        console.print("└ [green]Loaded Clients Information!")
        try:
            repo = Repo()
        except GitCommandError:
            console.print("┌ [red] Checking Git Updates!")
            console.print("└ [red]Git Command Error\n")
            return
        except InvalidGitRepositoryError:
            console.print("┌ [red] Checking Git Updates!")
            repo = Repo.init()
            if "origin" in repo.remotes:
                origin = repo.remote("origin")
            else:
                origin = repo.create_remote("origin", UPSTREAM_REPO)
            origin.fetch()
            repo.create_head(UPSTREAM_BRANCH, origin.refs[UPSTREAM_BRANCH])
            repo.heads[UPSTREAM_BRANCH].set_tracking_branch(
                origin.refs[UPSTREAM_BRANCH]
            )
            repo.heads[UPSTREAM_BRANCH].checkout(True)
            try:
                repo.create_remote("origin", UPSTREAM_REPO)
            except BaseException:
                pass
            nrs = repo.remote("origin")
            nrs.fetch(UPSTREAM_BRANCH)
            try:
                nrs.pull(UPSTREAM_BRANCH)
            except GitCommandError:
                repo.git.reset("--hard", "FETCH_HEAD")
            await install_requirements(
                "pip3 install --no-cache-dir -r Installer"
            )
            console.print("└ [red]Git Client Update Completed\n")


loop.run_until_complete(initiate_bot())


def init_db():
    global db_mem
    db_mem = {}


init_db()
