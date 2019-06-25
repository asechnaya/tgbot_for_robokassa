# -- coding: utf-8 -*-

import html2text
import requests
import use_pfx_with_requests
from config import pfx_path as pfx_path, pfx_password as pfx_password, payload as payload, certpath as certpath

s = requests.Session()
s.cert =certpath
cert = s.cert

statistics = 'https://admin.roboxchange.com/admin2/Face/Statistics'
botsstate = 'https://admin.roboxchange.com/admin2/Face/BotsState'
mobilewallet = 'https://admin.roboxchange.com/admin2/Face/PsCheck?PsLabel=MobileWallet'
mixplat = 'https://admin.roboxchange.com/admin2/Face/PsCheck?PsLabel=Mixplat'
alfabank = 'https://admin.roboxchange.com/admin2/Face/PsCheck?PsLabel=AlfaBank'
RabbitMq = 'https://admin.roboxchange.com/admin2/Face/RabbitMqMonitoring'
PaySendBank = 'https://admin.roboxchange.com/admin2/Face/PsCheck?PsLabel=PaySendBank'
OceanBank = 'https://admin.roboxchange.com/admin2/Face/PsCheck?PsLabel=BANKOCEAN'
QiwiBank = 'https://admin.roboxchange.com/admin2/Face/PsCheck?PsLabel=QiwiBank'

def parsing_operation(file):
    h = html2text.HTML2Text()
    # Ignore converting links from HTML
    h.ignore_links = True
    New_Text = h.handle(file)
    if 'работает |  chk' in New_Text:
        New_Text = New_Text.replace('работает |  chk', 'работает')
    if '96' in New_Text:
        New_Text = New_Text.replace('96', '')
    New_Text = New_Text.replace(' | ', '\n')
    New_Text = New_Text.split('\n')
    New_Text_list = list()
    for item in New_Text:
        if not item:
            pass
        elif item == '---|---  ':
            pass
        elif item == '---|---':
            pass
        elif item == '---  ':
            pass
        elif item == 'Обновление...  ':
            pass
        elif item == '  ':
            pass
        else:
            New_Text_list.append(item)
    del New_Text_list[0]
    return New_Text_list



def BotStateStatus(botsstate_all):
    botstate_text = ''
    botstate_status = []
    botstate_status.append(botsstate_all[0:2])
    botstate_status.append(botsstate_all[2:4])
    botstate_status.append(botsstate_all[4:6])
    botstate_status.append(botsstate_all[(len(botsstate_all)) - 2:(len(botsstate_all))])
    for item in botstate_status:
        if (' работает  ') or (' работает  ') or (' работает') in item:
            pass
        elif ('медленно') or (' медленно ') or ('медленно ') in item:
            botstate_text = botstate_text.join('ОК, но ' + item[0] + item[1]+'😢')
        else:
            botstate_text = botstate_text.join('!' + item[0] + item[1]+'🛑')
    if botstate_text == '':
        botstate_text = botstate_text.join('ОК ✅')
    return botstate_text

def allBotStateStatus(botsstate_all):
    botstate_status = []
    botstate_status.append(botsstate_all[0:2])
    botstate_status.append(botsstate_all[2:4])
    botstate_status.append(botsstate_all[4:6])
    botstate_status.append(botsstate_all[(len(botsstate_all)) - 2:(len(botsstate_all))])
    my_list= list()
    my_string = ''
    for item in botstate_status:
        my_list.append(item[0])
        my_list.append(item[1])
        my_list.append('\n')
    my_string = my_string.join(my_list)
    return my_string

def inv_skp():
    with requests.Session() as s:
        dd = s.post('http://support.robokassa.ru/ActiveIssues.aspx?', cookies=payload)
    return parsing_operation(dd.text)


# HOW TO USE:
# --------------------------------------------------------------------

#-----------------------------------------------
def inv_OceanBank_f():
    #with use_pfx_with_requests.pfx_to_pem(pfx_path, pfx_password) as cert:
    return requests.post(OceanBank, cert=cert, timeout=(3.05, 27)).text

def OceanBank_text():
    return (parsing_operation(inv_OceanBank_f()))
# --------------------------------------------------------------------
def inv_alfabank_f():
    #with use_pfx_with_requests.pfx_to_pem(pfx_path, pfx_password) as cert:
    return requests.post(alfabank, cert=cert, timeout=(3.05, 27)).text

def alfabank_text():
    return (parsing_operation(inv_alfabank_f()))
# --------------------------------------------------------------------

def inv_PaySendBank_f():
    #with use_pfx_with_requests.pfx_to_pem(pfx_path, pfx_password) as cert:
    return requests.post(PaySendBank, cert=cert, timeout=(3.05, 27)).text

def PaySendBank_text():
    return (parsing_operation(inv_PaySendBank_f()))

# --------------------------------------------------------------------
def inv_QiwiBank_f():
    #with use_pfx_with_requests.pfx_to_pem(pfx_path, pfx_password) as cert:
    return requests.post(QiwiBank, cert=cert, timeout=(3.05, 27)).text

def QiwiBank_text():
    return (parsing_operation(inv_QiwiBank_f()))
# # --------------------------------------------------------------------
def inv_mixplat_f():
    #with use_pfx_with_requests.pfx_to_pem(pfx_path, pfx_password) as cert:
    return requests.post(mobilewallet, cert=cert, timeout=(3.05, 27)).text

def mixplat_text():
    return (parsing_operation(inv_mixplat_f()))
# --------------------------------------------------------------------
def inv_mobilewallet_f():
    #with use_pfx_with_requests.pfx_to_pem(pfx_path, pfx_password) as cert:
    return requests.post(mobilewallet, cert=cert, timeout=(3.05, 27)).text

def mobilewallet_text():
    return (parsing_operation(inv_mobilewallet_f()))
# --------------------------------------------------------------------

def inv_RabbitMq_f():
    #with use_pfx_with_requests.pfx_to_pem(pfx_path, pfx_password) as cert:
    return requests.post(RabbitMq, cert=cert, timeout=(3.05, 27)).text
def RabbitMq_text():
    return (parsing_operation(inv_RabbitMq_f()))

# ---------------------------------------------------------------------

def inv_operations_f():
    #with use_pfx_with_requests.pfx_to_pem(pfx_path, pfx_password) as cert:
    return requests.post(statistics, cert=cert).text
def operations_text():
    return (parsing_operation(inv_operations_f()))
# ---------------------------------------------------------------------

def inv_botsstate_f():
    #with use_pfx_with_requests.pfx_to_pem(pfx_path, pfx_password) as cert:
    return requests.post(botsstate, cert=cert, timeout=(3.05, 27)).text

def all_bot_state_text():
    return allBotStateStatus(parsing_operation(inv_botsstate_f()))

def bot_state_text():
    return BotStateStatus(parsing_operation(inv_botsstate_f()))

# ---------------------------------------------------------------------

