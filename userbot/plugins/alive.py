import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba, check pinned in @XtraTgBot"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Gracias! HexBot Is Up And Running!`"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n`"
                     "`Bot created by:` [Akashi](tg://user?id=1213031275)\n"
                     f"`Forked By`: {DEFAULTUSER}")
