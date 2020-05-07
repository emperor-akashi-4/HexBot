from telethon import events
import asyncio
import os
import sys
from userbot.utils import admin_cmd


@borg.on(admin_cmd("restart"))
async def _(event):
    if event.fwd_from:
        return
    # await asyncio.sleep(2)
    # await event.edit("Restarting\nType `.ping` or `.alive` After Some Time!")
    # await asyncio.sleep(2)
    # await event.edit("Restarting\nType `.ping` or `.alive` After Some Time!")
    # await asyncio.sleep(2)
    await event.edit("Restarted!\nType `.ping` or `.alive`!")
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@borg.on(admin_cmd("shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Disabling Dyno!\nOpen Heroku And Enable Dyno To Use HexBot Again!")
    await borg.disconnect()
