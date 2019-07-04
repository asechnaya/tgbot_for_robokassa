# -- coding: utf-8 -*-

import logging
from telegram.ext import Updater, CommandHandler
import datetime
import time
from support import SkpSupport
from parametres import Robowebsites
from config import botpath as botpath
from all_operations import operation_text, allPSState_text, PSState_text, RabbitMq_status, BotStateStatus, allBotStateStatus

# Логгирование
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename=botpath
                    )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
RabbitMq_text =RabbitMq_status()
BOTTOKEN = '806792791:AAFCfdFRWf_Bg7kywHVuZBWdPsXY3pWiWHw' #мерч бот
#505329679:AAGhgsa4ymrOTUWJgWwKZirTXBjLpqc1WYs
#821731132:AAFQEQOBsequ3ljKlG_6KU_uv37hogODT_M

TIMER = 43200
#-------------------------------------------



def inv_check_param():
    return 'Cписок контрольных параметров системы: на {} (UTC): \n\n{}8. Состояние платежных систем: \n{}9. RabbitMq: {}\n' \
           '10. Состояние роботов {}'.format(time.strftime("%d.%m.%Y %H:%m:%S"),
                                             operation_text(),
                                             PSState_text(),
                                             RabbitMq_status(),
                                             BotStateStatus())

def inv_PState_text():
    return 'Состояние платежных систем: \n{}'.format(allPSState_text())


def inv_webstatus():
    return 'Проверка сайтов: на {}: \n \n{}'.format(datetime.datetime.now(), Robowebsites().info())

def inv_all_about_bot():
    return 'Состояние ботов:\n{}'.format(allBotStateStatus())

def SkpSupport_info():
    return 'Для клиентской поддержки {}:\n{}'.format(datetime.datetime.now(), SkpSupport(scoring.inv_skp()).info())

def test_info(bot, update):
    update.message.reply_text(operation_text())


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


chatik = '-1001221778947' # '-1001221778947' - мой чат, # '-1001102275465' - STS, -1001349957221- тр кнопка

def start(bot, update):
    update.message.reply_text(start_text)

# присылает состояние сайтов и операций
def callback_timer(bot, update):
    bot.send_message(chat_id='-1001102275465',
                     text=inv_check_param())
    bot.send_message(chat_id='-1001102275465',
                     text=inv_webstatus())

# просто пишет сообщения о ботах, операциях и сайтах

def warning_web(bot, update):
    update.message.reply_text(inv_webstatus())

def warning_operation(bot, update):
    update.message.reply_text(operation_text())

def warning_bot(bot, update):
    update.message.reply_text(inv_all_about_bot())

def warning_PsStates_info(bot, update):
    update.message.reply_text(inv_PState_text())

def warning_SkpSupport_info(bot, update):
    update.message.reply_text(SkpSupport_info())

def warning_Support_info(bot, update):
    bot.send_message(chat_id=chatik,  # '-1001102275465' - STS,
                     text=SkpSupport_info())
# рассказывает о ботах
def botsstate(bot, update):
    bot.send_message(chat_id=chatik,  # '-1001102275465' - STS,
                     text=inv_all_about_bot())

#-- все вместе

def sys_check_param(bot, update):
    update.message.reply_text(inv_check_param())

def allstat_sts(bot, update):
    bot.send_message(chat_id=chatik,  # '-1001102275465' - STS,
                     text=inv_check_param())




def main():

    updater = Updater(BOTTOKEN)
    dp = updater.dispatcher  # принимает входящие сообщения и посылает их куда-то
    #инструкция
    dp.add_handler(CommandHandler("start", start))

    # Запускаем так, чтобы каждые 12 часов робот писал в чатик
    #updater.job_queue.run_repeating(callback_timer, interval=TIMER, first=0)



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
    dp.add_handler(CommandHandler("test", test_info))


    # Handler -- обработчик
    updater.start_polling()  # отправь эти данные платформе телеграм
    updater.idle()  # Жди, пока тебе телеграм что-то пришлет




if __name__ == '__main__':
    main()
