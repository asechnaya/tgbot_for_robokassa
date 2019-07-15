import logging
import time
from datetime import time as timer

from telegram import Sticker
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from comandtext import inv_check_param, inv_PState_text, inv_webstatus, inv_all_about_bot, SkpSupport_info, start_text, \
    passportfiz_ident
from config import botpath, BOTTOKEN, chatik, tr_knopka
from all_operations import operation_text, BotStateStatus, allBotStateStatus, PSState_text, allPSState_text

myphoto = 'https://s.tcdn.co/18f/4d5/18f4d57e-c910-3aef-9523-9a0d3bb60468/thumb128.png'
# Логгирование
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename=botpath
                    )
TIMER = 60
# -------------------------------------------

def passport_info(bot, update):
    update.message.reply_text(passportfiz_ident())

from telegram.utils.helpers import escape_markdown

def test(bot, update):
    #https://s.tcdn.co/18f/4d5/18f4d57e-c910-3aef-9523-9a0d3bb60468/thumb128.png
    user_text= bot.send_photo(chat_id=update.message.chat_id, photo=myphoto)

def start(bot, update):
    update.message.reply_text(start_text)

# присылает состояние сайтов и операций
def callback_timer(bot, update):
    bot.send_message(chat_id=tr_knopka,
                     text=inv_check_param())
    bot.send_message(chat_id=tr_knopka,
                     text=inv_webstatus())

# состояние сайтов и операций для чата стс
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
# -- все вместе
def sys_check_param(bot, update):
    print('hi')
    update.message.reply_text(inv_check_param())

def allstat_sts(bot, update):
    bot.send_message(chat_id=chatik,  # '-1001102275465' - STS,
                     text=inv_check_param())

def printclock(bot, update):
    bs = BotStateStatus()
    ps = PSState_text()
    keyword =['не работает', 'отключена']
    for key in keyword:
        if key in ps:
            bot.send_message(chat_id='-1001290037577',  # '-1001102275465' - STS,
            text=allPSState_text())
            bot.send_photo(chat_id='-1001290037577', photo=myphoto)
        if key in bs:
            bot.send_message(chat_id='-1001290037577',  # '-1001102275465' - STS,
                             text=BotStateStatus())
            bot.send_photo(chat_id='-1001290037577', photo=myphoto)


def main():
    updater = Updater(BOTTOKEN)
    dp = updater.dispatcher  # принимает входящие сообщения и посылает их куда-то
    # инструкция
    dp.add_handler(CommandHandler("start", start))
    # Запускаем так, чтобы каждые 6 часов робот писал в чатик
    updater.job_queue.run_daily(callback_timer, time=timer(6, 1, 17))
    updater.job_queue.run_daily(callback_timer, time=timer(17, 55, 17))
    updater.job_queue.run_repeating(printclock, interval=TIMER, first=0)
    # Команды для общего чатика СТС
    # -------------------------
    dp.add_handler(CommandHandler("allstat_sts", allstat_sts))  # '-1001102275465' - STS,
    dp.add_handler(CommandHandler("warning_all", warning_all))  # '-1001102275465' - STS,
    dp.add_handler(CommandHandler("stsbotsstate", botsstate))  # '-1001102275465' - STS,
    dp.add_handler(CommandHandler("SkpSupport_sts", warning_Support_info)) # '-1001102275465' - STS,
    # -------------------------
    dp.add_handler(CommandHandler("warning", callback_timer))  # 'trev knopka',
    # -------------------------
    dp.add_handler(CommandHandler("SkpSupport", warning_SkpSupport_info))
    dp.add_handler(CommandHandler("webstatus", warning_web))
    dp.add_handler(CommandHandler("operation", warning_operation))
    dp.add_handler(CommandHandler("warning_bot", warning_bot))
    dp.add_handler(CommandHandler("PsStates", warning_PsStates_info))
    dp.add_handler(CommandHandler("Support", warning_Support_info))
    dp.add_handler(CommandHandler("sys_check_param", sys_check_param))
    dp.add_handler(CommandHandler("test", passport_info))
    dp.add_handler(CommandHandler("passport", passport_info))
    dp.add_handler(MessageHandler(Filters.text, test))

    updater.start_polling()  # отправь эти данные платформе телеграм
    updater.idle()  # Жди, пока тебе телеграм что-то пришлет


if __name__ == '__main__':
    main()
