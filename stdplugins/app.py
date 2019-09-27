import requests
import bs4 
import re
from telethon import *
from uniborg import *

@borg.on(events.NewMessage(outgoing=True,pattern='.app (.*)'))
@borg.on(events.MessageEdited(outgoing=True,pattern='.app (.*)'))
async def imdb(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        try:
            movie_name = e.pattern_match.group(1)
            remove_space = movie_name.split(' ')
            final_name = '+'.join(remove_space)
            page = get("https://play.google.com/store/search?q="+final_name+"&c=apps&hl=en")
            lnk = str(page.status_code)
            soup = BeautifulSoup(page.content,'lxml')
            odds = soup.findAll("div","WHE7ib")
            app_icon = odds[0].findNext('div').findNext('uzcko').findNext('img')['src']
            await e.edit('Icon Url :- '+app_icon)
        except IndexError:
            await e.edit("Plox enter **Valid app name**")