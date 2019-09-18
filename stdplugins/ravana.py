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

    if input_str == "ravana":

        await event.edit(input_str)

        animation_chars = [

            "RAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ",
            
            "◼️RAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ",

            "◼️◼️RAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ",

            "◼️◼️◼️️RAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ",

            "◼️◼️◼️◼️RAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ",

            "‎◼️◼️◼️◼️◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ",

            "◼️◼️◼️◼️◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ",
            
            "◼️◼️◼️◼️◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ",
            
            "◼️◼️◼️◼️◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ",
   
            "◼️◼️◼️◼️◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️",

            "◼️◼️◼️◼️◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀ◼️◼️",

            "◼️◼️◼️◼️◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀ◼️◼️◼️",

            "◼️◼️◼️◼️◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀ◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️RAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\nRAVÁNÀRAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️RAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️RAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️RAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️RAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️RAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️RAVÁNÀRAVÁNÀ◼️\n◼️RAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️RAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️RAVÁNÀ◼️\n◼️RAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️RAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️RAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️RAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️RAVÁNÀRAVÁNÀ◼️◼️\n◼️RAVÁNÀRAVÁNÀRAVÁNÀ◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️RAVÁNÀRAVÁNÀ◼️◼️\n◼️RAVÁNÀRAVÁNÀ◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️RAVÁNÀRAVÁNÀ◼️◼️\n◼️RAVÁNÀ◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️RAVÁNÀRAVÁNÀ◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️RAVÁNÀ◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
          
            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",
           
            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 30])
