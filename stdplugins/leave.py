"""Leave Groups
.leave to Leave Group
.fleave to Fake Leave."""
from telethon import events
from uniborg.util import admin_cmd
import asyncio
from telethon.tl.functions.channels import LeaveChannelRequest

import time
@borg.on(admin_cmd("leave", outgoing=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("[Legend]](http://t.me/amnd33p) `is leaving this chat.....!`\n@admin `Goodbye aren't forever.. `")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`Sir, This is Not A Chat.`')

@borg.on(admin_cmd("fleave", outgoing=True))
async def timer_blankx(e):
	txt=e.text[7:] + '\n\n`Exiting This Group In` '
	j=5
	k=j
	for j in range(j):
		await e.edit(txt + str(k))
		k=k-1
		await asyncio.sleep(1)
	if e.pattern_match.group(1) == 'f':
		await e.edit("`Group Exited. I Had A Pleasant Stay With You Guys..` ")
