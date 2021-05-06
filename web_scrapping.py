import requests
import datetime

from bs4 import BeautifulSoup

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
    data = {}
    for event in events:
        info = event.find('h3').text
        date = info.split(':')[0]
        title = info.split(':')[1]
        data[date] = title
    return data

    

get_data()