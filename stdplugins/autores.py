"""Auto-responder for #Request by `cHAuHaN`
"""

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
        await event.client.send_message(
            "-387693035",
            "New Request Received :- `"+name+"`",
            reply_to=message_id
        )

"""
@borg.on(events.Raw())
async def on_new_channel_message(event):
    try:
        if Config.PM_LOGGR_BOT_API_ID is None:
            return
        if tgbot is None:
            return
        # logger.info(event.stringify())
        if isinstance(event, types.UpdateChannel):
            channel_id = event.channel_id
            message_id = 2
            # someone added me to channel
            # TODO: https://t.me/TelethonChat/153947
            the_message = ""
            the_message += "#MessageActionChatAddUser\n\n"
            # the_message += f"[User](tg://user?id={added_by_user}): `{added_by_user}`\n"
            the_message += f"[Private Link](https://t.me/c/{channel_id}/{message_id})\n"
            await borg.send_message(
                entity=Config.PM_LOGGR_BOT_API_ID,
                message=the_message,
                # reply_to=,
                # parse_mode="html",
                link_preview=False,
                # file=message_media,
                silent=True
            )
    except Exception as e:
        print(str(e))
"""