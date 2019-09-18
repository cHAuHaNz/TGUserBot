#Modded from dagd.py
"""
BarCode Generator
Command .bar (your text)
"""

import os
import requests
import json
import aiohttp
import asyncio
import math
import os
import subprocess
import time
import telethon.utils
from datetime import datetime
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon import events
from telethon.tl.types import DocumentAttributeVideo
from pySmartDL import SmartDL
from uniborg.util import admin_cmd, humanbytes, progress, time_formatter
from uniborg import util


thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"


@borg.on(admin_cmd("bar (.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    mone = await event.reply("Processing ...")
    input_str = event.pattern_match.group(1)
    sample_url = "https://www.scandit.com/wp-content/themes/bridge-child/wbq_barcode_gen.php?symbology=code128&value={}&size=100&ec=L".format(input_str.replace(" ","-"))
    link = sample_url.rstrip()
    start = datetime.now()
    url = link
    file_name = "barcode.webp"
    to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
    url = url.strip()
    file_name = file_name.strip()
    downloaded_file_name = os.path.join(to_download_directory, file_name)
    downloader = SmartDL(url, downloaded_file_name, progress_bar=False)
    downloader.start(blocking=False)
    c_time = time.time()
    while not downloader.isFinished():
        # url
        # downloaded_file_name
        # mone
        # c_time
        total_length = downloader.filesize if downloader.filesize else None
        downloaded = downloader.get_dl_size()
        display_message = ""
        now = time.time()
        diff = now - c_time
        percentage = downloader.get_progress() * 100
        speed = downloader.get_speed()
        elapsed_time = round(diff) * 1000
        progress_str = "[{0}{1}]\nProgress: {2}%".format(
            ''.join(["█" for i in range(math.floor(percentage / 5))]),
            ''.join(["░" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2))
        estimated_total_time = downloader.get_eta(human=True)
        try:
            current_message = f"SNAPDRAGON DOWNLOADER\n\nURL: {url}\nFile Name: {file_name}\n{progress_str}\n{humanbytes(downloaded)} of {humanbytes(total_length)}\nETA: {estimated_total_time}"
            if current_message != display_message:
                await mone.edit(current_message)
                display_message = current_message
        except Exception as e:
            logger.info(str(e))
    end = datetime.now()
    ms = (end - start).seconds
    if downloader.isSuccessful():
        await mone.edit("Downloaded to `{}` in {} seconds.".format(downloaded_file_name, ms))
    mone = await event.reply("Processing ...")
    input_str = Config.TMP_DOWNLOAD_DIRECTORY + file_name
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    if os.path.exists(input_str):
        start = datetime.now()
        c_time = time.time()
        await borg.send_file(
            event.chat_id,
            input_str,
            force_document=True,
            supports_streaming=False,
            allow_cache=False,
            reply_to=event.message.id,
            thumb=thumb,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, mone, c_time, "trying to upload")
            )
        )
        end = datetime.now()
        os.remove(input_str)
        ms = (end - start).seconds
        await mone.edit("Uploaded in {} seconds.".format(ms))
