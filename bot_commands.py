import pytz
from datetime import datetime
import logging

from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from config import sts_chat, tr_knopka, kz_chat
from statistics.bots_statuses import bot_statuses
from statistics.rabbit_mq import rabbit_mq
from statistics.status_of_payment_systems import status_of_payment_systems, concise_status_of_payment_systems
from statistics.statistics import current_day_statistics, concise_statistics_of_the_day, paused_operations
from kazakhstan.kazakhstan import kazakhstan_operations_counter
from websites.website_status import websites_status
from queries.passports import number_of_passport_identifies
from support.support_info import support_data

MOSCOW_ZONE = "Europe/Moscow"
KZ_ZONE = "Asia/Almaty"
DOG_PIC = "https://s.tcdn.co/18f/4d5/18f4d57e-c910-3aef-9523-9a0d3bb60468/thumb128.png"
module_logger = logging.getLogger("bot_commands")

# -------------------------------------------------------------------------------------------
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


def start(bot, update):
    logger = logging.getLogger("bot_commands.start")
    update.message.reply_text(start_text)
    logger.info("Command /start is called")


def ourtime():
    local_format = "%Y-%m-%d %H:%M:%S"
    return datetime.now().astimezone(pytz.timezone(MOSCOW_ZONE)).strftime(local_format)


def print_skp(bot, update):
    logger = logging.getLogger("bot_commands.print_skp")
    update.message.reply_text(f"*Для клиентской поддержки на {ourtime()}*\n{support_data()}",
                              parse_mode=ParseMode.MARKDOWN)
    logger.info("Command /SkpSupport is called")


def sts_warning_support_info(bot, update):
    logger = logging.getLogger("bot_commands.sts_warning_support_info")
    bot.send_message(chat_id=sts_chat,
                     text=f"*Для клиентской поддержки на {ourtime()}*\n{support_data()}",
                     parse_mode=ParseMode.MARKDOWN)
    logger.info("Command /SkpSupport is called and printed to sts_chat")


def kazakhstan_30_min(bot, update):
    logger = logging.getLogger("bot_commands.kazakhstan_30_mins")
    dn = datetime.now()
    dn_kz = dn.astimezone(pytz.timezone(KZ_ZONE)).strftime('%H')
    if int(dn_kz) > 6:
        kazakhstan_operations_counter()
        if kazakhstan_operations_counter()[0] > 0:
            logger.info(f"Everything is ok {kazakhstan_operations_counter()[1]}")
        else:
            logger.critical(f"@Anton_Rokhlin No successful transactions in half an hour! "
                        f"The last is {kazakhstan_operations_counter()[1]}")
            bot.send_message(chat_id=kz_chat,
                             text=f"@Anton_Rokhlin Нет успешных операций за полчаса!")


def russia_paused_30_min(bot, update):
    dn = datetime.now()
    dn_msk = dn.astimezone(pytz.timezone(MOSCOW_ZONE)).strftime('%H')
    if 23 > int(dn_msk) > 8:
        paused = paused_operations()
        if int(paused) > 0:
            bot.send_message(chat_id=sts_chat,
                             text=f"Приостановленные операции, пацаны! {paused} штук")


def kazakhstan_count_operations(bot, update):
    logger = logging.getLogger("bot_commands.kazakhstan_count_operations")
    if kazakhstan_operations_counter()[0] < 1:
        logger.info(f"Counter = {kazakhstan_operations_counter()[0]}")
        logger.critical(f"No successful transactions in half an hour! The last {kazakhstan_operations_counter()[1]}")
        update.message.reply_text(f"Нет успешных операций за полчаса!")
    else:
        logger.info(f"Everything is OK, {kazakhstan_operations_counter()[0]} payments: "
                    f" {kazakhstan_operations_counter()[1]}")
        update.message.reply_text(f"Все хорошо, {kazakhstan_operations_counter()[0]} операций по оплате: "
                                  f" {kazakhstan_operations_counter()[1]}")


