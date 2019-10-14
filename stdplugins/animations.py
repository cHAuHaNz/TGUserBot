"""Available Commands:
.hilao // 👉✊️💦 ,
.sex // 🤵👼👰,
.kiss // 🤵💋👰
.🍎 to print a stack of 🍎
.loading
.square
.up
.round
.heart
.plane
.clock
.tclock
  © [cHAuHaN](http://t.me/amnd33p)"""
from telethon import events
import asyncio
import time
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 100)
    input_str = event.pattern_match.group(1)
    if input_str == "loading":
        animation_chars = [
            "▮",
            "▯",
            "▬",
            "▭"
            "‎"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])
    if input_str == "square":
        animation_chars = [
            "◧",
            "◨",
            "◧",
            "◨"
            "‎"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])
    if input_str == "up":
        animation_chars = [
            "╹",
            "╻",
            "╹",
            "╻"
            "‎"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])
    if input_str == "round":
        animation_chars = [
            "⚫",
            "⬤",
            "●",
            "∘"
            "‎"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])
    if input_str == "heart":
        animation_chars = [
            "🖤",
            "💜",
            "💙",
            "💚",
            "💛",
            "🧡",
            "‎"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 6])
    if input_str == "plane":
        animation_chars = [
            "✈-------------",
            "-✈------------",
            "--✈-----------",
            "---✈----------",
            "----✈---------",
            "-----✈--------",
            "------✈-------",
            "-------✈------",
            "--------✈-----", 
            "---------✈----",
            "----------✈---",
            "-----------✈--",
            "------------✈-",
            "-------------✈"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 14])
    if input_str == "clock":
        animation_chars = [
            "🕛",
            "🕐",
            "🕑",
            "🕒",
            "🕓",
            "🕔",
            "🕕",
            "🕖",
            "🕗",
            "🕘",
            "🕙"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])
    if input_str == "tclock":
        deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
        for _ in range(48):
            await asyncio.sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    if input_str == "🍎":
        animation_chars = [
                        " ‏‏‎               🍎",
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

    animation_interval = 0.2
    animation_ttl = range(1, 44)
    input_str = event.pattern_match.group(1)
    if input_str == "hilao":
        animation_chars = [
            "👉 ‏‏‎  ‏‏‎ ✊️",
            "👉 ‏‏‎ ✊️ ‏‏‎ ",
            "👉✊️ ‏‏‎  ‏‏‎ ",
            "👉 ‏‏‎ ✊️ ‏‏‎ ",
            "👉 ‏‏‎  ‏‏‎ ✊️",
            "👉 ‏‏‎ ✊️ ‏‏‎ ",
            "👉✊️ ‏‏‎  ‏‏‎ ",
            "👉 ‏‏‎ ✊️ ‏‏‎ ",
            "👉 ‏‏‎  ‏‏‎ ✊️",
            "👉 ‏‏‎ ✊️ ‏‏‎ ",
            "👉✊️💦 ‏‏‎ "
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])
    animation_ttl = range(1, 40)
    input_str = event.pattern_match.group(1)
    if input_str == "sex":
        animation_chars = [
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ 👰",
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ 👰 ‏‏‎ ",
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ 👰 ‏‏‎  ‏‏‎ ",
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎ 👰 ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵 ‏‏‎  ‏‏‎ 👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵 ‏‏‎ 👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵👼👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ "
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 8])
    animation_ttl = range(1, 40)
    input_str = event.pattern_match.group(1)
    if input_str == "kiss":
        animation_chars = [
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ 👰",
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ 👰 ‏‏‎ ",
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ 👰 ‏‏‎  ‏‏‎ ",
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎ 👰 ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵 ‏‏‎  ‏‏‎ 👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵 ‏‏‎ 👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵💋👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ "
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 8])    