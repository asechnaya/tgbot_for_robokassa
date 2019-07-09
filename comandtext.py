import time
from weblist import websites
from all_operations import operation_text, \
    web_info, allPSState_text, PSState_text, \
    RabbitMq_status, BotStateStatus, allBotStateStatus, inv_passfizident, inv_skp

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
    return 'Проверка сайтов: на {}: \n{}'.format(time.strftime("%d.%m.%Y %H:%m:%S"), web_info(websites))

def inv_all_about_bot():
    return 'Состояние ботов:\n{}'.format(allBotStateStatus())

def SkpSupport_info():
    return 'Для клиентской поддержки {}:\n{}'.format(time.strftime("%d.%m.%Y %H:%m:%S"), inv_skp())

def passportfiz_ident():
    return inv_passfizident()


start_text ='У нас есть:\n /start - список того, что ты можешь. \n ' \
            'warning - отправка чатик ТРЕВОЖНОЙ КНОПКИ инфы о состоянии операций и сайтов, (набирать / перед ворнингом, слеша нет в целях безопасности) \n' \
            '/stsbotsstate - отправка в чатик СТС инфы по всем ботам, \n ' \
            '/allstat_sts отправка всей инфы в СТС\n' \
            '/sys_check_param - все про все, \n' \
            '/webstatus - информация о сайтах, \n ' \
            '/operation - информация об операциях,\n' \
            '/warning_bot - информация о ботах \n' \
            '/PsStates -- информация о платежных системах \n' \
            '/test -- тестовый режим. Количество идентифицированных физлиц за день \n' \
            '@RoboHttpPingbot - робот от Вадима, который уведомляет, если что-то отвалилось\n' \
            '/SkpSupport - че-т там для СКП'
