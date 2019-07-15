import requests
import time
import re
from bs4 import BeautifulSoup

from config import certpath, payload as payload


cert = certpath


def operation_text():
    with requests.Session() as s:
        r = s.post('https://admin.roboxchange.com/admin2/Face/Statistics', cert=cert)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    newident = soup.select("tr > td")
    mydic = []
    for element in newident:
        mydic.append(element.get_text(strip=True))
    opertext = []
    k = 0
    numbers = [1, 2, 3, 4, 5, 6, 9, 10, 19, 20, 25, 26, 27, 28]
    for i in numbers:
        if i % 2 != 0:
            k += 1
            opertext.append(str(k))
            opertext.append('. ')
            opertext.append(mydic[i])
            opertext.append(': ')
        else:
            opertext.append(mydic[i])
            opertext.append('\n')
    my_string = ''
    my_string = my_string.join(opertext)
    return my_string


def allPSState_text():
    with requests.Session() as s:
        r = s.post('https://admin.roboxchange.com/admin2/Face/PsStates', cert=cert)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    k = soup.select("td.col-lg-4, td.col-lg-5")
    mydic = []
    for el in k:
        mydic.append(el.get_text(strip=True))
    d = {mydic[i]: mydic[i + 1] for i in range(0, len(mydic), 2)}
    try:
        del d['RussianStandardBank']
        del d['A2C']
        del d['EmptyPs']
        del d['Биокоин']
    except KeyError:
        pass
    my_string = """
        AlfaBank:  {}
        AsiaKzBank: {}
        BANKOCEAN: {}
        Mixplat: {}
        PaySendBank: {}
        QiwiBank: {}
        Rapida: {}
        ROBOKassa: {}
        RIBPayToAnyReq: {}
        YandexMerchant: {}
    """.format(d['AlfaBank'], d['AsiaKzBank'], d['BANKOCEAN'], d['Mixplat'],
               d['PaySendBank'], d['QiwiBank'], d['Rapida'], d['RIBPayToAnyReq'],
               d['ROBOKassa'], d['YandexMerchant'])
    return my_string


def PSState_text():
    with requests.Session() as s:
        r = s.post('https://admin.roboxchange.com/admin2/Face/PsStates', cert=cert)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    k = soup.select("td.col-lg-4, td.col-lg-5")
    mydic = []
    for el in k:
        mydic.append(el.get_text(strip=True))
    d = {mydic[i]: mydic[i + 1] for i in range(0, len(mydic), 2)}
    try:
        del d['RussianStandardBank']
        del d['A2C']
        del d['EmptyPs']
        del d['Биокоин']
    except KeyError:
        pass
    my_string = """AlfaBank:  {}
        AsiaKzBank: {}
        BANKOCEAN: {}
        Mixplat: {}
        PaySendBank: {}
        QiwiBank: {}
        Rapida: {}
        RIBPayToAnyReq: {}
        VTB24: {}
        YandexMerchant: {}
    """.format(d['AlfaBank'], d['AsiaKzBank'], d['BANKOCEAN'], d['Mixplat'],
               d['PaySendBank'], d['QiwiBank'], d['Rapida'], d['RIBPayToAnyReq'],
               d['VTB24'], d['YandexMerchant'])
    alarm = ''
    warning = ''
    for k, v in d.items():
        if v == 'частично работает':
            j = k + ' ' + v + '💤🔵' + '\n'
            warning += j
        if (v == 'не работает' or v == 'отключена'):
            j = k + ' ' + v + '🛑' + '\n'
            alarm += j
        else:
            pass
    if alarm != '' and warning != '':
        return (warning + ' ' + alarm)
    elif (alarm != '' and warning == ''):
        return (alarm)
    elif (alarm == '' and warning != ''):
        return ('ОК, но...\n' + warning)
    else:
        return 'ОК ✅\n'


def RabbitMq_status():
    with requests.Session() as s:
        r = s.post('https://admin.roboxchange.com/admin2/Face/RabbitMqMonitoring', cert=cert)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    newident = soup.select("td", {"class": "col-lg-3 text-right"})
    mydic = ''
    for element in newident:
        mydic = element.get_text(strip=True)
    if mydic == 'ok':
        mydic = ('ОК ✅')
    else:
        mydic.join('🛑')
    return mydic


