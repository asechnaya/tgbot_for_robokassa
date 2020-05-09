from ast import literal_eval as le
import requests

from bs4 import BeautifulSoup

from support.payload import supportpayload


link = 'http://support.robokassa.ru/Login.aspx?ReturnUrl=%2fActiveIssues.aspx'


def support_data():
    with requests.Session() as s:
        response = s.post(url=link, data=supportpayload)
    soup = BeautifulSoup(response.text, 'html.parser')
    column_2 = '{'
    for entry in soup.select("tr:nth-child(2) > td > a:nth-child(1)"):
        stroka = '"' + str(entry.get_text(strip=True)).replace('(', '": "')
        column_2 += stroka.replace(')', '", ')
    for entry in soup.select("ul > a"):
        if entry.get_text(strip=True) == "VIP":
            stroka = '"' + str(entry.get_text(strip=True))
            column_2 += stroka + '" : "None", '
        else:
            stroka = '"' + str(entry.get_text(strip=True)).replace('(', '" : "')
            column_2 += stroka.replace(')', '", ')
    column_2 += '}'
    support_invoices = le(column_2)
    support_mails = ''.join([f'{key}: {value}\n' for key, value in support_invoices.items()])
    return support_mails

