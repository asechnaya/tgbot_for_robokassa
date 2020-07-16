import requests
from bs4 import BeautifulSoup

from config import cert

link = 'https://admin.roboxchange.com/admin2/Face/PsStates'

headers = {"Content-Type": "text/html; charset=utf-8"}


def payment_systems_statuses():
    with requests.Session() as s:
        response = s.post(link, headers=headers, cert=cert)
    soup = BeautifulSoup(response.text, 'html.parser')
    column_1 = []
    for entry in soup.select("tr > td.l.w.col-lg-4"):
        column_1.append(entry.text)
    column_2 = []
    for entry in soup.select("tr > td.r.w.col-lg-5"):
        column_2.append(entry.text.replace("\r\n", ""))
    pss = dict(zip(column_1, column_2))
    return pss


def status_of_payment_systems():
    pss = payment_systems_statuses()
    status_of_ps_ = f"AlfaBank:  {pss['AlfaBank']} \n" \
                    f"AsiaKzBank: {pss['AsiaKzBank']}\n" \
                    f"BANKOCEAN: {pss['BANKOCEAN']}\n" \
                    f"Mixplat: {pss['Mixplat']}\n" \
                    f"PaySendBank: {pss['PaySendBank']}\n" \
                    f"QiwiBank: {pss['QiwiBank']}\n" \
                    f"Rapida: {pss['Rapida']}\n" \
                    f"ROBOKassa: {pss['ROBOKassa']}\n" \
                    f"RIBPayToAnyReq: {pss['RIBPayToAnyReq']}\n" \
                    f"YandexMerchant: {pss['YandexMerchant']}"
    return status_of_ps_


def concise_status_of_payment_systems():
    pss = payment_systems_statuses()
    del pss['A2C']
    del pss['RussianStandardBank']
    alarm = ''
    warning = ''
    for payment_system, status in pss.items():
        if status == 'частично работает':
            j = payment_system + ' ' + status + '💤🔵' + '\n'
            warning += j
        if status == 'не работает' or status == 'отключена':
            j = payment_system + ' ' + status + '🛑' + '\n'
            alarm += j
        else:
            pass
    if alarm != '' and warning != '':
        return warning + ' ' + alarm
    elif alarm != '' and warning == '':
        return alarm
    elif alarm == '' and warning != '':
        return 'ОК, но...\n' + warning
    else:
        return 'ОК ✅\n'


