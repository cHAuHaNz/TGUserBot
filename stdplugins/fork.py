"""COMMAND : .fork"""
from telethon import events
import asyncio
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 13)
    input_str = event.pattern_match.group(1)
    if input_str == "fork":
        animation_chars = [
            "`Your bot is running\n\nTelethon version:` 1.9.0\n`Python:` 3.7.3\n`User:` @amnd33p\n`Database Status: Databases functioning normally!`",
            "`Connecting To github.com...`",
            "`Deleting Old Repo....`",
            "`Forking TGUserBot... 0%\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 0 MiB / 100.7 MiB`",
            "`Forking TGUserBot... 4%\n\n⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 4 MiB / 100.7 MiB`",
            "`Forking TGUserBot... 8%\n\n⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 8 MiB / 100.7 MiB`",    
            "`Forking TGUserBot... 20%\n\n⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 20 MiB / 100.7 MiB`",
            "`Forking TGUserBot... 36%\n\n⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 36 MiB / 100.7 MiB `",
            "`Forking TGUserBot... 52%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n\nFile Size: 52.7 MiB / 100.7 MiB `",
            "`Forking TGUserBot... 75%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️\n\nFile Size: 52.7 MiB / 100.7 MiB `",
            "`Forking TGUserBot... 84%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️\n\nFile Size: 84.7 MiB / 100.7 MiB `",
            "`Forking TGUserBot... 100%\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️\n\nFile Size: 100.7 MiB / 100.7 MiB\n\nTask Completed... `",
            "`Fork Deploying...`\n\n@UniBorg ( `Custom Built By` @amnd33p ) \n`Verified Account:` ☑️\n`Official Channel:` https://t.me/Xpl0iter\n\n`Python` `Loading...`\n[GCC 7.3.0]\n`Telethon` `Loading...`",
            "`Fork Deployed...`\n\n@UniBorg ( `Custom Built By` @amnd33p ) \n`Verified Account:` ✅\n`Official Channel:` https://t.me/Xpl0iter\n\n`Python` 3.6.8 [GCC 7.3.0]\n`Telethon` 1.8.0"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 14])
