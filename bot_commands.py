from statistics.statistics import current_day_statistics
from statistics.rabbit_mq import rabbit_mq
from statistics.status_of_payment_systems import status_of_payment_systems
from kazakhstan.kazakhstan import kazakhstan_operations_counter
from statistics.bots_statuses import bot_statuses
from websites.website_status import websites_status
from queries.passports import number_of_passport_identifies
from config import botpath, BOTTOKEN, chatik, tr_knopka, REQUEST_KWARGS
import pytz
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from all_operations import inv_skp

timezones = 'Europe/Moscow'
localFormat = "%Y-%m-%d %H:%M:%S"

kz_chat = '-429447678'
# kz_chat = -476235070
# g476235070
sts_chat = '-1001102275465'
# s1102275465_6631847710490334924


def start(bot, update):
    update.message.reply_text(start_text)
    print(start_text)


def kazakhstan_30_min(bot, update):
    # kz_chat = update.message.chat_id
    kazakhstan_operations_counter()
    if kazakhstan_operations_counter() > 1:
        print("Все в порядке")
    else:
        print("Нет успешных операций за час!")
        bot.send_message(chat_id=kz_chat,
                         text="@Anton_Rokhlin Нет успешных операций за час!")

def kazakhstan_count_operations(bot, update):
    # kz_chat = update.message.chat_id
    kazakhstan_operations_counter()
    if kazakhstan_operations_counter() > 1:
        print("Все в порядке")
        update.message.reply_text(f"Все хорошо, {kazakhstan_operations_counter()} операций")
    else:
        print("Нет успешных операций за час!")
        update.message.reply_text("Нет успешных операций за час!")



def print_day_statistics(bot, update):
    print(current_day_statistics())
    update.message.reply_text(current_day_statistics())


def print_bots_statuses(bot, update):
    print("bot")
    update.message.reply_text(f'   Состояние ботов:\n{bot_statuses()}')


def print_payment_systems_info(bot, update):
    update.message.reply_text(status_of_payment_systems())


def print_websites_status(bot, update):
    update.message.reply_text(f'Проверка сайтов: на {ourtime()}: \n{websites_status()}')


def print_passports_identify(bot, update):
    update.message.reply_text(number_of_passport_identifies())


def ourtime():
    return datetime.now().astimezone(pytz.timezone(timezones)).strftime(localFormat)

# -- Прописываем контрольные точки
def print_control_points(bot, update):
    print("Пишем контрольные точки")
    update.message.reply_text(f"Cписок контрольных параметров системы {ourtime()}: \n"
                              f"{current_day_statistics()} \n"
                              f"*Состояние платежных систем*: \n{status_of_payment_systems()}\n"
                              f"RabbitMq: {rabbit_mq()}\n"
                              f"Состояние роботов {bot_statuses()}")

def send_sts_bot_states(bot, update):
    bot.send_message(chat_id=chatik,  # '-1001102275465' - STS,
                     text=f'   Состояние ботов:\n{bot_statuses()}')

def send_sts_control_points(bot, update):
    bot.send_message(chat_id=chatik,  # '-1001102275465' - STS,
                     text=f"Cписок контрольных параметров системы {ourtime()}: \n"
                              f"{current_day_statistics()} \n"
                              f"*Состояние платежных систем*: \n{status_of_payment_systems()}\n"
                              f"RabbitMq: {rabbit_mq()}\n"
                              f"Состояние роботов {bot_statuses()}")

def send_sts_control_points_and_webs(bot, update):
    bot.send_message(chat_id=chatik,
                     text=(f"Cписок контрольных параметров системы {ourtime()}: \n"
                              f"{current_day_statistics()} \n"
                              f"*Состояние платежных систем*: \n{status_of_payment_systems()}\n"
                              f"RabbitMq: {rabbit_mq()}\n"
                              f"Состояние роботов {bot_statuses()} \n "
                              f"Проверка сайтов: на {ourtime()}: \n{websites_status()}"))


# контрольные точки в тревожку каждые 12 часов
def control_points_timer(bot, update):
    bot.send_message(chat_id=tr_knopka,
                     text=f"Cписок контрольных параметров системы {ourtime()}: \n"
                          f"{current_day_statistics()} \n"
                          f"*Состояние платежных систем*: \n{status_of_payment_systems()}\n"
                          f"RabbitMq: {rabbit_mq()}\n"
                          f"Состояние роботов {bot_statuses()}")


def SkpSupport_info():
    return 'Для клиентской поддержки {}:\n{}'.format(ourtime(), inv_skp())



def check_bs_and_ps_every_300s(bot, update):
    myphoto = 'https://s.tcdn.co/18f/4d5/18f4d57e-c910-3aef-9523-9a0d3bb60468/thumb128.png'
    bs = bot_statuses()
    ps = status_of_payment_systems()
    keyword =['не работает', 'отключена']
    for key in keyword:
        if key in ps:
            bot.send_message(chat_id=chatik,  # '-1001102275465' - STS,
            text=f'Состояние ботов:\n{bot_statuses()}')
            bot.send_photo(chat_id='-1001102275465', photo=myphoto)
        if key in bs:
            bot.send_message(chat_id=chatik,  # '-1001102275465' - STS,
                             text=status_of_payment_systems())
            bot.send_photo(chat_id='-1001102275465', photo=myphoto)




start_text ='У нас есть:\n /start - список того, что ты можешь. \n ' \
            '/warning - отправка чатик ТРЕВОЖНОЙ КНОПКИ инфы о состоянии операций и сайтов\n' \
            '/stsbotsstate - отправка в чатик СТС инфы по всем ботам,\n' \
            '/SkpSupport_sts -- про суппорт в СТС \n' \
            '/allstat_sts - по всем операциям в СТС \n ' \
            '/warning_all отправка всей инфы в СТС\n' \
            '/sys_check_param - все про все, \n' \
            '/webstatus - информация о сайтах, \n ' \
            '/operation - информация об операциях,\n' \
            '/warning_bot - информация о ботах \n' \
            '/PsStates -- информация о платежных системах \n' \
            '/passport -- тестовый режим. Количество идентифицированных физлиц за день \n' \
            '@RoboHttpPingbot - робот от Вадима, который уведомляет, если что-то отвалилось\n' \
            '/kz - состояние по Казахстану'
