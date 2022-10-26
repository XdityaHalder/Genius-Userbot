from pyrogram import Client as Bot
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream
from AdityaHalder.config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION
from . import queues


client = Bot(STRING_SESSION, API_ID, API_HASH, plugins=dict(root="AdityaHalder.plugins"))
robot = Bot(":memory:", API_ID, API_HASH, bot_token=BOT_TOKEN)

pytgcalls = PyTgCalls(client)

@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: Update) -> None:
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
    else:
        await pytgcalls.change_stream(
            chat_id, 
            InputStream(
                InputAudioStream(
                    queues.get(chat_id)["file"],
                ),
            ),
        )

