operations_f = """
<div class="row">
	<div class="col-lg-12 text-center">
		<h4>Статистика текущего дня <small>(<a data-ajax="true" data-ajax-begin="face.onBegin(&#39;StatisticsWait&#39;, &#39;StatisticsData&#39;)" data-ajax-method="Post" data-ajax-mode="replace" data-ajax-update="#Statistics" href="/admin2/Face/Statistics">обновить</a>)</small></h4>
	</div>
</div>
<div id="StatisticsWait" class="row hidden">
	<div class="col-lg-12">
		<table class="table-striped col-lg-12">
			<tr>
				<td class="c text-primary">Обновление...</td>
			</tr>
		</table>
	</div>
</div>
<div id="StatisticsData" class="row show">
		<div class="col-lg-12">
			<table class="table-striped col-lg-12">
				<tr class="active">
					<td class="l nw">
						<a href="/admin2/Operations?SpecialOpFilter=Finished" class="light" target="_blank">Исполнено операций</a>
					</td>
					<td class="r b text-success">33422</td>
				</tr>
				<tr>
					<td class="l nw">Начато и незавершено операций</td>
					<td class="r b text-primary">6320</td>
				</tr>
				<tr class="active">
					<td class="l nw">
						<a href="/admin2/Operations?SpecialOpFilter=Paused" class="light" target="_blank">Остановлено по техническим причинам</a>
					</td>
					<td class="r b text-red">87</td>
				</tr>
				<tr>
					<td class="l nw">
						<a href="/admin2/Operations?SpecialOpFilter=Duplicated" class="light" target="_blank">Повторных оплат</a>
					</td>
					<td class="r b text-darkred">5011</td>
				</tr>
				<tr class="active">
					<td class="l nw">
						<a href="/admin2/Operations?SpecialOpFilter=Hold" class="light" target="_blank">Приостановлено операций</a>
					</td>
					<td class="r b text-orange">0</td>
				</tr>
				<tr>
					<td class="l nw">Заблокировано операций</td>
					<td class="r b text-darkred">258</td>
				</tr>
				<tr class="active">
					<td class="l nw">Отложено операций</td>
					<td class="r b text-brown">0</td>
				</tr>
				<tr>
					<td class="l nw">Всего заявок подавалось</td>
					<td class="r b">41789</td>
				</tr>
				<tr class="active">
					<td class="l nw">Отменено роботом</td>
					<td class="r b">8317</td>
				</tr>
				<tr>
					<td class="l nw">
						<a href="/admin2/Operations?SpecialOpFilter=Scoring" class="light" target="_blank">Не прошло скоринг</a>
					</td>
					<td class="r b">288</td>
				</tr>
				<tr class="active">
					<td class="l nw">Завершено операций предыдущего дня</td>
					<td class="r b">31464</td>
				</tr>
			    <tr>
			        <td class="l nw">Отправлено сообщений в поддержку</td>
			        <td class="r b">42</td>
			    </tr>
			    <tr class="active">
                    <td class="l nw">Ошибки фискал-ии по Робочекам</td>
					<td class="r b">1258</td>
				</tr>
			    <tr>
                    <td class="l nw">Ошибки фискал-ии по доходам БЭ</td>
					<td class="r b">7</td>
				</tr>
			</table>
		</div>
</div>
"""
botsstate_f = """

<div class="row">
	<div class="col-lg-12 text-center">
		<h4>Состояние роботов <small>(<a data-ajax="true" data-ajax-begin="face.onBegin(&#39;BotsStateWait&#39;, &#39;BotsStateData&#39;)" data-ajax-method="Post" data-ajax-mode="replace" data-ajax-update="#BotsState" href="/admin2/Face/BotsState">обновить</a>)</small></h4>
	</div>
</div>
<div id="BotsStateWait" class="row hidden">
	<div class="col-lg-12">
		<table class="table-striped col-lg-12">
			<tr>
				<td class="c text-primary">Обновление...</td>
			</tr>
		</table>
	</div>
</div>
<div id="BotsStateData" class="row show">
		<div class="col-lg-12">
			<table class="table-striped col-lg-12">
					<tr class="active">
						<td class="l col-lg-9">
							Автомат:
						</td>
						<td class="r nw col-lg-3">
							работает
						</td>
					</tr>
					<tr class="active">
						<td class="l col-lg-9">
							Сервис запуска ботов:
						</td>
						<td class="r nw col-lg-3">
							работает
						</td>
					</tr>
					<tr class="active">
						<td class="l col-lg-9">
							Сервис подтверждений OCEAN:
						</td>
						<td class="r nw col-lg-3">
							работает
						</td>
					</tr>
					<tr class="active">
						<td class="l col-lg-9">
							 - поток мониторинга:
						</td>
						<td class="r nw col-lg-3 text-lightgray">
							ожидает
						</td>
					</tr>
					<tr class="active">
						<td class="l col-lg-9">
							 - поток снятия блокировок:
						</td>
						<td class="r nw col-lg-3 text-lightgray">
							ожидает
						</td>
					</tr>
					<tr class="active">
						<td class="l col-lg-9">
							 - поток ошибок подтверждений:
						</td>
						<td class="r nw col-lg-3 text-lightgray">
							ожидает
						</td>
					</tr>
					<tr class="active">
						<td class="l col-lg-9">
							Сервис OpenStat RegisterNotificationsManager:
						</td>
						<td class="r nw col-lg-3 text-red">
							не работает
						</td>
					</tr>
					<tr class="active">
						<td class="l col-lg-9">
							Сервис OpenStat QueueTasksManager:
						</td>
						<td class="r nw col-lg-3 text-red">
							не работает
						</td>
					</tr>
					<tr class="active">
						<td class="l col-lg-9">
							Сервис iRobo:
						</td>
						<td class="r nw col-lg-3 text-red">
							работает
						</td>
					</tr>
					<tr class="active">
						<td class="l col-lg-9">
							Сервис учетной системы:
						</td>
						<td class="r nw col-lg-3">
							работает медленно
						</td>
					</tr>
			</table>
		</div>
</div>


"""
mobilewallet_f = """
<td class="r nw col-lg-1 text-success">75</td>
<td class="l nw col-lg-1 text-darkred">96</td>
<td class="l w col-lg-4">MobileWallet</td>
<td class="r w col-lg-5">
работает</td>
<td class="r nw col-lg-1">
<a data-ajax="true" data-ajax-begin="onBegin(&#39;CStatePsMobileWallet&#39;)" data-ajax-mode="replace" data-ajax-update="#CStatePsMobileWallet" href="/admin2/Face/PsCheck?PsLabel=MobileWallet">chk</a></td>
"""
mixplat_f = """
<td class="r nw col-lg-1 text-darkred">51</td>
<td class="l nw col-lg-1"></td>
<td class="l w col-lg-4">Mixplat</td>
<td class="r w col-lg-5 text-red">
частично работает</td>
<td class="r nw col-lg-1">
<a data-ajax="true" data-ajax-begin="onBegin(&#39;CStatePsMixplat&#39;)" data-ajax-mode="replace" data-ajax-update="#CStatePsMixplat" href="/admin2/Face/PsCheck?PsLabel=Mixplat">chk</a></td>

"""
alfabank_f = """
<td class="r nw col-lg-1 text-darkred">52</td>
<td class="l nw col-lg-1"></td>
<td class="l w col-lg-4">AlfaBank</td>
<td class="r w col-lg-5 text-red">
частично работает</td>
<td class="r nw col-lg-1">
<a data-ajax="true" data-ajax-begin="onBegin(&#39;CStatePsAlfaBank&#39;)" data-ajax-mode="replace" data-ajax-update="#CStatePsAlfaBank" href="/admin2/Face/PsCheck?PsLabel=AlfaBank">chk</a></td>
"""
RabbitMq_f = """
<div class="row">
	<div class="col-lg-12 text-center">
		<h4>Мониторинг RabbitMq <small>(<a data-ajax="true" data-ajax-begin="face.onBegin(&#39;RabbitMqMonitoringWait&#39;, &#39;RabbitMqMonitoringData&#39;)" data-ajax-method="Post" data-ajax-mode="replace" data-ajax-update="#RabbitMqMonitoring" href="/admin2/Face/RabbitMqMonitoring">обновить</a>)</small> </h4>
	</div>
</div>
<div id="RabbitMqMonitoringWait" class="row hidden">
	<div class="col-lg-12">
		<table class="table-striped col-lg-12">
			<tr>
				<td class="c text-primary">Обновление...</td>
			</tr>
		</table>
	</div>
</div>
   <div id="RabbitMqMonitoringData" class="row">
	<div class=" col-lg-12">
		<table class="table-striped col-lg-12">
			<tr>
				<td class="col-lg-9">
					Статус:
				</td>
				<td class="col-lg-3 text-right">
					ok
				</td>
			</tr>


		</table>
	</div>
 </div>




	<script type="text/javascript">
		function RabbitUpdate() {
			$.ajax({
				url: '/admin2/Face/RabbitMqMonitoring',
				success: function(data) {
					$("#RabbitMqMonitoring").html(data);
				}
			});
		}
			setTimeout(RabbitUpdate, 5000);
	</script>

"""


