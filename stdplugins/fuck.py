"""COMMAND : 
.hilao // 👉✊️💦 ,
.sex // 🤵👼👰,
.kiss // 🤵💋👰"""

from telethon import events
import asyncio
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 35)
    input_str = event.pattern_match.group(1)
    if input_str == "hilao":
        await event.edit(input_str)
        animation_chars = [
            "👉______✊️",
            "👉_____✊️_",
            "👉____✊️__",
            "👉___✊️___",
            "👉__✊️____",
            "👉_✊️_____",
            "👉✊️💦____"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 7])

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 40)
    input_str = event.pattern_match.group(1)
    if input_str == "sex":
        await event.edit(input_str)
        animation_chars = [
            "🤵______👰",
            "🤵_____👰_",
            "🤵____👰__",
            "🤵___👰___",
            "🤵__👰____",
            "🤵_👰_____",
            "🤵👰______",
            "🤵👼👰____"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 8])

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.2
    animation_ttl = range(0, 40)
    input_str = event.pattern_match.group(1)
    if input_str == "kiss":
        await event.edit(input_str)
        animation_chars = [
            "🤵______👰",
            "🤵_____👰_",
            "🤵____👰__",
            "🤵___👰___",
            "🤵__👰____",
            "🤵_👰_____",
            "🤵👰______",
            "🤵💋👰____"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 8])