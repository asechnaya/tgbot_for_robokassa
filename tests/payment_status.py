def payment_state(*text):
    payment_text = '{} : {}'.format(*text)
    return payment_text

mylist = ['Mixplat :  частично работает', 'MobileWallet :  работает', 'AlfaBank :  работает', 'PaySendBank :  работает']

def payment_state_check(text):
    check_text = 'OK'
    for item in text:
        if item == 'работает':
            check_text.join('но '+item)
        else:
            pass
    return check_text

print(mylist.count('Mixplat :  частично работает'))
print(mylist.index('PaySendBank :  работает'))

payment_state_check(mylist)

