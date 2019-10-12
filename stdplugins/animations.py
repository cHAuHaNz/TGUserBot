"""Available Commands:
.loading
.square
.up
.round
.heart
.plane
.clock
.tclock"""
from telethon import events
import asyncio
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 100)
    input_str = event.pattern_match.group(1)
    if input_str == "loading":
        await event.edit(input_str)
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
        await event.edit(input_str)
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
        await event.edit(input_str)
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
        await event.edit(input_str)
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
        await event.edit(input_str)
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
        await event.edit(input_str)
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
        await event.edit(input_str)
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