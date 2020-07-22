import logging
from datetime import time as timer

from telegram.ext import Updater, CommandHandler

from config import botpath, BOTTOKEN
from bot_commands import print_payment_systems_info, print_websites_status
from bot_commands import send_sts_bot_states, send_sts_control_points_and_webs, send_sts_control_points
from bot_commands import control_points_timer, check_bs_and_ps_every_300s, kazakhstan_count_operations
from bot_commands import print_passports_identify, print_control_points, print_skp, sts_warning_support_info
from bot_commands import start, kazakhstan_30_min, print_day_statistics, print_bots_statuses, russia_paused_30_min
from bot_commands import test

# Логгирование
# FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
FORMAT = '%(asctime)-15s %(name)s - %(levelname)s - %(message)s '
logging.basicConfig(format=FORMAT,
                    datefmt='%m-%d %H:%M',
                    level=logging.INFO,
                    filename=botpath
                    )

logger = logging.getLogger('main_application')


def main():
    logger.info('Bot has launched')
    updater = Updater(BOTTOKEN) #Ранее: , request_kwargs=REQUEST_KWARGS)
    dp = updater.dispatcher  # принимает входящие сообщения и посылает их куда-то
    # инструкция
    dp.add_handler(CommandHandler("start", start))
    # Запускаем так, чтобы каждые 6 часов робот писал в чатик
    updater.job_queue.run_daily(control_points_timer, time=timer(9, 1, 17))
    updater.job_queue.run_daily(control_points_timer, time=timer(21, 1, 17))
    updater.job_queue.run_repeating(check_bs_and_ps_every_300s, interval=300, first=0)
    updater.job_queue.run_repeating(kazakhstan_30_min, interval=1800, first=0)
    updater.job_queue.run_repeating(russia_paused_30_min, interval=1800, first=0)
    # Команды для общего чатика СТС
    # -------------------------
    dp.add_handler(CommandHandler("allstat_sts", send_sts_control_points))  # '-1001102275465' - STS,
    dp.add_handler(CommandHandler("warning_all", send_sts_control_points_and_webs))  # '-1001102275465' - STS,
    dp.add_handler(CommandHandler("stsbotsstate", send_sts_bot_states))  # '-1001102275465' - STS,
    dp.add_handler(CommandHandler("SkpSupport_sts", sts_warning_support_info))  # '-1001102275465' - STS,
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

    dp.add_handler(CommandHandler("SkpSupport", print_skp))
    dp.add_handler(CommandHandler("kz", kazakhstan_count_operations))

    updater.start_polling()  # отправь эти данные платформе телеграм
    updater.idle()  # Жди, пока тебе телеграм что-то пришлет


if __name__ == '__main__':
    logger.info('Start point')
    main()

