import json
from datetime import date
from pytz import timezone

from web_scrapping import get_data

def data_file_name():
    today = date.today()
    return f'{today.day}_{today.month}_{today.year}'

def events_data():   
    file_name = data_file_name()
    try:
        with open(f"data/{file_name}.json", "r", encoding="utf8") as json_file:
            print('file_exists\n\n')
            json.load(json_file)
            json_file.close()

    except FileNotFoundError:
        data = get_data()
        with open(f"data/{file_name}.json", "w", encoding="utf8") as json_file:
            json.dump(data, json_file)
            json_file.close()
