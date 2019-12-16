"""COMMAND : .info, .dc, .help <plugin_name>"""

import sys
from telethon import events, functions, __version__
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="info ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    splugin_name = event.pattern_match.group(1)
    if splugin_name in borg._plugins:
        s_help_string = borg._plugins[splugin_name].__doc__
    else:
        s_help_string = "use .info <module_name>"
    help_string = """**Custom Built [TGUserBot](https://github.com/cHAuHaNz/TGUserBot/) By** [cHAuHaN](tg://user?id=606846495)\n**Verified Account**: ✅\n**Official Channel**: https://t.me/Xpl0iter
""".format(
        sys.version,
        __version__
    )
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER
    if tgbotusername is not None:
        results = await borg.inline_query(
            tgbotusername,
            help_string + "\n\n" + s_help_string
        )
        await results[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
        await event.delete()
    else:
        await event.reply(help_string + "\n\n" + s_help_string)
        await event.delete()


@borg.on(admin_cmd(pattern="dc"))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetNearestDcRequest())
    await event.edit(result.stringify())


@borg.on(admin_cmd(pattern="config"))
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())
    result = result.stringify()
    logger.info(result)
    await event.edit("""Telethon UserBot custom built by @amnd33p""")


@borg.on(admin_cmd(pattern="help (.*)"))
async def _(event):
    if event.fwd_from:
        return
    plugin_name = event.pattern_match.group(1)
    if plugin_name in borg._plugins:
        help_string = borg._plugins[plugin_name].__doc__
        unload_string = f"Use `.uninstall {plugin_name}` to remove this plugin.\n  © @amnd33p"
        if help_string:
            plugin_syntax = f"Syntax for plugin **{plugin_name}**:\n\n{help_string}\n{unload_string}"
        else:
            plugin_syntax = f"No DOCSTRING has been setup for {plugin_name} plugin."
    else:
        plugin_syntax = "Enter valid **Plugin** name.\nDo `.stdplugins` or `.info` to get list of valid plugin names."
    await event.edit(plugin_syntax)
