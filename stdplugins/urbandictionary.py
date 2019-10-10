"""Urban Dictionary
Syntax: .ud Query"""
from telethon import events
import urbandict
from uniborg.util import admin_cmd


@borg.on(admin_cmd("ud (.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("processing...")
    str = event.pattern_match.group(1)
    try:
        mean = urbandict.define(str)
        if len(mean) > 0:
            await event.edit(
                'Text: **' +
                str +
                '**\n\nMeaning: **' +
                mean[0]['def'] +
                '**\n\n' +
                'Example: \n__' +
                mean[0]['example'] +
                '__'
            )
        else:
            await event.edit("No result found for **" + str + "**")
    except:
        await event.edit("No result found for **" + str + "**")
