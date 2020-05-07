from coffeehouse.lydia import LydiaAI
from coffeehouse.api import API
import asyncio
from telethon import events

# Non-SQL Mode
ACC_LYDIA = {}

if Var.LYDIA_API_KEY:
    api_key = Var.LYDIA_API_KEY
    api_client = API(api_key)
    lydia = LydiaAI(api_client)

@command(pattern="^.repcf", outgoing=True)
async def repcf(event):
    if event.fwd_from:
        return
    await event.edit("Processing...")
    try:
        session = lydia.create_session()
        session_id = session.id
        reply = await event.get_reply_message()
        msg = reply.text
        text_rep = session.think_thought(msg)
        await event.edit("Hey: {0}".format(text_rep))
    except Exception as e:
        await event.edit(str(e))

@command(pattern="^.addcf", outgoing=True)
async def addcf(event):
    if event.fwd_from:
        return
    await event.edit("Enabling Lydia!")
    await asyncio.sleep(3)
    await event.edit("Processing...")
    reply_msg = await event.get_reply_message()
    if reply_msg:
        session = lydia.create_session()
        session_id = session.id
        if reply_msg.from_id is None:
            return await event.edit("Invalid user type.")
        ACC_LYDIA.update({(event.chat_id & reply_msg.from_id): session})
        await event.edit("`Lydia Enabled Successfully!`")
    else:
        await event.edit("Reply To A User To Activate Lydia AI On Them!")

@command(pattern="^.remcf", outgoing=True)
async def remcf(event):
    if event.fwd_from:
        return
    await event.edit("Disabling Lydia!")
    await asyncio.sleep(3)
    await event.edit("Processing...")
    reply_msg = await event.get_reply_message()
    try:
        del ACC_LYDIA[event.chat_id & reply_msg.from_id]
        await event.edit("`Lydia Disbaled Successfully!`")
    except Exception:
        await event.edit("Lydia Not Activated For User!")


@bot.on(events.NewMessage(incoming=True))
async def user(event):
    user_text = event.text
    try:
        session = ACC_LYDIA[event.chat_id & event.from_id]
        msg = event.text
        async with event.client.action(event.chat_id, "typing"):
            text_rep = session.think_thought(msg)
            wait_time = 0
            for i in range(len(text_rep)):
                wait_time = wait_time + 0.1
            await asyncio.sleep(wait_time)
            await event.reply(text_rep)
    except (KeyError, TypeError):
        return
