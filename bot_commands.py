import pytz
from datetime import datetime

from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from config import chatik, tr_knopka, kz_chat
from statistics.statistics import current_day_statistics, concise_statistics_of_the_day, paused_operations
from statistics.rabbit_mq import rabbit_mq
from statistics.status_of_payment_systems import status_of_payment_systems, concise_status_of_payment_systems
from kazakhstan.kazakhstan import kazakhstan_operations_counter
from statistics.bots_statuses import bot_statuses
from websites.website_status import websites_status
from queries.passports import number_of_passport_identifies
from support.support_info import support_data

moscow_zone = 'Europe/Moscow'
kazzone = 'Asia/Almaty'
localFormat = "%Y-%m-%d %H:%M:%S"


def start(bot, update):
    update.message.reply_text(start_text)
    print(start_text)


def ourtime():
    return datetime.now().astimezone(pytz.timezone(moscow_zone)).strftime(localFormat)


def print_skp(bot, update):
    update.message.reply_text(f"*Для клиентской поддержки на {ourtime()}*\n{support_data()}",
                              parse_mode=ParseMode.MARKDOWN)
    print(support_data())


def sts_warning_Support_info(bot, update):
    bot.send_message(chat_id=chatik,
                     text=f"*Для клиентской поддержки на {ourtime()}*\n{support_data()}",
                     parse_mode=ParseMode.MARKDOWN)
    print(support_data())


def kazakhstan_30_min(bot, update):
    dn = datetime.now()
    dn_msk = dn.astimezone(pytz.timezone(kazzone))
    if dn_msk in range(9, 21):
        kazakhstan_operations_counter()
        if kazakhstan_operations_counter() > 1:
            print("Все в порядке")
        else:
            print("Нет успешных операций за час!")
            bot.send_message(chat_id=kz_chat,
                             text="@Anton_Rokhlin Нет успешных операций за час!")


def russia_paused_30_min(bot, update):
    dn = datetime.now()
    dn_msk = dn.astimezone(pytz.timezone(moscow_zone))
    if dn_msk in range(9, 21):
        paused = paused_operations()
        if paused > 0:
            bot.send_message(chat_id=chatik,
                             text=f"Зависшие операции, пацаны! {paused} штук")


def kazakhstan_count_operations(bot, update):
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


def print_concise_statistics_of_the_day(bot, update):
    print(concise_statistics_of_the_day())
    update.message.reply_text(concise_statistics_of_the_day())


def print_bots_statuses(bot, update):
    print("bot")
    update.message.reply_text(f'   Состояние ботов:\n{bot_statuses()}')


def print_payment_systems_info(bot, update):
    update.message.reply_text(status_of_payment_systems())


def print_websites_status(bot, update):
    update.message.reply_text(f'Проверка сайтов: на {ourtime()}: \n{websites_status()}')


def print_passports_identify(bot, update):
    update.message.reply_text(number_of_passport_identifies())


# -- Прописываем контрольные точки
def print_control_points(bot, update):
    print("Пишем контрольные точки")
    update.message.reply_text(f"Cписок контрольных параметров системы {ourtime()}: \n"
                              f"{current_day_statistics()} \n"
                              f"*Состояние платежных систем*: \n{status_of_payment_systems()}\n"
                              f"RabbitMq: {rabbit_mq()}\n"
                              f"Состояние роботов {bot_statuses()}")


def send_sts_bot_states(bot, update):
    bot.send_message(chat_id=chatik,
                     text=f'   Состояние ботов:\n{bot_statuses()}')


def send_sts_control_points(bot, update):
    bot.send_message(chat_id=chatik,
                     text=f"Cписок контрольных параметров системы {ourtime()}: \n"
                     f"{current_day_statistics()} \n"
                     f"*Состояние платежных систем*: \n{status_of_payment_systems()}\n"
                     f"RabbitMq: {rabbit_mq()}\n"
                     f"Состояние роботов {bot_statuses()}")


def send_sts_control_points_and_webs(bot, update):
    bot.send_message(chat_id=chatik,
                     text=(f"*Cписок контрольных параметров системы на {ourtime()}*: \n"
                           f"{concise_statistics_of_the_day()}"
                           f"*Состояние платежных систем*: \n{concise_status_of_payment_systems()}\n"
                           f"*RabbitMq*: {rabbit_mq()}\n"
                           f"*Состояние роботов* {bot_statuses()}"),
                     parse_mode=ParseMode.MARKDOWN)
    bot.send_message(chat_id=chatik,
                     text=f"*Проверка сайтов на {ourtime()}*: \n{websites_status()}",
                     parse_mode=ParseMode.MARKDOWN)


# контрольные точки в тревожку каждые 12 часов
def control_points_timer(bot, update):
    bot.send_message(chat_id=tr_knopka,
                     text=(f"*Cписок контрольных параметров системы на {ourtime()}*: \n"
                           f"{concise_statistics_of_the_day()}\n"
                           f"*Состояние платежных систем*: \n{concise_status_of_payment_systems()}\n"
                           f"*RabbitMq*: {rabbit_mq()}\n"
                           f"*Состояние роботов* {bot_statuses()}"),
                     parse_mode=ParseMode.MARKDOWN)
    bot.send_message(chat_id=tr_knopka,
                     text=f"*Проверка сайтов на {ourtime()}*: \n{websites_status()}",
                     parse_mode=ParseMode.MARKDOWN)


def check_bs_and_ps_every_300s(bot, update):
    myphoto = 'https://s.tcdn.co/18f/4d5/18f4d57e-c910-3aef-9523-9a0d3bb60468/thumb128.png'
    bs = bot_statuses()
    ps = status_of_payment_systems()
    keyword = ['не работает', 'отключена']
    for key in keyword:
        if key in ps:
            bot.send_message(chat_id=chatik,
                             text=f"Состояние ботов:\n{bot_statuses()}")
            bot.send_photo(chat_id=chatik, photo=myphoto)
        if key in bs:
            bot.send_message(chat_id=chatik,
                             text=status_of_payment_systems())
            bot.send_photo(chat_id=chatik, photo=myphoto)


start_text = 'У нас есть:\n /start - список того, что ты можешь. \n ' \
             '/warning - отправка чатик ТРЕВОЖНОЙ КНОПКИ инфы о состоянии операций и сайтов\n' \
             '/stsbotsstate - отправка в чатик СТС инфы по всем ботам,\n' \
             '/SkpSupport_sts -- про суппорт в СТС \n' \
             '/allstat_sts - по всем операциям в СТС \n ' \
             '/warning_all отправка всей инфы в СТС\n' \
             '/sys_check_param - все про все, \n' \
             '/webstatus - информация о сайтах, \n ' \
             '/operation - информация об операциях,\n' \
             '/SkpSupport - информация об СКП,\n' \
             '/warning_bot - информация о ботах \n' \
             '/PsStates -- информация о платежных системах \n' \
             '/passport -- тестовый режим. Количество идентифицированных физлиц за день \n' \
             '@RoboHttpPingbot - робот от Вадима, который уведомляет, если что-то отвалилось\n' \
             '/kz - состояние по Казахстану'