def BotStateStatus():
    with requests.Session() as s:
        r = s.post('https://admin.roboxchange.com/admin2/Face/BotsState', cert=cert)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    newident = soup.select(".col-lg-9, .col-lg-3")
    mydic = []
    for element in newident:
        mydic.append(element.get_text(strip=True))
    d = {mydic[i]: mydic[i + 1] for i in range(0, len(mydic), 2)}
    bttext = {
        'Автомат': d['Автомат:'],
        'Сервис запуска ботов': d['Сервис запуска ботов:'],
        'Сервис подтверждений OCEAN': d['Сервис подтверждений OCEAN:'],
        'Сервис учетной системы': d['Сервис учетной системы:']}
    alarm = ''
    warning = ''
    for k, v in bttext.items():
        if v == 'частично работает' or v == 'работает медленно':
            j = k + ': ' + v + '😢' + '\n'
            warning += j
        if (v == 'не работает' or v == 'отключена'):
            j = k + ': ' + v + '🛑' + '\n'
            alarm += j
        else:
            pass
    if alarm != '' and warning != '':
        return (warning + ' ' + alarm)
    elif (alarm != '' and warning == ''):
        return (alarm)
    elif (alarm == '' and warning != ''):
        return (warning)
    else:
        return 'ОК ✅\n'


def allBotStateStatus():
    with requests.Session() as s:
        r = s.post('https://admin.roboxchange.com/admin2/Face/BotsState', cert=cert)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    newident = soup.select(".col-lg-9, .col-lg-3")
    mydic = []
    for element in newident:
        mydic.append(element.get_text(strip=True))
    d = {mydic[i]: mydic[i + 1] for i in range(0, len(mydic), 2)}
    my_string = """
    Автомат: {}
    Сервис запуска ботов: {}
    Сервис подтверждений OCEAN: {}
    Сервис учетной системы: {}
    """.format(d['Автомат:'], d['Сервис запуска ботов:'], d['Сервис подтверждений OCEAN:'],
               d['Сервис учетной системы:'])
    return my_string


def webcheck(d):
    newd = {}
    for key, value in d.items():
        try:
            r = requests.get(value).status_code
            if r == 200 or r == 403:
                newd[key] = 'OK ✅'
            else:
                newd[key] = {r: '😱😱❗😱😱❗😱😱 СЛОМАЛОСЬ\n 😱😱❗😱😱❗😱😱'}
        except EnvironmentError as e:
            newd[key] = {e: '😱😱❗😱😱❗😱😱'}
    return newd


def web_info(websites):
    d = webcheck(websites)
    mystrings = ''
    i = 0
    for k, v in d.items():
        i += 1
        mystrings += str(k) + ': ' + str(v) + '\n'
    return mystrings


def inv_passfizident():
    from datetime import date, timedelta
    yesterday = date.today() - timedelta(days=0)
    today = date.today() + timedelta(days=1)
    dateTimeAfter = yesterday.strftime("%d.%m.20%y")
    #print(dateTimeAfter)
    dateTimeUntil = today.strftime("%d.%m.20%y")
    #print(dateTimeUntil)
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
        'dateTimeAfter': dateTimeAfter,
        'dateTimeUntil': dateTimeUntil,
        'fetchRows': 30,
        'X-Requested-With': 'XMLHttpRequest'
    }

    data='reqType=identification&pageNumber=1&sortDirection=CreatedAsc&assigned=NULL&merchantType=MerchantOff&PartnerCountry=RU&PartnerIdentifier=&ShopIdentifier=&reqState=-1&DateType=modified&dateTimeAfter=07.07.2019&dateTimeUntil=08.07.2019&fetchRows=30&X-Requested-With=XMLHttpRequest'
    with requests.Session() as s:
        r = s.post('https://admin.roboxchange.com/admin2/ClientRequests/List?Length=13', data=payload, cert=cert)
    html_doc = r.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    newident = soup.find_all("td", {"class": "hideme"}, string=re.compile('Identification_Subject'))
    nident = soup.find("span", {"style": "float:right;"}, text=re.compile('Всего заявок')).get_text(strip=True)
    i = 0
    mydict={}
    for element in newident:
        i += 1
        #print(repr(element.get_text(strip=True)))
    print(nident)
    return 'Физиков идентифицировано по паспорту за сегодня: {}'.format(i)


def inv_skp():
    with requests.Session() as s:
        r = s.post('http://support.robokassa.ru/ActiveIssues.aspx?', cookies=payload)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    newident = soup.select("ul > a")
    mydic = []
    for element in newident:
        mydic.append(element.get_text(strip=True))
    opertext = []
    i = 0
    for item in mydic:
        opertext.append(item)
        opertext.append('\n')
    my_string = ''
    my_string = my_string.join(opertext)
    return my_string


