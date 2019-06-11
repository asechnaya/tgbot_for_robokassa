htmltxt = """
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
							не работает
						</td>
					</tr>
					<tr class="active">
						<td class="l col-lg-9">
							Сервис учетной системы:
						</td>
						<td class="r nw col-lg-3 text-brown">
							работает медленно
						</td>
					</tr>
			</table>
		</div>
</div>

"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(htmltxt, 'html.parser')

BotState = soup.text
BotState = soup.find_all(class = 'col-lg-12').text
print(type(BotState))
BotState = BotState.replace('\t\t\t\t\t\t', '')
BotState = BotState.replace('\t', '')
BotState = BotState.split('\n')

print('-----JUJUJ------\n')

print(BotState)
