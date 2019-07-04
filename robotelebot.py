# -- coding: utf-8 -*-

import logging
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from comandtext import inv_check_param, inv_PState_text, inv_webstatus, inv_all_about_bot, SkpSupport_info, start_text, passportfiz_ident
from config import botpath as botpath
from all_operations import operation_text, RabbitMq_status

# Логгирование
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename=botpath
                    )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
RabbitMq_text =RabbitMq_status()
BOTTOKEN = 'tokjen' #мерч бот
TIMER = 43200
#-------------------------------------------

chatik = '-1001221778947' # '-1001221778947' - мой чат, # '-1001102275465' - STS, 1349957221
tr_knopka ='-1001349957221' #'@channelrobo' #'-1001349957221'

def test_info(bot, update):
    update.message.reply_text(passportfiz_ident())
def start(bot, update):
    update.message.reply_text(start_text)
# присылает состояние сайтов и операций
def callback_timer(bot, update):
    bot.send_message(chat_id=tr_knopka,
                     text=inv_check_param())
    bot.send_message(chat_id=tr_knopka,
                     text=inv_webstatus())
#состояние сайтов и операций для чата стс
def warning_all(bot, update):
    bot.send_message(chat_id=chatik,
                     text=inv_check_param())
    bot.send_message(chat_id=chatik,
                     text=inv_webstatus())
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
    # инструкция
    dp.add_handler(CommandHandler("start", start))
    # Запускаем так, чтобы каждые 6 часов робот писал в чатик
    updater.job_queue.run_repeating(callback_timer, interval=TIMER, first=0)
    # Команды для общего чатика СТС
    dp.add_handler(CommandHandler("stsbotsstate", botsstate))
    dp.add_handler(CommandHandler("warning", warning_all))
    # -------------------------
    dp.add_handler(CommandHandler("stsbotsstate", botsstate))  # '-1001102275465' - STS,
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
