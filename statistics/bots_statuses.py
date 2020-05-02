import requests
from bs4 import BeautifulSoup

from config import cert

link = 'https://admin.roboxchange.com/admin2/Face/BotsState'

headers = {"Content-Type": "text/html; charset=utf-8"}


def bot_statuses():
    with requests.Session() as s:
        response = s.post(link, headers=headers, cert=cert)
    soup = BeautifulSoup(response.text, 'html.parser')
    column_1 = []
    for entry in soup.select("tr > td.l.col-lg-9"):
        column_1.append(entry.get_text(strip=True))
    column_2 = []
    for entry in soup.select("tr > td.r.nw.col-lg-3"):
        column_2.append(entry.get_text(strip=True))
    bs = dict(zip(column_1, column_2))
    bots_state = f"Автомат: {bs['Автомат:']}\n" \
                 f"Сервис запуска ботов: {bs['Сервис запуска ботов:']}\n" \
                 f"Сервис подтверждений OCEAN: {bs['Сервис подтверждений OCEAN:']}\n" \
                 f"Сервис учетной системы: {bs['Сервис учетной системы:']}\n"
    print(bots_state)
    return bots_state

