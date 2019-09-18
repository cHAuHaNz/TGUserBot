# For @UniBorg

"""fake leave

.fleave"""



from telethon import events

from datetime import datetime

from uniborg.util import admin_cmd

import importlib.util

import asyncio

import random

import importlib.util




@borg.on(events.NewMessage(outgoing=True, pattern='^\.(f?f)leave '))

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

