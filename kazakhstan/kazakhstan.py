from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

from config import cert


link = 'https://admin.roboxchange.com/admin2/Operations/Search'
headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}


def payload():
    this_time = (datetime.utcnow() + timedelta(days=1)).strftime("%d.%m.%Y %H:%M")
    minus_hour = (datetime.utcnow() + timedelta(minutes=-30)).strftime("%d.%m.%Y %H:%M")

    data = {"SpecialOpFilter": "Finished",
            "Filter[Limit]": 100,
            "Filter[UsePeriod]": True,
            "Filter[DateFrom]": minus_hour,
            "Filter[DateTill]": this_time,
            "Filter[IncAccountFull]": False,
            "Filter[OutAccountFull]": False,
            "Filter[IncCurr]": "",
            "Filter[OutCurr]": "BNT",
            "Filter[IncludeAccounts]": False,
            "Filter[Processes]": ""}
    return data


def kazakhstan_operations_counter():
    with requests.Session() as s:
        entry_number = 0  # счетчик числа записей с номерами операций
        operations = []
        response = s.post(link, data=payload(), cert=cert, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        for entry in soup.select("tr > td:nth-child(2) > a"):  # считываем первый столбец в админке
            entry_number += 1
            operations.append(entry.get_text(strip=True))
        return entry_number, operations
