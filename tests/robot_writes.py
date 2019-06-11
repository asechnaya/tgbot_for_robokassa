# -- coding: utf-8 -*-

import datetime
import scoring
from operations import OperationSts, BotSts
from parametres import Robowebsites
from payment_status import payment_state

#-------------------------------------------
operations_p = scoring.operations
operations = OperationSts(operations_p)
operation = operations.info()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
botstate_text = scoring.bot_state_text
allbotstate_text = scoring.all_bot_state_text
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mixplat_text = payment_state(*scoring.mixplat_text)
mobilewallet_text = payment_state(*scoring.mobilewallet_text)
alfabank_text = payment_state(*scoring.alfabank_text)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
status = Robowebsites()
webstatus = status.info()
#-------------------------------------------


RabbitMq_text = scoring.RabbitMq_text

PsStates_info = 'Состояние платежных систем:\n {} \n {} \n {}'.format(mixplat_text, mobilewallet_text, alfabank_text)

check_param = 'Cписок контрольных параметров системы: на {}: \n{}8. {}\n9. RabbitMq {}{}\n10. Состояние роботов {}'.format(datetime.datetime.now(), operation, PsStates_info, *RabbitMq_text[0:2], botstate_text)

webstatus = 'Проверка сайтов: на {}: \n \n{}'.format(datetime.datetime.now(), webstatus)

botsstate = 'Состояние ботов:\n {}'.format(allbotstate_text)

allbotsstate = 'Состояние ботов:\n {}'.format(botstate_text)



start_text ='У нас есть: /start - список того, что ты можешь. \n ' \
            '/warning - отправка чатик инфы о состоянии операций и сайтов, \n' \
            '/botestate - отправка в чатик инфы по всем ботам, \n ' \
            '/webstatus - бот расскажет о сайтах, \n ' \
            '/operation - бот расскажет об операциях,\n' \
            '/botsstate - бот расскажет о ботах \n' \
            '/PsStates -- что там с миксплатом, альфой, мобайлваллет?'




def main():
    pass
    #print(start_text)
    #print(operation)
    print(allbotsstate)
    #print(botsstate)
    #print(webstatus)
    #print(PsStates_info)
    #print(RabbitMq_text)
    #print(check_param)

if __name__ == '__main__':
    main()
