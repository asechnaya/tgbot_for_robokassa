В файл _config.py_ вписываем 

<span style="color:purple">
pfx_path = 'название.pfx'<br> 
pfx_password = 'кодовое слово из цифр'<br> 
botpath = 'bot.log'<br> 
cert = 'temp/cert.pem'<br> 
dire ="temp/"<br> 
payload = {
   куки
}


REQUEST_KWARGS = {
    'proxy_url': 'socks5h://наш адрес:9999',
    'urllib3_proxy_kwargs': {
        'username': 'telega',
        'password': 'telega_pass',
    }
}
</span>



В файл _sypport/payload.py_ вписываем 
payload = {
   авторизация
}

---

Для запуска бота: _python3 robotelebot.py_

--- 

##### В результате bot отправит сообщение вида

```
merchwebcheck_bot, [04.07.19 15:00]
Cписок контрольных параметров системы: на 04.07.2019 15:07:55 (UTC): 

1. Исполнено операций: 21693
2. Начато и незавершено операций: 6492
3. Остановлено по техническим причинам: 9
4. Приостановлено операций: 4
5. Не прошло скоринг: 238
6. Ошибки фискал-ии по Робочекам: 13
7. Ошибки фискал-ии по доходам БЭ: 7
8. Состояние платежных систем: 
AlfaBank частично работает💤🔵
Mixplat частично работает💤🔵
9. RabbitMq: ОК ✅
10. Состояние роботов Сервис iRobo: не работает🛑
```
##Для создания Service

```
[Unit]
Description=robobot service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 cdrobotelebot.py
Restart=always

[Install]
WantedBy=multi-user.target

[Unit]
Description=MyTelegramBot
After=multi-user.target

[Service]
User = user
Type=idle
WorkingDirectory=/home/user/robobot/
ExecStart=/usr/bin/python3.6 -u robotelebot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Для запуска

sudo systemctl daemon-reload

sudo systemctl enable ROBOBOT.service

sudo systemctl start ROBOBOT.service
