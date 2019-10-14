from telethon import events
import asyncio

@borg.on(events.NewMessage(pattern=r"sapple", outgoing=True))
async def _(event):
    animation_chars = [
                    " ‏‏‎ ",
                    "        🍎        ",
                    "      🍎 🍎       ",
                    "    🍎 🍎 🍎      ",
                    "  🍎 🍎 🍎 🍎     ",
                    "🍎 🍎 🍎 🍎 🍎    "
                ]
    msg = ""
    for s in animation_chars:
        msg += s+"\n"
        await event.edit(msg)
        await asyncio.sleep(0.5)