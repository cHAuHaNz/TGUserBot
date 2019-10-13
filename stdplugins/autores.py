"""Auto-responder for #Request by [cHAuHaN](http://t.me/amnd33p)"""

#regex ([a-zA-Z0-9 ]+)( #([r]|[R])equest)($|[\n])

import asyncio
import io
import re
from telethon import events, errors, functions, types
from uniborg.util import admin_cmd

@borg.on(admin_cmd(incoming=True))
async def on_snip(event):
    name = event.raw_text
    pattern = r"([a-zA-Z0-9 ]+)( #([r]|[R])equest)($|[\n])"
    if re.search(pattern, name, flags=re.IGNORECASE):
        message_id = event.message.id
        #if event.reply_to_msg_id:
        #    message_id = event.reply_to_msg_id
        await event.client.send_message(
            event.chat_id,
            "Your request has been received, It will be fulfilled ASAP.\n`Please don't send a duplicate request within 3 days.`",
            reply_to=message_id
        )
        msg = event.message
        if msg:
            msg_o = await event.client.forward_messages(
                entity=Config.PRIVATE_GROUP_FOR_REQUESTS_ID,
                messages=msg,
                from_peer=event.chat_id,
                silent=False
            )