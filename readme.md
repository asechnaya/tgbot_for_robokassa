В файл _config.py_ вписываем 

<span style="color:purple">
pfx_path = 'название.pfx'<br> 
pfx_password = 'кодовое слово из цифр'<br> 
botpath = 'bot.log'<br> 
certpath = 'temp/cert.pem'<br> 
dire ="temp/"<br> 
payload = {
   куки
}

</span>

---

Для запуска бота: _robotelebot.py_

--- 

##### В результате bot отправит сообщение вида

```
Cписок контрольных параметров системы: на 2019-06-11 18:32:25.845809: 
1. Исполнено операций: 31114  
2. Начато и незавершено операций: 6451  
3. Остановлено по техническим причинам: 61  
4. Приостановлено операций: 0  
5. Не прошло скоринг: 262  
6. Ошибки фискал-ии по Робочекам: 2  
7. Ошибки фискал-ии по доходам БЭ: 7
8. Состояние платежных систем:
    Mixplat :  частично работает 
    MobileWallet :  работает 
    AlfaBank :  работает 
    PaySendBank :  работает
9. RabbitMq Статус:  ok  
10. Состояние роботов ОК, но Сервис учетной системы:  работает😢
```

