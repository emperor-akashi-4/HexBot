import asyncio
import time
from asyncio import wait
from userbot.utils import admin_cmd
from telethon import events


@borg.on(events.NewMessage(pattern=r"\.spam", outgoing=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])

        await wait(
            [e.respond(spam_message) for i in range(counter)]
            )

        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP,
                "#SPAM \n\n"
                "Spam was executed successfully"
                )
                
@borg.on(admin_cmd("tspam"))
async def tmeme(e):
     tspam = str(e.text[7:])
     message = tspam.replace(" ", "")
     for letter in message:
         await e.respond(letter)
     await e.delete()