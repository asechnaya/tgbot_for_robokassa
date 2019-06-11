# -- coding: utf-8 -*-

import html2text
from my_urls import operations_f, botsstate_f, mixplat_f, mobilewallet_f, alfabank_f, RabbitMq_f

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

botsstate_all = parsing_operation(botsstate_f)
botstate_status = []
botstate_status.append(botsstate_all[0:2])
botstate_status.append(botsstate_all[2:4])
botstate_status.append(botsstate_all[4:6])
botstate_status.append(botsstate_all[(len(botsstate_all))-2:(len(botsstate_all))])


def BotStateStatus(botstate_status):
    botstate_text = ''
    for item in botstate_status:
        if (' работает  ' or ' работает  ' or ' работает') in item:
            pass
        elif ('медленно') or (' медленно ') or ('медленно ') in item:
            botstate_text = botstate_text.join('ОК, но ' + item[0] + item[1])
        else:
            botstate_text = botstate_text.join('!' + item[0] + item[1])
    if botstate_text == '':
        botstate_text = botstate_text.join('ОК')
    return botstate_text

def allBotStateStatus(botstate_status):
    my_list= list()
    my_string = ''
    for item in botstate_status:
        my_list.append(item[0])
        my_list.append(item[1])
        my_list.append('\n')
    my_string = my_string.join(my_list)
    return my_string



operations = parsing_operation(operations_f)

mixplat_text = parsing_operation(mixplat_f)
mobilewallet_text = parsing_operation(mobilewallet_f)
alfabank_text = parsing_operation(alfabank_f)
RabbitMq_text = parsing_operation(RabbitMq_f)
bot_state_text = BotStateStatus(botstate_status)
all_bot_state_text = allBotStateStatus(botstate_status)
