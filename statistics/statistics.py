import requests
from bs4 import BeautifulSoup

from config import cert


link = 'https://admin.roboxchange.com/admin2/Face/Statistics'

headers = {"Content-Type": "text/html; charset=utf-8"}


def extract_day_statistics():
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
    return stat


def current_day_statistics():
    stat = extract_day_statistics()
    statistics = ''.join([f'{key}: {value}\n' for key, value in stat.items()])
    return statistics


def concise_statistics_of_the_day():
    daystats = extract_day_statistics()
    del daystats['Повторных оплат']
    del daystats['Заблокировано операций']
    del daystats['Отложено операций']
    del daystats['Всего заявок подавалось']
    del daystats['Отменено роботом']
    del daystats['Завершено операций предыдущего дня']
    del daystats['Отправлено сообщений в поддержку']
    statistics = ''.join([f'{key}: {value}\n' for key, value in daystats.items()])
    return statistics


def paused_operations():
    paused = extract_day_statistics()
    return paused['Приостановлено операций']
