import requests
from bs4 import BeautifulSoup
from _datetime import datetime, timedelta

from config import cert
# cert = "../temp/cert.pem"


link = 'https://admin.roboxchange.com/admin2/Operations/Search'
headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}


this_time = datetime.today().strftime("%d.%m.%Y %H:%M")
minus_hour = datetime.today() + timedelta(minutes=-30)
minus_hour = minus_hour.strftime("%d.%m.%Y %H:%M")

data = {"SpecialOpFilter": "Finished",
        "Filter[Limit]": 10,
        "Filter[UsePeriod]": True,
        "Filter[DateFrom]": minus_hour,
        "Filter[DateTill]": this_time,
        "Filter[IncAccountFull]": False,
        "Filter[OutAccountFull]": False,
        "Filter[IncCurr]": "",
        "Filter[IncludeAccounts]": False,
        "Filter[Processes]": "D__"}


def payment_systems_statuses():
    with requests.Session() as s:
        entry_number = 0  # счетчик числа записей с номерами операций
        response = s.post(link, data=data, cert=cert, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        for entry in soup.select("tr > td:nth-child(2) > a"):
            # print(entry.get_text(strip=True))
            entry_number += 1
        return entry_number