mainurl_f = """

<!DOCTYPE html>
<html >
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=EDGE" />
    <link rel="icon" type="image/png" href="/admin2/Content/images/favicon-96x96.png" />
    <title>Административная консоль ROBOKASSA</title>
    <link rel="stylesheet" type="text/css" href="/admin2/Content/font-awesome/css/fontawesome-all.css" />
    <script src="/admin2/scripts/modernizr?v=inCVuEFe6J4Q07A0AcRsbJic_UE5MwpRMNGcOtk94TE1"></script>

    
    <link href="/admin2/content/themes/base/jquery-ui?v=" rel="stylesheet"/>
<link href="/admin2/content/css?v=y-BsmjfXe4od7pcgi48mf5UTTy9VKW3r23HCc8xpJYc1" rel="stylesheet"/>


    <script src="/admin2/scripts/jquery?v=TO-weCkjoajLHXPpwTj4CDwGJI-Jy45UzXsBJYnzshw1"></script>
<script src="/admin2/scripts/moment?v=HJfC7ryO_9ZtWq8TogvV7Y_bhfFSpxx8MUtNO58ZoDY1"></script>
<script src="/admin2/scripts/bootstrap?v=ottYQyTAplh-cMt4DwcTxUjb5cdvwr11IeKuNt7psXE1"></script>
<script src="/admin2/scripts/globalization?v=3xsqHh0anm6_6qsza15PcDzdjNLV5OfZQQvSOEwwrdw1"></script>
<script src="/admin2/scripts/unobtrusive-ajax?v=OogFi3g5HLuGIHAgSqPk_6zluJg3HjxNAuUL0uNC8a81"></script>
<script src="/admin2/scripts/knockout?v=BuG8Nb-qvi4pJtBzzKqXnpD5TfnIvTgfbcmeRR0P1yw1"></script>

    <script type="text/javascript">
		$.fn.globalizeCldr(Globalize, { locale: "ru-RU", baseUrl: "/admin2/Scripts" });

		// Простейший обработчик ошибки Ajax-запроса.
		function OnAjaxFailure(xhr) { $('html').html(xhr.responseText); }
    </script>

    
	<script src="/admin2/Scripts/Face/PsCheck.js"></script>
<script src="/admin2/Scripts/Face/Refresh.js"></script>
<script src="/admin2/Scripts/Face/Notify.js"></script>


    <style>
        hr {
            margin-top: 0.5em;
            margin-bottom: 0.5em;
        }

        .container {
            min-width: 768px !important;
        }
    </style>
</head>
<body>
    
    <div class="modal-overlay" id="overlay-wait"></div>
    <div class="container-fluid">
        
        <div class="row header">
            <div class="col-lg-4">
                <a href="/admin2/">Администрирование</a>
                &bull;
                <a href="http://www.robokassa.ru" target="_blank">Робокасса</a>
            </div>
            <div class="col-lg-4 pull-right text-right b">
                Пользователь: <span class="pseudoA">Макаровская Анна</span> &bull; Дата: <span class="pseudoA">10.06.2019 15:27 UTC</span>
            </div>
        </div>
        <div class="row">
            
            <div class="col-lg-12">
                <hr />
<style type="text/css">
	div.navbar-inner ul {
		background-color: #f0f0f0;
		border: 1px solid silver;
	}

		div.navbar-inner ul li a {
			padding: 0.15em 0.5em 0.15em 0.5em;
			color: #0067A4;
			text-decoration: none;
			font-weight: bold;
		}

		div.navbar-inner ul.dropdown-menu li a {
			padding-left: 1.5em;
		}
</style>

<script type="text/javascript">
	$(document).ready(function () {
		$('.nav li.dropdown').hover(
			function () {
				$(this).addClass('open');
			}, function () {
				$(this).removeClass('open');
			});
	});
</script>
<div class="row">
	<div class="col-lg-12">
		<nav>
			<div class="navbar-inner">
				<ul class="nav navbar-nav">
						<li class="dropdown">
							<a class="dropdown-toggle" data-toggle="dropdown" href="" target="_self">Операции</a>
							<ul class="dropdown-menu">
									<li>
										<a href="/admin2/Operations?SpecialOpFilter=Paused" target="_self">«Зависшие» операции</a> 
									</li>
									<li>
										<a href="/admin2/Operations?SpecialOpFilter=InProgress" target="_self">Незаконченные операции</a> 
									</li>
									<li>
										<a href="/admin2/Operations?SpecialOpFilter=Finished" target="_self">Законченные операции</a> 
									</li>
									<li>
										<a href="/admin2/Operations?SpecialOpFilter=Refund" target="_self">Операции требующие возврата</a> 
									</li>
									<li>
										<a href="/admin2/Operations?SpecialOpFilter=Blocked" target="_self">Блокированные операции</a> 
									</li>
									<li>
										<a href="/admin2/Operations" target="_self">Найти операции</a> 
									</li>
									<li>
										<a href="/admin2/Op/MicroPayment.aspx" target="_self">Авторизации карт</a> 
									</li>
									<li>
										<a href="/admin2/Operations?SpecialOpFilter=Duplicated" target="_self">Повторные оплаты счетов</a> 
									</li>
									<li>
										<a href="/admin2/External/Terminals/Search.aspx" target="_self">Терминалы. Поиск оплаты</a> 
									</li>
							</ul>
						</li>
						<li class="dropdown">
							<a class="dropdown-toggle" data-toggle="dropdown" href="" target="_self">Массовые выплаты</a>
							<ul class="dropdown-menu">
									<li>
										<a href="/admin2/MassPayments/MassPayment" target="_self">Найти выплату</a> 
									</li>
							</ul>
						</li>
						<li class="dropdown">
							<a class="dropdown-toggle" data-toggle="dropdown" href="" target="_self">Пост-процессинг</a>
							<ul class="dropdown-menu">
									<li>
										<a href="/admin2/Postprocess/Failed" target="_self">Неуспешные - фискализация</a> 
									</li>
							</ul>
						</li>
						<li class="dropdown">
							<a class="dropdown-toggle" data-toggle="dropdown" href="" target="_self">Партнёры</a>
							<ul class="dropdown-menu">
									<li>
										<a href="/admin2/Cabinet/Clients" target="_self">Клиенты сервиса ROBOKASSA</a> 
									</li>
									<li>
										<a href="/admin2/Payments/MerchantOff" target="_self">Мерчанты Off-line. Платежи</a> 
									</li>
									<li>
										<a href="/admin2/Partners/LoyaltyRequests.aspx" target="_self">Программа лояльности</a> 
									</li>
							</ul>
						</li>
						<li class="dropdown">
							<a class="dropdown-toggle" data-toggle="dropdown" href="" target="_self">Отчёты и статистика</a>
							<ul class="dropdown-menu">
									<li>
										<a href="/admin2/Balance/Balance.aspx" target="_self">Расчет баланса ROBOX</a> 
									</li>
									<li>
										<a href="/admin2/Reports/ReportViewer/ReportList.aspx" target="_self">Отчеты</a> 
									</li>
							</ul>
						</li>
						<li class="dropdown">
							<a class="dropdown-toggle" data-toggle="dropdown" href="" target="_self">Карточный процессинг</a>
							<ul class="dropdown-menu">
									<li>
										<a href="/admin2/CardProcessing/Live" target="_self">Live</a> 
									</li>
									<li>
										<a href="/admin2/CardProcessing/Graph" target="_self">Графики</a> 
									</li>
									<li>
										<a href="/admin2/CardProcessing/GraphDays" target="_self">Графики (за сегодня)</a> 
									</li>
									<li>
										<a href="/admin2/CardProcessing/" target="_self">Жизнь шлюза</a> 
									</li>
									<li>
										<a href="/admin2/CardProcessing/Terminals" target="_self">Терминалы</a> 
									</li>
									<li>
										<a href="/admin2/CardProcessing/DeadTerminals" target="_self">Терминалы зомби (или есть ли жизнь после смерти)</a> 
									</li>
									<li>
										<a href="/admin2/CardProcessing/TerminalStat" target="_self">Терминалы Статистика</a> 
									</li>
									<li>
										<a href="/admin2/CardProcessing/Search" target="_self">Поиск операций</a> 
									</li>
									<li>
										<a href="/admin2/CardProcessing/BankReiting" target="_self">Народный рейтинг банков</a> 
									</li>
							</ul>
						</li>
						<li class="dropdown">
							<a class="dropdown-toggle" data-toggle="dropdown" href="" target="_self">Расчётные банки</a>
							<ul class="dropdown-menu">
									<li>
										<a href="/admin2/Payments/MerchantBN" target="_self">Платежи</a> 
									</li>
									<li>
										<a href="/admin2/Partners/RefundRequests_RIB.aspx" target="_self">Возвраты</a> 
									</li>
							</ul>
						</li>
						<li class="dropdown">
							<a class="dropdown-toggle" data-toggle="dropdown" href="" target="_self">Инфо</a>
							<ul class="dropdown-menu">
									<li>
										<a href="/InfoPanel" target="_self">Информационная панель</a> 
									</li>
							</ul>
						</li>
						<li class="dropdown">
							<a class="dropdown-toggle" data-toggle="dropdown" href="" target="_self">Безопасность</a>
							<ul class="dropdown-menu">
									<li>
										<a href="/admin2/BlackList/List.aspx" target="_self">Черный список</a> 
									</li>
							</ul>
						</li>
						<li class="dropdown">
							<a class="dropdown-toggle" data-toggle="dropdown" href="" target="_self">Заявки</a>
							<ul class="dropdown-menu">
									<li>
										<a href="/admin2/ClientRequests/List" target="_self">Заявки-2.0</a> 
									</li>
							</ul>
						</li>
						<li class="dropdown">
							<a class="dropdown-toggle" data-toggle="dropdown" href="" target="_self">ЛКФ</a>
							<ul class="dropdown-menu">
									<li>
										<a href="/admin2/Personal/" target="_self">Пользователи</a> 
									</li>
							</ul>
						</li>
						<li class="dropdown">
							<a class="dropdown-toggle" data-toggle="dropdown" href="" target="_self">OpenStat</a>
							<ul class="dropdown-menu">
									<li>
										<a href="/admin2/OpenStat/Dashboard" target="_self">Графики</a> 
									</li>
									<li>
										<a href="/admin2/OpenStat/Register" target="_self">Журнал мониторинга</a> 
									</li>
									<li>
										<a href="/admin2/OpenStat/PriorityMonitoring" target="_self">Статистика приоритетного мониторинга</a> 
									</li>
									<li>
										<a href="/admin2/OpenStat/BlackList" target="_self">Черный список</a> 
									</li>
									<li>
										<a href="/admin2/OpenStat/WhiteList" target="_self">Белый список</a> 
									</li>
							</ul>
						</li>
				</ul>
			</div>
		</nav>
	</div>
</div>
                <hr />
            </div>
        </div>
        <div class="row">
            
            <div class="col-lg-12">
                <div id="alertMessage"></div>
                

<form id="notify-sms-form" class="form-horizontal" role="form" title="Ох, как же так...">
	<p>Беда беда!!! Уведомить авторов по СМС?</p>
	<p><img id="sms-notify-img" src="/admin2/Content/images/iisusi.jpg" hidden="hidden"/></p>
</form>
<div class="row">
	<div class="col-lg-4">
		<div class="row">
			<div class="col-lg-12" id="Warnings">
				
				


	<script type="text/javascript">
		$.ajax({
			url: '/admin2/Face/Warnings',
			success: function (data) {
				$("#Warnings").html(data);
			}
		})
	</script>

			</div>
		</div>
		<div class="row">
			<div class="col-lg-12" id="RatesState">
				
				

<div class="row">
	<div class="col-lg-12 text-center">
		<h4>Состояние курсов <small>(<a data-ajax="true" data-ajax-begin="face.onBegin(&#39;RatesStateWait&#39;, &#39;RatesStateData&#39;)" data-ajax-method="Post" data-ajax-mode="replace" data-ajax-update="#RatesState" href="/admin2/Face/RatesState">обновить</a>)</small></h4>
	</div>
</div>
<div id="RatesStateWait" class="row show">
	<div class="col-lg-12">
		<table class="table-striped col-lg-12">
			<tr>
				<td class="c text-primary">Обновление...</td>
			</tr>
		</table>
	</div>
</div>
<div id="RatesStateData" class="row hidden">
	<div class=" col-lg-12">
		<table class="table-striped col-lg-12">
			<tr>
				<td class="col-lg-9">
					Базовые курсы обновлялись:
				</td>
				<td class="nw col-lg-3">
					 UTC
				</td>
			</tr>
		</table>
	</div>
</div>

	<script type="text/javascript">
		$.ajax({
			url: '/admin2/Face/RatesState',
			success: function (data) {
				$("#RatesState").html(data);
			}
		})
	</script>

			</div>
		</div>
		<div class="row">
			<div class="col-lg-12" id="BotsState">
				
				


<div class="row">
	<div class="col-lg-12 text-center">
		<h4>Состояние роботов <small>(<a data-ajax="true" data-ajax-begin="face.onBegin(&#39;BotsStateWait&#39;, &#39;BotsStateData&#39;)" data-ajax-method="Post" data-ajax-mode="replace" data-ajax-update="#BotsState" href="/admin2/Face/BotsState">обновить</a>)</small></h4>
	</div>
</div>
<div id="BotsStateWait" class="row show">
	<div class="col-lg-12">
		<table class="table-striped col-lg-12">
			<tr>
				<td class="c text-primary">Обновление...</td>
			</tr>
		</table>
	</div>
</div>
<div id="BotsStateData" class="row hidden">
</div>

	<script type="text/javascript">
		$.ajax({
			url: '/admin2/Face/BotsState',
			success: function (data) {
				$("#BotsState").html(data);
			}
		})
	</script>

			</div>
		</div>
		<div class="row">
			<div class="col-lg-12" id="PersonalQueueStates">
				
				


<div class="row">
	<div class="col-lg-12 text-center">
		<h4>Состояние очередей ЛКФ <small>(<a data-ajax="true" data-ajax-begin="face.onBegin(&#39;PersonalQueueStatesWait&#39;, &#39;PersonalQueueStatesData&#39;)" data-ajax-method="Post" data-ajax-mode="replace" data-ajax-update="#PersonalQueueStates" href="/admin2/Face/PersonalQueueStates">обновить</a>)</small></h4>
	</div>
</div>
<div id="PersonalQueueStatesWait" class="row show">
	<div class="col-lg-12">
		<table class="table-striped col-lg-12">
			<tr>
				<td class="c text-primary">Обновление...</td>
			</tr>
		</table>
	</div>
</div>
<div id="PersonalQueueStatesData" class="row hidden">
</div>

	<script type="text/javascript">
		$.ajax({
			url: '/admin2/Face/PersonalQueueStates',
			success: function (data) {
				$("#PersonalQueueStates").html(data);
			}
		})
	</script>

			</div>
		</div>
		<div class="row">
			<div class="col-lg-12" id="RabbitMqMonitoring">
				
				
<div class="row">
	<div class="col-lg-12 text-center">
		<h4>Мониторинг RabbitMq <small>(<a data-ajax="true" data-ajax-begin="face.onBegin(&#39;RabbitMqMonitoringWait&#39;, &#39;RabbitMqMonitoringData&#39;)" data-ajax-method="Post" data-ajax-mode="replace" data-ajax-update="#RabbitMqMonitoring" href="/admin2/Face/RabbitMqMonitoring">обновить</a>)</small> </h4>
	</div>
</div>
<div id="RabbitMqMonitoringWait" class="row show">
	<div class="col-lg-12">
		<table class="table-striped col-lg-12">
			<tr>
				<td class="c text-primary">Обновление...</td>
			</tr>
		</table>
	</div>
</div>




	<script type="text/javascript">
		function RabbitUpdate() {
			$.ajax({
				url: '/admin2/Face/RabbitMqMonitoring',
				success: function(data) {
					$("#RabbitMqMonitoring").html(data);
				}
			});
		}
			RabbitUpdate();
	</script>



			</div>
		</div>
		<div class="row">
			<div class="col-lg-12" id="Uptimes">
				
				<div class="row">
    <div class="col-lg-12 text-center">
        <h4>Мониторинг доступности сайтов</h4>
    </div>
</div>
<div class="row">
    <div class=" col-lg-12">
        <table class="table-striped col-lg-12">
            <tr class="active">
                <td class="col-lg-9">Касса</td>
                <td class="col-lg-3 text-right">
                    <a href="https://www.host-tracker.com/UptimeGraph/UptimeInfo/a0ce6272-0f65-4f92-b914-5274d3fe803c" rel="nofollow" target="_blank">
                        <img id='HostTrackerInformer' style="border: 0" alt="" src="//i.h-t.co/trace.png?id=4694b89c-59e6-4789-9d6a-63a1171e4b0c" />
                    </a>
                </td>
            </tr>
            <tr class="active">
                <td class="col-lg-9">Web-сервис</td>
                <td class="col-lg-3 text-right">
                    <a href="https://www.host-tracker.com/UptimeGraph/UptimeInfo/1b6e6152-a67a-405a-b45a-10207304d601" rel="nofollow" target="_blank">
                        <img id='HostTrackerInformer' style="border: 0" alt="" src="//i.h-t.co/trace.png?id=1b6e6152-a67a-405a-b45a-10207304d601" />
                    </a>
                </td>
            </tr>
            <tr class="active">
                <td class="col-lg-9">opg.robokassa.ru</td>
                <td class="col-lg-3 text-right">
                    <a href="https://www.host-tracker.com/UptimeGraph/UptimeInfo/efb9f591-3aac-4353-ade1-9a8c0e20cb6a" rel="nofollow" target="_blank">
                        <img id='HostTrackerInformer' style="border: 0" alt="" src="//i.h-t.co/monitoring.png?id=efb9f591-3aac-4353-ade1-9a8c0e20cb6a" />
                    </a>
                </td>
            </tr>
            <tr class="active">
                <td class="col-lg-9">partner.robokassa.ru</td>
                <td class="col-lg-3 text-right">
                    <a href="https://www.host-tracker.com/UptimeGraph/UptimeInfo/6b496921-42a5-48d8-bb44-2b3c73b71f29" rel="nofollow" target="_blank">
                        <img style="border: 0" alt="" src="//i.h-t.co/website ping.png?id=6b496921-42a5-48d8-bb44-2b3c73b71f29" />
                    </a>
                </td>
            </tr>
            <tr class="active">
                <td class="col-lg-9">my.robokassa.ru</td>
                <td class="col-lg-3 text-right">
                    <a href="https://www.host-tracker.com/UptimeGraph/UptimeInfo/9f8c7b25-36bb-4d98-b2ea-6a234e308366" rel="nofollow" target="_blank">
                        <img style="border: 0" alt="" src="//i.h-t.co/website ping.png?id=9f8c7b25-36bb-4d98-b2ea-6a234e308366" />
                    </a>
                </td>
            </tr>
            <tr class="active">
                <td class="col-lg-9">auth.robokassa.ru/my</td>
                <td class="col-lg-3 text-right">
                    <a href="https://www.host-tracker.com/UptimeGraph/UptimeInfo/e774be87-16c0-453a-9f97-4420bc7db94d" rel="nofollow" target="_blank">
                        <img style="border: 0" alt="" src="//i.h-t.co/website ping.png?id=e774be87-16c0-453a-9f97-4420bc7db94d" />
                    </a>
                </td>
            </tr>
            <tr class="active">
                <td class="col-lg-9">www.caravan.ru</td>
                <td class="col-lg-3 text-right">
                    <a href="https://www.host-tracker.com/UptimeGraph/UptimeInfo/001b2879-8377-4340-a9cc-56d4e494aa25" rel="nofollow" target="_blank">
                        <img style="border: 0" alt="" src="//i.h-t.co/website ping.png?id=001b2879-8377-4340-a9cc-56d4e494aa25" />
                    </a>
                </td>
            </tr>
        </table>
    </div>
</div>

			</div>
		</div>
	</div>
	<div class="col-lg-4">
		<div class="row">
			<div class="col-lg-12" id="PsStates">
				
				


<div class="row">
	<div class="col-lg-12 text-center">
		<h4>Состояние платежных систем <small>(<a data-ajax="true" data-ajax-begin="face.onBegin(&#39;PsStatesWait&#39;, &#39;PsStatesData&#39;)" data-ajax-method="Post" data-ajax-mode="replace" data-ajax-update="#PsStates" href="/admin2/Face/PsStates">обновить</a>)</small></h4>
	</div>
</div>
<div id="PsStatesWait" class="row show">
	<div class="col-lg-12">
		<table class="table-striped col-lg-12">
			<tr>
				<td class="c text-primary">Обновление...</td>
			</tr>
		</table>
	</div>
</div>
<div id="PsStatesData" class="row hidden">
</div>

	<script type="text/javascript">
		$.ajax({
			url: '/admin2/Face/PsStates',
			success: function (data) {
				$("#PsStates").html(data);
			}
		})
	</script>

			</div>
		</div>
	</div>
	<div class="col-lg-4">
		<div class="row">
			<div class="col-lg-12" id="Statistics">
				
				


<div class="row">
	<div class="col-lg-12 text-center">
		<h4>Статистика текущего дня <small>(<a data-ajax="true" data-ajax-begin="face.onBegin(&#39;StatisticsWait&#39;, &#39;StatisticsData&#39;)" data-ajax-method="Post" data-ajax-mode="replace" data-ajax-update="#Statistics" href="/admin2/Face/Statistics">обновить</a>)</small></h4>
	</div>
</div>
<div id="StatisticsWait" class="row show">
	<div class="col-lg-12">
		<table class="table-striped col-lg-12">
			<tr>
				<td class="c text-primary">Обновление...</td>
			</tr>
		</table>
	</div>
</div>
<div id="StatisticsData" class="row hidden">
</div>

	<script type="text/javascript">
		$.ajax({
			url: '/admin2/Face/Statistics',
			success: function (data) {
				$("#Statistics").html(data);
			}
		})
	</script>

			</div>
		</div>
	</div>
</div>
            </div>
        </div>
        <div class="row">
            
            <div class="col-lg-12">
                <div class="pull-right" style="color: Gray;">&copy; 2002-2019 ROBOKASSA</div>
            </div>
        </div>
        
    </div>

    

    
</body>
</html>


"""
