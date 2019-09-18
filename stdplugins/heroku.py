"""command: .heroku"""



from telethon import events

from datetime import datetime

from uniborg.util import admin_cmd

import importlib.util

import asyncio

import random

import importlib.util




@borg.on(events.NewMessage(outgoing=True, pattern='^\.(f?h)eroku '))

async def timer_blankx(e):

 txt=e.text[7:] + '\n\n`Exiting This Group In` '

 j=10

 k=j

 for j in range(j):

  await e.edit(txt + str(k))

  k=k+10

  await asyncio.sleep(1)

 if e.pattern_match.group(1) == 'f':

  await e.edit("`\nOutput: \naccount_profile.py \nafk.py \nantiflood.py \nblacklist.py \ncalendar.py \ncall_admin.py \nclock.animation.py \nclock_name.py \ncode.py \ncoinflip.py \ncolors.py \ncountdown.py \ncount.py \ncreate_private_group.py \ncurrency.py \ndagd.py \ndecide.py \ndictionary.py \ndownload.py \nemojis.py \neval.py \nexec.py \nfileext.py \nfilemanager_v0.2.py \nfile_to_photo.py \nfilters.py \nfwd.py \ngban.py \nget_admin.py \nget_bot.py \nget_id.py \ngifs_to_stickers.py \ngithub.py \ngoogle.py \n_help.py \nheroku.py \nifsc.py \ninvite.py \njson.py \nleave.py \nlocks.py \nlog_pms.py \nmarkdown.py \nmoon.animation.py \nninja.py \nocr.py \nopenweathermap.py \npastebin.py \nping.py \npin_message.py \npmpermit.py \npolls.py \npower_tools.py \npromote.py \npurge.py \npycache \nqr_code.py \nreact.py \nREADME.md \nremove.bg.py \nrename.py \nsca.py \nschd.py \nscreencapture.py \nsed.py \nsnip.py \nspeedtest.py \nstickers.py \nstt.py \ntagall.py \ntelegraph.py \nthumbnail.py \ntime.py \ntorrentz.py \ntranslatewithoutemoji.py \ntts.py \nukinti.py \nunbanmute.py \nupload.py \nupload_to_mirrorace.py \nurbandictionary.py \nverystream.py \nwelcome.py \nwhatscrapp.py \nwhois.py \nwikimedia.py \nwikipedia.py \nwirelesscharge.py \nxkcd.py \nxtools.py \nyoutube_dl.py` ")