def print_day_statistics(bot, update):
    logger = logging.getLogger("bot_commands.print_day_statistics")
    logger.info("Command /operations is called")
    update.message.reply_text(current_day_statistics())


def print_concise_statistics_of_the_day(bot, update):
    # logger.info(concise_statistics_of_the_day())
    update.message.reply_text(concise_statistics_of_the_day())


def print_bots_statuses(bot, update):
    logger = logging.getLogger("bot_commands.print_bots_statuses")
    logger.info("Command /warning_bot is called")
    update.message.reply_text(f'   Состояние ботов:\n{bot_statuses()}')


def print_payment_systems_info(bot, update):
    logger = logging.getLogger("bot_commands.print_payment_systems_info")
    logger.info("Command /PsStates is called")
    update.message.reply_text(status_of_payment_systems())


def print_websites_status(bot, update):
    logger = logging.getLogger("bot_commands.print_websites_status")
    update.message.reply_text(f'Проверка сайтов: на {ourtime()}: \n{websites_status()}')


def print_passports_identify(bot, update):
    logger = logging.getLogger("bot_commands.print_passports_identify")
    logger.info("Command /passports is called")
    update.message.reply_text(number_of_passport_identifies())


# -- Прописываем контрольные точки
def print_control_points(bot, update):
    logger = logging.getLogger("bot_commands.print_control_points")
    logger.info("Command /sys_check_param is called")
    update.message.reply_text(f"*Cписок контрольных параметров системы* {ourtime()}: \n"
                              f"`{current_day_statistics()}` \n"
                              f"*Состояние платежных систем*: \n`{status_of_payment_systems()}`\n"
                              f"*Состояние очередей*: \n`abbitMq: {rabbit_mq()}`\n"
                              f"*Состояние роботов* \n`{bot_statuses()}`",
                              parse_mode=ParseMode.MARKDOWN)


def send_sts_bot_states(bot, update):
    logger = logging.getLogger("bot_commands.send_sts_bot_states")
    logger.info("Command /stsbotsstate is called")
    bot.send_message(chat_id=sts_chat,
                     text=f'   Состояние ботов:\n{bot_statuses()}')


def send_sts_control_points(bot, update):
    logger = logging.getLogger("bot_commands.send_sts_control_points")
    bot.send_message(chat_id=sts_chat,
                     text=f"*Cписок контрольных параметров системы {ourtime()}*: \n\n"
                     f"{current_day_statistics()} \n"
                     f"*Состояние платежных систем*: \n{status_of_payment_systems()}\n"
                     f"*RabbitMq*: {rabbit_mq()}\n"
                     f"*Состояние роботов* {bot_statuses()}")


def send_sts_control_points_and_webs(bot, update):
    bot.send_message(chat_id=sts_chat,
                     text=(f"*Cписок контрольных параметров системы на {ourtime()}*: \n"
                           f"{concise_statistics_of_the_day()}"
                           f"*Состояние платежных систем*: \n{concise_status_of_payment_systems()}\n"
                           f"*RabbitMq*: {rabbit_mq()}\n"
                           f"*Состояние роботов* {bot_statuses()}"),
                     parse_mode=ParseMode.MARKDOWN)
    bot.send_message(chat_id=sts_chat,
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
    bs = bot_statuses()
    ps = status_of_payment_systems()
    keyword = ['не работает', 'отключена']
    for key in keyword:
        if key in ps:
            bot.send_message(chat_id=sts_chat,
                             text=f"Состояние ботов:\n{bot_statuses()}")
            bot.send_photo(chat_id=sts_chat, photo=DOG_PIC)
        if key in bs:
            bot.send_message(chat_id=sts_chat,
                             text=status_of_payment_systems())
            bot.send_photo(chat_id=sts_chat, photo=DOG_PIC)


def test(bot, update):
    # просто команда-пасхалка, когда хочется видеть пса в горящей избе
    user_text = bot.send_photo(chat_id=update.message.chat_id, photo=DOG_PIC)
    # update.effective_message.reply_text("Hola tester! _I_ *have* `markdown`", parse_mode=ParseMode.MARKDOWN)
