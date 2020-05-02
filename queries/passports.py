import re
import requests
from bs4 import BeautifulSoup
from queries.payload import payload
from config import cert

link = 'https://admin.roboxchange.com/admin2/ClientRequests/List?Length=13'

def number_of_passport_identifies():
    with requests.Session() as s:
        r = s.post(link, data=payload, cert=cert)
        soup = BeautifulSoup(r.text, 'html.parser')
        nident = soup.find("span", {"style": "float:right;"}, text=re.compile('Всего заявок')).get_text(strip=True)
    return 'Идентификация физлиц по паспорту за сегодня. {}'.format(nident)

