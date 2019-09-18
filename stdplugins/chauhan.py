"""Emoji

Available Commands:

.ravana"""

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

            "cHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ",
            
            "◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ",

            "◼️◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ",

            "◼️◼️◼️️cHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ",

            "◼️◼️◼️◼️cHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ",

            "‎◼️◼️◼️◼️◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ",

            "◼️◼️◼️◼️◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ",
            
            "◼️◼️◼️◼️◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ",
            
            "◼️◼️◼️◼️◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ",
   
            "◼️◼️◼️◼️◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️",

            "◼️◼️◼️◼️◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️◼️",

            "◼️◼️◼️◼️◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑ◼️◼️◼️",

            "◼️◼️◼️◼️◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑ◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\ncHÀûHäÑcHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️cHÀûHäÑcHÀûHäÑ◼️\n◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️cHÀûHäÑ◼️\n◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️cHÀûHäÑcHÀûHäÑ◼️◼️\n◼️cHÀûHäÑcHÀûHäÑcHÀûHäÑ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️cHÀûHäÑcHÀûHäÑ◼️◼️\n◼️cHÀûHäÑcHÀûHäÑ◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️cHÀûHäÑcHÀûHäÑ◼️◼️\n◼️cHÀûHäÑ◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️cHÀûHäÑcHÀûHäÑ◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

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
