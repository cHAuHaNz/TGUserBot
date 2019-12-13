#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
from math import ceil
import asyncio
import json
import random
import re
from telethon import events, custom
from uniborg.util import admin_cmd, humanbytes


@borg.on(admin_cmd(pattern="ib (.[^ ]*) (.*)"))
async def _(event):
    # https://stackoverflow.com/a/35524254/4723940
    if event.fwd_from:
        return
    bot_username = event.pattern_match.group(1)
    search_query = event.pattern_match.group(2)
    try:
        output_message = ""
        bot_results = await event.client.inline_query( 
            bot_username,
            search_query
        )
        i = 0
        for result in bot_results:
            output_message += "{} {} `{}`\n\n".format(
                result.title,
                result.description,
                ".icb " + bot_username + " " + str(i + 1) + " " + search_query
            )
            i = i + 1
        await event.edit(output_message)
    except Exception as e:
        await event.edit("{} did not respond correctly, for **{}**!\n\
            `{}`".format(bot_username, search_query, str(e)))


@borg.on(admin_cmd(pattern="icb (.[^ ]*) (.[^ ]*) (.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    bot_username = event.pattern_match.group(1)
    i_plus_oneth_result = event.pattern_match.group(2)
    search_query = event.pattern_match.group(3)
    try:
        bot_results = await event.client.inline_query(bot_username,search_query)
        message = await bot_results[int(i_plus_oneth_result) - 1].click(event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True)
    except Exception as e:
        await event.edit(str(e))


if Config.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == borg.uid and query.startswith("@amnd33p_bot"):
            rev_text = query[::-1]
            buttons = paginate_help(0, borg._plugins, "helpme")
            result = builder.article(
                "© @amnd33p",
                text="{}\nℂ𝕦𝕣𝕣𝕖𝕟𝕥𝕝𝕪 𝕃𝕠𝕒𝕕𝕖𝕕 ℙ𝕝𝕦𝕘𝕚𝕟𝕤: {}".format(
                    query, len(borg._plugins)),
                buttons=buttons,
                link_preview=False
            )
        elif query.startswith("tb_btn"):
            result = builder.article(
                "Button Parser © @amnd33p",
                text=f"Powered by @uniborg",
                buttons=[],
                link_preview=False
            )
        else:
            result = builder.article(
                "© @amnd33p",
                text="""**Custom Built [TGUserBot](https://github.com/cHAuHaNz/TGUserBot/) By** [cHAuHaN](tg://user?id=606846495)\
                    \n**Verified Account:** ✅\
                    \n**Official Channel:** [Tʜᴇ Xᴘʟ0ɪᴛᴇʀ™](https://t.me/Xpl0iter)\
                    \n\
                    \n**Python 3.7.4 (default, Sep 12 2019, 01:19:52)** \
                    \n**[GCC 7.4.0]**\
                    \n**Telethon 1.10.3**""",
                buttons=[
                    [custom.Button.url("Creator👤", "https://telegram.dog/amnd33p"), custom.Button.url("📼Channel📼", "https://t.me/Xpl0iter")],
                    [custom.Button.url("👨‍💻Source👨‍💻", "https://github.com/cHAuHaNz/TGUserBot/"), custom.Button.url(
                        "Deploy❗", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FcHAuHaNz%2FTGUserBot%2F&template=https%3A%2F%2Fgithub.com%2FcHAuHaNz%2FTGUserBot%2F")]
                ],
                link_preview=False
            )
        await event.answer([result] if result else None)


    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"helpme_next\((.+?)\)")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == borg.uid:
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number + 1, borg._plugins, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Please get your own @UniBorg, and don't edit my messages!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"helpme_prev\((.+?)\)")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == borg.uid:
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1,
                borg._plugins,
                "helpme"
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Please get your own @UniBorg, and don't edit my messages!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ub_plugin_(.*)")))
    async def on_plug_in_callback_query_handler(event):
        plugin_name = event.data_match.group(1).decode("UTF-8")
        help_string = borg._plugins[plugin_name].__doc__[0:125]
        if help_string is not None:
            reply_pop_up_alert = help_string 
        else:
            reply_pop_up_alert = "No DOCSTRING has been setup for {} plugin".format(plugin_name)
        reply_pop_up_alert += "\n\n Use .remove {} to remove this plugin\n\
            © @amnd33p".format(plugin_name)
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = Config.NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD
    number_of_cols = 2
    multi = "😇🤠🤡😈👿👹👺💀☠👻👽👾🤖💩😺😸😹😻😼😽🙀😿😾🙈🙉🙊👦👧👨👩👴👵👶"
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [custom.Button.inline(
        "{} {} {}".format(random.choice(list(multi)), x, random.choice(list(multi))),
        data="ub_plugin_{}".format(x))
        for x in helpable_plugins]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
            [
            (custom.Button.inline("⏪", data="{}_prev({})".format(prefix, modulo_page)),
             custom.Button.inline("⏩", data="{}_next({})".format(prefix, modulo_page)))
        ]
    return pairs