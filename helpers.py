import json
from datetime import date
from pytz import timezone

from web_scrapping import get_data_inthesky

def data_file_name():
    today = date.today()
    return f'{today.day}_{today.month}_{today.year}'

def events_data():   
    print('Iniciando busca de dados')
    try:
        with open(f"data/events.json", "r", encoding="utf8") as json_file:
            print('file_exists\n\n')
            json.load(json_file)
            json_file.close()

    except FileNotFoundError:
        print('Criando dados...')
        data = get_data_inthesky()
        print('escrevendo dados')
        with open(f"data/events.json", "w", encoding="utf8") as json_file:
            json.dump(data, json_file)
            json_file.close()
