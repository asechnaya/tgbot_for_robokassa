# -- coding: utf-8 -*-
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler

import datetime
import scoring
from operations import OperationSts
from support import SkpSupport
from parametres import Robowebsites
from payment_status import payment_state
from config import botpath as botpath

chatik = '-100 номер чатика'
BOTTOKEN = '%bot token'
TIMER = 43200 #12 часов
tr_kn = '-100 номер канала'

# Логгирование
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename=botpath
                    )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
RabbitMq_text = scoring.RabbitMq_text()
#-------------------------------------------


def inv_check_param():
    return 'Cписок контрольных параметров системы: на {}: \n\n{}8. {}\n9. RabbitMq {}{}\n' \
           '10. Состояние роботов {}'.format(datetime.datetime.now(),
                                             OperationSts(scoring.operations_text()).info(),
                                             inv_PsStates_info(),
                                             *scoring.RabbitMq_text()[0:len(RabbitMq_text)],
                                             scoring.bot_state_text())


def inv_PsStates_info():
    return 'Состояние платежных систем:\n  {} \n   {} \n   {} \n   {} \n   {}\n     {}'.format(
                                                                                                     payment_state(*scoring.mixplat_text()),
                                                                                                     payment_state(*scoring.mobilewallet_text()),
                                                                                                     payment_state(*scoring.alfabank_text()),
                                                                                                     payment_state(*scoring.PaySendBank_text()),
                                                                                                     payment_state(*scoring.OceanBank_text()),
                                                                                                     payment_state(*scoring.QiwiBank_text())
                                                                                                )
def inv_webstatus():
    return 'Проверка сайтов: на {}: \n \n{}'.format(datetime.datetime.now(), Robowebsites().info())

def inv_about_bot():
    return 'Состояние ботов:\n{}'.format(scoring.bot_state_text())

def inv_all_about_bot():
    return 'Состояние ботов:\n{}'.format(scoring.all_bot_state_text())

def SkpSupport_info():
    return 'Для клиентской поодержки {}:\n{}'.format(datetime.datetime.now(), SkpSupport(scoring.inv_skp()).info())





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

def start(bot, update):
    update.message.reply_text(start_text)

# присылает состояние сайтов и операций
def callback_timer(bot, update):
    bot.send_message(chat_id=tr_kn,
                     text=inv_check_param())
    bot.send_message(chat_id=tr_kn,
                     text=inv_webstatus())


#-- все вместе

def sys_check_param(bot, update):
    update.message.reply_text(inv_check_param())

def allstat_sts(bot, update):
    bot.send_message(chat_id=chatik,  
                     text=inv_check_param())

# рассказывает о ботах
def botsstate(bot, update):
    bot.send_message(chat_id=chatik,  
                     text=inv_all_about_bot())

    
# просто пишет сообщения о ботах, операциях и сайтах

def warning_web(bot, update):
    update.message.reply_text(inv_webstatus())

def warning_operation(bot, update):
    update.message.reply_text(OperationSts(scoring.operations_text()).info())

def warning_bot(bot, update):
    update.message.reply_text(inv_all_about_bot())

def warning_PsStates_info(bot, update):
    update.message.reply_text(inv_PsStates_info())

def warning_SkpSupport_info(bot, update):
    update.message.reply_text(SkpSupport_info())

def warning_Support_info(bot, update):
    bot.send_message(chat_id=chatik, 
                     text=SkpSupport_info)

def main():

    updater = Updater(BOTTOKEN)
    dp = updater.dispatcher  # принимает входящие сообщения и посылает их куда-то
    #инструкция
    dp.add_handler(CommandHandler("start", start))

    # Запускаем так, чтобы каждые 12 часов робот писал в чатик
    updater.job_queue.run_repeating(callback_timer, interval=TIMER, first=0)

    #Команды для общего чатика
    dp.add_handler(CommandHandler("stsbotsstate", botsstate))
    dp.add_handler(CommandHandler("warning", callback_timer))
    dp.add_handler(CommandHandler("allstat_sts", allstat_sts))
    #-------------------------
    #Команды для индвидуальной обработки
    dp.add_handler(CommandHandler("webstatus", warning_web))
    dp.add_handler(CommandHandler("operation", warning_operation))
    dp.add_handler(CommandHandler("warning_bot", warning_bot))
    dp.add_handler(CommandHandler("PsStates", warning_PsStates_info))
    dp.add_handler(CommandHandler("SkpSupport", warning_SkpSupport_info))
    dp.add_handler(CommandHandler("Support", warning_Support_info))
    dp.add_handler(CommandHandler("sys_check_param", sys_check_param))

    # Handler -- обработчик
    updater.start_polling()  # отправь эти данные платформе телеграм
    updater.idle()  # Жди, пока тебе телеграм что-то пришлет


if __name__ == '__main__':
    main()

