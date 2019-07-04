import requests
from bs4 import BeautifulSoup
from config import certpath
cert = certpath

def operation_text():
    with requests.Session() as s:
        r = s.post('https://admin.roboxchange.com/admin2/Face/Statistics', cert=cert)
    html_doc=r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    newident = soup.select("tr > td")
    mydic=[]
    for element in newident:
        mydic.append(element.get_text(strip=True))
    opertext=[]
    k=0
    numbers = [1, 2, 3, 4, 5, 6, 9, 10, 19, 20, 25, 26, 27, 28]
    for i in numbers:
        if i%2 !=0:
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
    html_doc=r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    k=soup.select("td.col-lg-4, td.col-lg-5")
    mydic=[]
    for el in k:
        mydic.append(el.get_text(strip=True))
    pstext=[]
    numbers = [2, 3, #alfa
               4, 5, #KZ
               6, 7, #Ocean
               20, 21, #Mixplat
               25, 26, #MobileWallet
               30, 31,
               32, 33,
               46, 47]
    i=0
    for a in numbers:
        pstext.append(mydic[a])
        i +=1
        if i%2 ==0:
             pstext.append('\n')
        else:
             pstext.append(': ')
    my_string = ''
    my_string=my_string.join(pstext)
    return my_string
print(allPSState_text())


def PSState_text():
    with requests.Session() as s:
        r = s.post('https://admin.roboxchange.com/admin2/Face/PsStates', cert=cert)
    html_doc=r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    k=soup.select("td.col-lg-4, td.col-lg-5")
    mydic=[]
    for el in k:
        mydic.append(el.get_text(strip=True))
    pstext=[]
    numbers = [2, 3, #alfa
               4, 5, #KZ
               6, 7, #Ocean
               20, 21, #Mixplat
               25, 26, #MobileWallet
               30, 31,
               32, 33,
               46, 47]

    for a in (numbers):
        pstext.append(mydic[a])

    alarm = ''
    warning=''
    k=-1
    for p in pstext:
        k +=1
        if p == 'частично работает':
            j = str(pstext[k-1])+' '+str(pstext[k]) + '💤🔵' + '\n'
            warning += j
        if (p == 'не работает' or p == 'отключена'):
            j = str(pstext[k-1])+' '+str(pstext[k]) + '🛑'+'\n'
            alarm += j
        else:
            pass
    if alarm !='' and warning !='':
        return (warning+' '+ alarm)
    elif (alarm !='' and warning == ''):
        return (alarm)
    elif (alarm =='' and warning != ''):
        return (warning)
    else:
        return 'ОК ✅'


def RabbitMq_status():
    with requests.Session() as s:
        r = s.post('https://admin.roboxchange.com/admin2/Face/RabbitMqMonitoring', cert=cert)
    html_doc=r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    newident = soup.select("td", {"class": "col-lg-3 text-right"})
    mydic=''
    for element in newident:
        mydic=element.get_text(strip=True)
    if mydic =='ok':
        mydic=('ОК ✅')
    else:
        mydic.join('🛑')
    return mydic

def BotStateStatus():
    with requests.Session() as s:
        r = s.post('https://admin.roboxchange.com/admin2/Face/BotsState', cert=cert)
    html_doc=r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    newident = soup.select(".col-lg-9, .col-lg-3")
    mydic=[]
    bttext=[]
    for element in newident:
        mydic.append(element.get_text(strip=True))
    numbers = [0, 1, 2, 3, 4, 5, 14, 15]
    for a in (numbers):
        bttext.append(mydic[a])
    alarm = ''
    warning = ''
    k = -1
    for p in bttext:
        k += 1
        if p == 'частично работает':
            j = str(bttext[k - 1]) + ' ' + str(bttext[k]) + '😢' + '\n'
            warning += j
        if (p == 'не работает' or p == 'отключена'):
            j = str(bttext[k - 1]) + ' ' + str(bttext[k]) + '🛑' + '\n'
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
        return 'ОК ✅'

def allBotStateStatus():
    with requests.Session() as s:
        r = s.post('https://admin.roboxchange.com/admin2/Face/BotsState', cert=cert)
    html_doc=r.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    k = soup.select(".col-lg-9, .col-lg-3")
    mydic=[]
    for el in k:
        mydic.append(el.get_text(strip=True))
    bttext=[]
    numbers = [0, 1, 2, 3, 4, 5, 14, 15]
    i = 0
    for a in numbers:
        bttext.append(mydic[a])
        i += 1
        if i % 2 == 0:
            bttext.append('\n')
        else:
            bttext.append(' ')
    my_string = ''
    my_string = my_string.join(bttext)
    return my_string