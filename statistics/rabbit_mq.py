import requests
from bs4 import BeautifulSoup

from config import cert

link = 'https://admin.roboxchange.com/admin2/Face/RabbitMqMonitoring'

headers = {"Content-Type": "text/html; charset=utf-8"}


def rabbit_mq():
    with requests.Session() as s:
        response = s.post(link, headers=headers, cert=cert)
    soup = BeautifulSoup(response.text, 'html.parser')
    for entry in soup.select("div > table > tr > td:nth-child(2)"):
        if 'ok' in entry.get_text(strip=True):
            rmq_status = "ОК ✅"
        else:
            rmq_status = entry.get_text(strip=True) + ' 🛑'
        return rmq_status
