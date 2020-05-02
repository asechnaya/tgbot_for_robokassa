import logging
from datetime import time as timer

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import botpath, BOTTOKEN, chatik, tr_knopka, REQUEST_KWARGS
from comandtext import inv_check_param, inv_PState_text, inv_webstatus, inv_all_about_bot
from comandtext import SkpSupport_info, start_text, passportfiz_ident
from all_operations import operation_text, BotStateStatus, PSState_text, allPSState_text

myphoto = 'https://s.tcdn.co/18f/4d5/18f4d57e-c910-3aef-9523-9a0d3bb60468/thumb128.png'
# Логгирование
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename=botpath
                    )


TIMER = 43200
# -------------------------------------------


def passport_info(bot, update):
    update.message.reply_text(passportfiz_ident())

from telegram.utils.helpers import escape_markdown

def test(bot, update):
    user_text= bot.send_photo(chat_id=update.message.chat_id, photo=myphoto)

def start(bot, update):
    update.message.reply_text(start_text)
    print(start_text)


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
    bot.send_message(chat_id=chatik,  
                     text=SkpSupport_info())


# рассказывает о ботах
def botsstate(bot, update):
    bot.send_message(chat_id=chatik,   
                     text=inv_all_about_bot())


# -- все вместе
def sys_check_param(bot, update):
    print('sys_check_param')
    update.message.reply_text(inv_check_param())



def allstat_sts(bot, update):
    bot.send_message(chat_id=chatik,  
                     text=inv_check_param())

def printclock(bot, update):
    bs = BotStateStatus()
    ps = PSState_text()
    keyword =['не работает', 'отключена']
    for key in keyword:
        if key in ps:
            bot.send_message(chat_id=chatik,  
            text=allPSState_text())
            bot.send_photo(chat_id=chatik, photo=myphoto)
        if key in bs:
            bot.send_message(chat_id=chatik,  
                             text=BotStateStatus())
            bot.send_photo(chat_id=chatik, photo=myphoto)


def main():
    updater = Updater(BOTTOKEN, request_kwargs=REQUEST_KWARGS)
    dp = updater.dispatcher  # принимает входящие сообщения и посылает их куда-то
    # инструкция
    dp.add_handler(CommandHandler("start", start))
    # Запускаем так, чтобы каждые 6 часов робот писал в чатик
    updater.job_queue.run_daily(control_points_timer, time=timer(6, 1, 17))
    updater.job_queue.run_daily(control_points_timer, time=timer(18, 35, 17))
    updater.job_queue.run_repeating(check_bs_and_ps_every_300s, interval=300, first=0)
    updater.job_queue.run_repeating(kazakhstan_30_min, interval=1800, first=0)
    # Команды для общего чатика СТС
    # -------------------------
    dp.add_handler(CommandHandler("allstat_sts", send_sts_control_points)) ,
    dp.add_handler(CommandHandler("warning_all", send_sts_control_points_and_webs))  
    dp.add_handler(CommandHandler("stsbotsstate", send_sts_bot_states))  
    dp.add_handler(CommandHandler("SkpSupport_sts", sts_warning_Support_info))  
    # -------------------------
    dp.add_handler(CommandHandler("warning", control_points_timer))  # 'trev knopka',
    # -------------------------
    dp.add_handler(CommandHandler("operation", print_day_statistics))
    dp.add_handler(CommandHandler("warning_bot", print_bots_statuses))
    dp.add_handler(CommandHandler("PsStates", print_payment_systems_info))
    dp.add_handler(CommandHandler("webstatus", print_websites_status))
    dp.add_handler(CommandHandler("sys_check_param", print_control_points))
    dp.add_handler(CommandHandler("passport", print_passports_identify))
    dp.add_handler(CommandHandler("test", test))

    # dp.add_handler(CommandHandler("SkpSupport", warning_SkpSupport_info))
    dp.add_handler(CommandHandler("kz", kazakhstan_count_operations))
    dp.add_handler(MessageHandler(Filters.text, test))



    updater.start_polling() 
    updater.idle()  

if __name__ == '__main__':
    print('hi')
    main()

