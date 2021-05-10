import requests
import datetime

from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup


translator = GoogleTranslator(source='en', target='pt')

def get_data_timeand_date():
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
        detail = translator.translate(detail)
        date = info.split(':')[0]
        title = info.split(':')[1]
        title = translator.translate(title)
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

def get_event_details_inthesky(url_event_detail):
    response = requests.get(url_event_detail)
    content = response.content
    site = BeautifulSoup(content, 'html.parser')
    details_div = site.find('div', attrs={'class': 'mainpane'})
    img_data = {
        'img_url': details_div.find('img')['src'],
        'img_description': translator.translate(details_div.find('img')['alt']),
    }
    news_div = details_div.find('div', attrs={'class': 'newsbody'})
    text =  news_div.find_all('p')[0].text
    tranlated_text = translator.translate(text.replace('\n', ''))
    return {
        'img_data': img_data,
        'text': tranlated_text
    }

def get_data_inthesky():
    months_translated = {
        'january': 'Janeiro',
        'february': 'Fevereiro',
        'march': 'Março',
        'april': 'Abril',
        'may': 'Maio',
        'june': 'Junho',
        'july': 'Julho',
        'august': 'Agosto',
        'september': 'Setembro',
        'october': 'Outubro',
        'november': 'Novembro',
        'december': 'Dezembro'
    }
    response = requests.get('https://in-the-sky.org/newscalyear.php?year=2021&maxdiff=1')
    content = response.content
    site = BeautifulSoup(content, 'html.parser')
    year_events = site.findAll('table', attrs={'class': 'stripy'})
    month = []
    data = {}
    index = 0    
    for month_events in year_events:
        month = month_events.find('thead').text
        rows = month_events.find('tbody')
        events = rows.find_all('tr')
        month_name = months_translated[month.lower()]
        event_list = []
        for event in events:
            name = event.find('a').text
            name = translator.translate(name)
            day = event.find('td').text
            details = get_event_details_inthesky(event.find('a')['href'])
            event_data = {
                'day': day,
                'name': name,
                'details': details
            }
            event_list.append(event_data)
        data[month_name] = event_list
    return data
            

    

# data = get_data_inthesky()