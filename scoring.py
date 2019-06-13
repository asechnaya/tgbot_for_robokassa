# -- coding: utf-8 -*-

import html2text
import requests
import use_pfx_with_requests
from config import pfx_path as pfx_path, pfx_password as pfx_password

statistics = 'https://admin.roboxchange.com/admin2/Face/Statistics'
botsstate = 'https://admin.roboxchange.com/admin2/Face/BotsState'
mobilewallet = 'https://admin.roboxchange.com/admin2/Face/PsCheck?PsLabel=MobileWallet'
mixplat = 'https://admin.roboxchange.com/admin2/Face/PsCheck?PsLabel=Mixplat'
alfabank = 'https://admin.roboxchange.com/admin2/Face/PsCheck?PsLabel=AlfaBank'
RabbitMq = 'https://admin.roboxchange.com/admin2/Face/RabbitMqMonitoring'
PaySendBank = 'https://admin.roboxchange.com/admin2/Face/PsCheck?PsLabel=PaySendBank'
OceanBank = 'https://admin.roboxchange.com/admin2/Face/PsCheck?PsLabel=BANKOCEAN'


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

# HOW TO USE:
with use_pfx_with_requests.pfx_to_pem(pfx_path, pfx_password) as cert:
    operations_f = requests.post(statistics, cert=cert).text
    botsstate_f = requests.post(botsstate, cert=cert).text
    mobilewallet_f = requests.post(mobilewallet, cert=cert).text
    mixplat_f = requests.post(mixplat, cert=cert).text
    alfabank_f = requests.post(alfabank, cert=cert).text
    RabbitMq_f = requests.post(RabbitMq, cert=cert).text
    PaySendBank_f = requests.post(PaySendBank, cert=cert).text
    OceanBank_f = requests.post(OceanBank, cert=cert).text

#-----------------------------------------------------------------------

    botsstate_all = parsing_operation(botsstate_f)
    operations = parsing_operation(operations_f)
    mixplat_text = parsing_operation(mixplat_f)
    mobilewallet_text = parsing_operation(mobilewallet_f)
    alfabank_text = parsing_operation(alfabank_f)
    RabbitMq_text = parsing_operation(RabbitMq_f)
    PaySendBank_text = parsing_operation(PaySendBank_f)
    OceanBank_text = parsing_operation(OceanBank_f)
    #-----------------------------------------------
    bot_state_text = BotStateStatus(botsstate_all)
    all_bot_state_text = allBotStateStatus(botsstate_all)

    # -----------------------------------------------
