"""Emoji

Available Commands:

.deploy"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 10

    animation_ttl = range(0, 12)

    input_str = event.pattern_match.group(1)

    if input_str == "deploy":

        await event.edit(input_str)

        animation_chars = [
        
            "**Heroku Connecting To Latest Github Build (Pornhub)**",
            "**Build started by user** @r4v4n4",
            "**Deploy** `535a74f0` **by user** @r4v4n4",
            "**Restarting Heroku Server...**",
            "**State changed from up to starting**",    
            "**Stopping all processes with SIGTERM**",
            "**Process exited with** `status 143`",
            "**Starting process with command** `python3 -m stdborg`",
            "**State changed from starting to up**",
            "__INFO:UniBorg:Logged in as 557667062__",
            "__INFO:UniBorg:Successfully loaded all plugins__",
            "**Build Succeeded**"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
