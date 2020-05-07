from telethon import events
import asyncurban
from userbot.utils import admin_cmd


@borg.on(admin_cmd("ud (.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("processing...")
    word = event.pattern_match.group(1)
    urban = asyncurban.UrbanDictionary()
    try:
        mean = await urban.get_word(word)
        await event.edit("Text: **{}**\n\nMeaning: **{}**\n\nExample: __{}__".format(mean.word, mean.definition, mean.example))
    except asyncurban.WordNotFoundError:
        await event.edit("No result found for **" + word + "**")
