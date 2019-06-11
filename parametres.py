import requests

class Robowebsites(object):

    def __init__(self):
        self.color = 'blue'
        robomarket = requests.get('http://robo.market').status_code
        opg_robokassa = requests.get('http://opg.robokassa.ru').status_code
        partner_robokassa = requests.get('http://partner.robokassa.ru').status_code
        my_robokassa = requests.get('https://auth.robokassa.ru/my/Account/Login', auth=('amakarovskaya@robokassa.ru', 'Anitarat1')).status_code
        auth_robokassa = requests.get('http://auth.robokassa.ru/my').status_code
        admin_roboxchange = requests.get('https://admin.roboxchange.com/admin2/').status_code
        support_robokassa = requests.get('http://support.robokassa.ru/').status_code
        caravanru = requests.get('https://www.caravan.ru/').status_code
        self.p = [robomarket, opg_robokassa, partner_robokassa, my_robokassa, auth_robokassa, admin_roboxchange,
                   support_robokassa, caravanru]
        self.webname = ['robomarket', 'opg_robokassa', 'partner_robokassa', 'my_robokassa', 'auth_robokassa',
                   'admin_roboxchange',
                   'support_robokassa', 'caravanru']

    def info(self):

        counter = 0
        for i in range(len(self.p)):
            if self.p[i] == 200 or self.p[i] == 403:
                self.p[i] = '✅'
            else:
                self.p[i] = '❌'
                counter = 1
        if counter == 1:
            alarm = '\n \n 😱😱❗😱😱❗😱😱❗😱😱❗😱😱\n' + self.webname[i] + ' СЛОМАЛОСЬ\n 😱😱❗😱😱❗😱😱'
        else:
            alarm = ''
        self.robo_text = '1. robo.market:  %s\n' \
                    '2. opg.robokassa.ru: %s\n' \
                    '3. partner.robokassa.ru: %s\n' \
                    '4. my.robokassa.ru:  %s\n' \
                    '5. auth.robokassa.ru:  %s\n' \
                    '6. admin.roboxchange.ru: %s\n' \
                    '7. support.robokassa.ru: %s\n' \
                    '8. caravan.ru: %s' \
                    '%s' % (self.p[0], self.p[1], self.p[2], self.p[3], self.p[4], self.p[5], self.p[6], self.p[7], alarm)
        return self.robo_text