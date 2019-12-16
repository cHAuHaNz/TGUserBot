"""Available Commands: .chauhan"""
from telethon import events
import asyncio
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 30)
    input_str = event.pattern_match.group(1)
    if input_str == "chauhan":
        await event.edit(input_str)
        animation_chars = [
            "cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ",
            "◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ",
            "◼️◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ",
            "◼️◼️◼️️cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ",
            "◼️◼️◼️◼️cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ",
            "‎◼️◼️◼️◼️◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ",
            "◼️◼️◼️◼️◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ",
            "◼️◼️◼️◼️◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ",
            "◼️◼️◼️◼️◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ",
            "◼️◼️◼️◼️◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️",
            "◼️◼️◼️◼️◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️◼️",
            "◼️◼️◼️◼️◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ◼️◼️◼️",
            "◼️◼️◼️◼️◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\ncHÀûHäÑ cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️cHÀûHäÑ cHÀûHäÑ◼️\n◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️cHÀûHäÑ◼️\n◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️cHÀûHäÑ cHÀûHäÑ◼️◼️\n◼️cHÀûHäÑ cHÀûHäÑ cHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️cHÀûHäÑ cHÀûHäÑ◼️◼️\n◼️cHÀûHäÑ cHÀûHäÑ◼️◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️cHÀûHäÑ cHÀûHäÑ◼️◼️\n◼️cHÀûHäÑ◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️cHÀûHäÑ cHÀûHäÑ◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️cHÀûHäÑ◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",          
            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",           
            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",
            "◼️◼️\n◼️◼️",
            "◼️"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 30])
