import requests
import bs4 
import re
from telethon import *
from uniborg import *

@borg.on(events.NewMessage(outgoing=True,pattern='.app (.*)'))

@borg.on(events.MessageEdited(outgoing=True,pattern='.app (.*)'))

async def imdb(e):
    try:
        movie_name = e.pattern_match.group(1)
        remove_space = movie_name.split(' ')
        final_name = '+'.join(remove_space)
        page = requests.get("https://play.google.com/store/search?q="+final_name+"&c=apps&hl=en")
        lnk = str(page.status_code)
        soup = bs4.BeautifulSoup(page.content,'lxml', from_encoding='utf-8')
        results = soup.findAll("div","WHE7ib")
        app_icon = results[0].findNext('div').findNext('uzcko').findNext('img')['src']
        await e.edit('Icon Url :- '+app_icon)
    except IndexError:
        await e.edit("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await e.edit("Exception"+str(err))
