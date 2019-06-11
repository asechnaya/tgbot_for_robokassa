# -- coding: utf-8 -*-

class OperationSts(object):

    def __init__(self, o):
        self.o = o
        del o[6:8]
        del o[8:16]
        del o[10:14]

    def info(self):
        i = 1
        k = 1
        self.op = list()
        self.stat = list()
        for item in self.o:
            if i%2 == 0:
                self.stat.append(item)
            else:
                item = (str(k)) +'. ' + item +':'
                self.op.append(item)
                k +=1
            i += 1

        self.oper_info = '%s %s\n' \
                         '%s %s\n' \
                         '%s %s\n' \
                         '%s %s\n' \
                         '%s %s\n' \
                         '%s %s\n' \
                         '%s %s\n' % (self.op[0], self.stat[0], self.op[1], self.stat[1], self.op[2], self.stat[2], self.op[3],
                                      self.stat[3], self.op[4], self.stat[4], self.op[5],   self.stat[5], self.op[6], self.stat[6])
        return self.oper_info

class BotSts(object):

    def __init__(self, o):
        self.o = o

    def info(self):
        i = 1
        k = 1
        self.op = list()
        self.stat = list()
        for item in self.o:
            if i%2 == 0:
                self.stat.append(item)
            else:
                item = (str(k)) +'. ' + item +':'
                self.op.append(item)
                k +=1
            i += 1

        self.oper_info = '%s %s\n' \
                         '%s %s\n' \
                         '%s %s\n' \
                         '%s %s\n' \
                         '%s %s\n' \
                         '%s %s\n' \
                         '%s %s\n' % (self.op[0], self.stat[0], self.op[1], self.stat[1], self.op[2], self.stat[2], self.op[3],
                                      self.stat[3], self.op[4], self.stat[4], self.op[5],   self.stat[5], self.op[6], self.stat[6])
        return self.oper_info
