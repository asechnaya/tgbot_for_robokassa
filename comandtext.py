import pytz
from datetime import datetime

from weblist import websites
from all_operations import operation_text, web_info, allPSState_text, PSState_text
from all_operations import RabbitMq_status, BotStateStatus, allBotStateStatus, inv_passfizident, inv_skp

timezones = 'Europe/Moscow'
localFormat = "%Y-%m-%d %H:%M:%S"

def ourtime():
    return datetime.now().astimezone(pytz.timezone(timezones)).strftime(localFormat)

def inv_check_param():
    return 'Cписок контрольных параметров системы {}: \n\n{}' \
           '8. Состояние платежных систем: \n{}' \
           '9. RabbitMq: {}\n' \
           '10. Состояние роботов {}'.format(ourtime(),
                                             operation_text(),
                                             PSState_text(),
                                             RabbitMq_status(),
                                             BotStateStatus())

def inv_PState_text():
    return 'Состояние платежных систем: \n{}'.format(allPSState_text())

def inv_webstatus():
    return 'Проверка сайтов: на {}: \n{}'.format(ourtime(), web_info(websites))

def inv_all_about_bot():
    return 'Состояние ботов:\n{}'.format(allBotStateStatus())

def SkpSupport_info():
    return 'Для клиентской поддержки {}:\n{}'.format(ourtime(), inv_skp())

def passportfiz_ident():
    return inv_passfizident()


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
            '/SkpSupport - че-т там для СКП'
