# -*- coding: cp1251 -*-
from datetime import date, timedelta

import re
import requests
from bs4 import BeautifulSoup

from config import cert

import logging


module_logger = logging.getLogger('passports')


def payload_for_passports():
    date_time_after = (date.today() - timedelta(days=22)).strftime("%d.%m.%Y")
    date_time_until = (date.today() + timedelta(days=1)).strftime("%d.%m.%Y")

    payload = {
        'Length': 13,
        'reqType': 'identification',
        'pageNumber': 1,
        'sortDirection': 'CreatedAsc',
        'assigned': 'NULL',
        'merchantType': 'MerchantOff',
        'PartnerCountry': 'RU',
        'PartnerIdentifier': '',
        'ShopIdentifier': '',
        'reqState': 92,
        'DateType': 'modified',
        'dateTimeAfter': date_time_after,
        'dateTimeUntil': date_time_until,
        'fetchRows': 30,
        'X-Requested-With': 'XMLHttpRequest'
    }
    return payload


def number_of_passport_identifies():
    logger = logging.getLogger('number_of_passport_identifies')
    link = 'https://admin.roboxchange.com/admin2/ClientRequests/List?Length=13'
    with requests.Session() as s:
        r = s.post(link, data=payload_for_passports(), cert=cert)
        soup = BeautifulSoup(r.text, 'html.parser')
        count_requests = soup.find("span", {"style": "float:right;"}, text=re.compile('Всего заявок'))
        count_requests_text = count_requests.get_text(strip=True)
    logger.info(u'Individuals identified by passport for today: {}.'.format(count_requests_text))
    return f'Идентификация физлиц по паспорту за сегодня. {count_requests_text}'

