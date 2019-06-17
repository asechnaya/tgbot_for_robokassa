# -- coding: utf-8 -*-

import logging

from telegram.ext import Updater, CommandHandler

import datetime
import scoring
from operations import OperationSts
from parametres import Robowebsites
from payment_status import payment_state

# Логгирование
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

#-------------------------------------------
operations_p = scoring.operations
operations = OperationSts(operations_p)
operation = operations.info()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SkpSupport_p = SkpSupport(scoring.ddd)
SkpSupport = SkpSupport_p.info()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
botsstate_all = scoring.botsstate_all
botstate_text = scoring.bot_state_text
allbotstate_text = scoring.all_bot_state_text
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mixplat_text = payment_state(*scoring.mixplat_text)
mobilewallet_text = payment_state(*scoring.mobilewallet_text)
alfabank_text = payment_state(*scoring.alfabank_text)
PaySendBank_text = payment_state(*scoring.PaySendBank_text)
OceanBank_text = payment_state(*scoring.OceanBank_text)
QiwiBank_text = payment_state(*scoring.QiwiBank_text)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
status = Robowebsites()
webstatus = status.info()
#-------------------------------------------


RabbitMq_text = scoring.RabbitMq_text

PsStates_info = 'Состояние платежных систем:\n  {} \n   {} \n   {} \n   {} \n   {}\n     {}'.format(mixplat_text, mobilewallet_text, alfabank_text, PaySendBank_text, OceanBank_text, QiwiBank_text)

check_param = 'Cписок контрольных параметров системы: на {}: \n\n{}8. {}\n9. RabbitMq {}{}\n10. Состояние роботов {}'.format(datetime.datetime.now(), operation, PsStates_info, *RabbitMq_text[0:len(RabbitMq_text)], botstate_text)

webstatus = 'Проверка сайтов: на {}: \n \n{}'.format(datetime.datetime.now(), webstatus)

about_bot = 'Состояние ботов:\n{}'.format(allbotstate_text)

SkpSupport_info = 'Для клиентской поодержки:\n{}'.format(SkpSupport)



start_text ='У нас есть:\n /start - список того, что ты можешь. \n ' \
            '/warning - отправка чатик инфы о состоянии операций и сайтов, \n' \
            '/stsbotsstate - отправка в чатик инфы по всем ботам, \n ' \
            '/sys_check_param - все про все, \n' \
            '/webstatus - бот расскажет о сайтах, \n ' \
            '/operation - бот расскажет об операциях,\n' \
            '/warning_bot - бот расскажет о ботах \n' \
            '/PsStates -- что там с миксплатом, альфой, мобайлваллет? \n' \
            '@RoboPing - робот от Вадима, который уведомляет, если что-то отвалилось\n' \
            '/SkpSupport - че-т там для СКП'


chatik = '-1001102275465' # '-1001221778947' - мой чат, # '-1001102275465' - STS,

def start(bot, update):
    update.message.reply_text(start_text)

# присылает состояние сайтов и операций
def callback_timer(bot, update):
    bot.send_message(chat_id=chatik,
                     text=check_param)
    bot.send_message(chat_id=chatik,
                     text=webstatus)

# просто пишет сообщения о ботах, операциях и сайтах

def warning_web(bot, update):
    update.message.reply_text(webstatus)

def warning_operation(bot, update):
    update.message.reply_text(operation)

def warning_bot(bot, update):
    update.message.reply_text(about_bot)

def warning_PsStates_info(bot, update):
    update.message.reply_text(PsStates_info)

def warning_SkpSupport_info(bot, update):
    update.message.reply_text(SkpSupport_info)

def warning_Support_info(bot, update):
    bot.send_message(chat_id=chatik,  # '-1001102275465' - STS,
                     text=SkpSupport_info)



#-- все вместе

def sys_check_param(bot, update):
    update.message.reply_text(check_param)

def allstat_sts(bot, update):
    bot.send_message(chat_id=chatik,  # '-1001102275465' - STS,
                     text=check_param)

# рассказывает о ботах
def botsstate(bot, update):
    bot.send_message(chat_id=chatik,  # '-1001102275465' - STS,
                     text=about_bot)



def main():
    updater = Updater("821731132:AAFQEQOBsequ3ljKlG_6KU_uv37hogODT_M")#, request_kwargs=REQUEST_KWARGS)
    dp = updater.dispatcher  # принимает входящие сообщения и посылает их куда-то
    #инструкция
    dp.add_handler(CommandHandler("start", start))

    # Запускаем так, чтобы каждые 6 часов робот писал в чатик
    #updater.job_queue.run_repeating(callback_timer, interval=28800, first=0)



    #Команды для общего чатика
    dp.add_handler(CommandHandler("stsbotsstate", botsstate))
    dp.add_handler(CommandHandler("warning", callback_timer))
    #-------------------------
    dp.add_handler(CommandHandler("webstatus", warning_web))
    dp.add_handler(CommandHandler("operation", warning_operation))
    dp.add_handler(CommandHandler("warning_bot", warning_bot))
    dp.add_handler(CommandHandler("PsStates", warning_PsStates_info))
    dp.add_handler(CommandHandler("SkpSupport", warning_SkpSupport_info))
    dp.add_handler(CommandHandler("Support", warning_Support_info))
    dp.add_handler(CommandHandler("sys_check_param", sys_check_param))
    dp.add_handler(CommandHandler("allstat_sts", allstat_sts))


    # Handler -- обработчик
    updater.start_polling()  # отправь эти данные платформе телеграм
    updater.idle()  # Жди, пока тебе телеграм что-то пришлет




if __name__ == '__main__':
    main()

