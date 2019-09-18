"""COMMAND : .ae"""

from telethon import events

PRINTABLE_ASCII = range(0x21, 0x7f)


def aesthetify(string):
    for c in string:
        c = ord(c)
        if c in PRINTABLE_ASCII:
            c += 0xFF00 - 0x20
        elif c == ord(" "):
            c = 0x3000
        yield chr(c)


@borg.on(events.NewMessage(pattern=r'.ae\s+(.+)', outgoing=True))
@borg.on(events.MessageEdited(pattern=r'.ae\s+(.+)', outgoing=True))
async def _(event):
    text = event.pattern_match.group(1)
    text = "".join(aesthetify(text))
    await event.edit(text=text, parse_mode=None, link_preview=False)
    raise events.StopPropagation
