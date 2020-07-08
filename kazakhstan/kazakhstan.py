import requests
from bs4 import BeautifulSoup
from .payload import payload
from config import cert


link = 'https://admin.roboxchange.com/admin2/Operations/Search'
headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}


def kazakhstan_operations_counter():
    with requests.Session() as s:
        entry_number = 0  # счетчик числа записей с номерами операций
        opers = []
        response = s.post(link, data=payload(), cert=cert, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup)
        for entry in soup.select("tr > td:nth-child(2) > a"):
            entry_number += 1
            opers.append(entry.get_text(strip=True))
        return entry_number, opers


print(kazakhstan_operations_counter())
