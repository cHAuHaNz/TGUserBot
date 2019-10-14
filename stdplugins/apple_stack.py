"""Command: .🍎 to print a stack of 🍎
  © [cHAuHaN](http://t.me/amnd33p)"""

from telethon import events
import asyncio

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "🍎":
        animation_chars = [
                        " ‏‏‎ ",
                        "                🍎",
                        "            🍎 🍎",
                        "        🍎 🍎 🍎",
                        "    🍎 🍎 🍎 🍎",
                        "🍎 🍎 🍎 🍎 🍎"
                    ]
        msg = ""
        for s in animation_chars:
            msg += s+"\n"
            await event.edit(msg)
            await asyncio.sleep(0.5)