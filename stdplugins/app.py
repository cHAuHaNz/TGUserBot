import requests
import bs4 
import re
from telethon import *
from uniborg import *

@borg.on(events.NewMessage(outgoing=True,pattern='.app (.*)'))

@borg.on(events.MessageEdited(outgoing=True,pattern='.app (.*)'))

async def imdb(e):
    try:
        app_name = e.pattern_match.group(1)
        remove_space = app_name.split(' ')
        final_name = '+'.join(remove_space)
        page = requests.get("https://play.google.com/store/search?q="+final_name+"&c=apps")
        lnk = str(page.status_code)
        soup = bs4.BeautifulSoup(page.content,'lxml', from_encoding='utf-8')
        results = soup.findAll("div","WHE7ib mpg5gc")
        print(results.__len__())
        app_name = results[0].findNext('div', 'Vpfmgd').findNext('div', 'WsMG1c nnK0zc').text
        app_dev = results[0].findNext('div', 'Vpfmgd').findNext('div', 'KoLSrc').text
        app_dev_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('a', 'mnKHRc')['href']
        app_rating = results[0].findNext('div', 'Vpfmgd').findNext('div', 'pf5lIe').find('div')['aria-label']
        app_link = "https://play.google.com"+results[0].findNext('div', 'Vpfmgd').findNext('div', 'vU6FJ p63iDd').a['href']
        app_icon = results[0].findNext('div', 'Vpfmgd').findNext('div', 'uzcko').img['data-src']
        app_details = app_name
        app_details += "\nDeveloper : ["+app_dev+"]("app_dev_link+")"
        app_details += "\nRating : "+app_rating.replace("Rated ", "⭐ ").replace(" out of ", "/").replace(" stars", "", 1).replace(" stars", "⭐ ").replace("five", "5"))
        app_details += "\n[View in Play Store]("+app_link+")"
        app_details += "\n[]("+app_icon+")"
        await e.edit(app_details, link_preview = True)
    except IndexError:
        await e.edit("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await e.edit("Exception Occured:- "+str(err))
