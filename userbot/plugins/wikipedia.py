from telethon import events
import wikipedia
from userbot.utils import admin_cmd


@borg.on(admin_cmd("wiki (.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Searching Wiki")
    input_str = event.pattern_match.group(1)
    result = ""
    results = wikipedia.search(input_str)
    for s in results:
        page = wikipedia.page(s)
        url = page.url
        result += f"> [{s}]({url}) \n"
    await event.edit("WikiPedia **Search**: {} \n\n **Result**: \n\n{}".format(input_str, result))
