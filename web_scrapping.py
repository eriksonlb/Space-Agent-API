import requests
import datetime

from googletrans import Translator
from bs4 import BeautifulSoup


translator = Translator()

def get_data():
    response = requests.get('https://www.timeanddate.com/astronomy/sights-to-see.html')
    content = response.content
    today = datetime.datetime.now()
    month = today.month
    months = {
        1: 'january',
        2: 'february',
        3: 'mars',
        4: 'april',
        5: 'may',
        6: 'june',
        7: 'july',
        8: 'august',
        9: 'september',
        10: 'october',
        11: 'november',
        12: 'december'
    }


    site = BeautifulSoup(content, 'html.parser')
    events = site.findAll('article', attrs={'class': 'post-row'})
    item = {}
    data = []
    index = 0
    for event in events:
        info = event.find('h3').text
        detail = event.find('p').text
        img_data = event.find('figure')
        img = img_data.find('img')
        img_link = img['src']
        # detail = translator.translate(detail)
        date = info.split(':')[0]
        title = info.split(':')[1]
        # title = translator.translate(title)
        index = index + 1
        event_data = {
            'title': title,
            'date': date.replace('/', ' and '), 
            'details': detail,
            'img_link': img_link
        }
        item[f'event_{index}'] = event_data
        data.append(item)    

    return data

    

get_data()