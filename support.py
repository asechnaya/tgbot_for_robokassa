class SkpSupport(object):

    def __init__(self, ddd):
        del ddd[0:7]
        del ddd[19:11:-1]
        del ddd[1::2]

        self.numbers = []
        for item in range(len(ddd)):
            newitem = ddd[item].split('**')
            del newitem[-1]
            for i in range(len(newitem)):
                self.numbers.append(newitem[i])
        del self.numbers[0::2]

    def info(self):
        self.section = 'VIP: {}\n'\
                    'Вопросы по платежам: {}\n'\
                    'Входящие: {}\n'\
                    'СПАМ: {}\n'\
                    'MARKET: {}\n'\
                    'Мошенничество/Жалобы: {}\n'\
                    'ROBOKASSA: {}\n'\
                    'Партнеры: {}\n'\
                    'Предпродажи: {}\n'\
                    'Предложения по улучшению: {}' .format(*self.numbers)
        return(self.section)
