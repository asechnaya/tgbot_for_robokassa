import requests
from bs4 import BeautifulSoup

from config import cert
link = 'https://admin.roboxchange.com/admin2/Face/Statistics'

headers = {"Content-Type": "text/html; charset=utf-8"}


def current_day_statistics():
    with requests.Session() as s:
        response = s.post(link, headers=headers, cert=cert)
    soup = BeautifulSoup(response.text, 'html.parser')
    column_1 = []
    for entry in soup.select("tr > td.l.nw"):
        column_1.append(entry.get_text(strip=True))
    column_2 = []
    for entry in soup.select("tr > td.r.b"):
        column_2.append(entry.get_text(strip=True))
    stat = dict(zip(column_1, column_2))
    statistics = ''.join([f'{key}: {value}\n' for key, value in stat.items()])
    return statistics

