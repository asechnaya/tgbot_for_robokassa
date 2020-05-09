import requests

websites = {
'robokassa.ru': 'https://robokassa.ru',
'robo.market': 'http://robo.market',
'opg.robokassa.ru': 'https://opg.robokassa.ru',
'partner.robokassa.ru':'https://partner.robokassa.ru',
'my.robokassa.ru': 'https://my.robokassa.ru',
'auth.robokassa.ru/my': 'http://auth.robokassa.ru/my',
'admin.roboxchange.com/admin2/': 'https://admin.roboxchange.com/admin2/',
'support.robokassa.ru': 'https://support.robokassa.ru/',
'caravan.ru': 'https://www.caravan.ru/'}


def websites_status():
    status = {}
    for key, value in websites.items():
        try:
            r = requests.get(url=value, verify=False).status_code
            if r == 200 or r == 403:
                status[key] = 'OK ✅'
            else:
                status[key] = {r: '😱😱❗😱😱❗😱😱 СЛОМАЛОСЬ\n 😱😱❗😱😱❗😱😱'}
        except EnvironmentError as e:
            status[key] = {e: '😱😱❗😱😱❗😱😱'}
    status = ' '.join([f'{key}: {value}\n' for key, value in status.items()])
    return status
