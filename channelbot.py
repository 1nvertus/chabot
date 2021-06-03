import telebot;
import random
import requests
from bs4 import BeautifulSoup
bot = telebot.TeleBot('1884289982:AAEc9vGgabGY-6IMqR-7065gYk1CaCCZeEA')
def news():
	url = 'https://www.hltv.org/events'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')
	quotes = soup.find_all('div', class_='text-ellipsis')
	#find_news=random.choice (quotes)
	site=[]
	for i in quotes:
		site.append(i.text)
	#return(find_news.text)
	site = random.choice(site)
	return site

message_1 = ['Нормально', 'Всё очень хорошо, меня запустили:), а у тебя как?']
channels_1 = ['https://www.youtube.com/user/dj47maryn','https://www.youtube.com/user/ShaftChenal','https://www.youtube.com/user/TheKupidMan','https://www.youtube.com/channel/UCwAlUoQBC1Tqn0PlrNDDz_A','https://www.youtube.com/user/Warpath031','https://www.youtube.com/channel/UCL-nbxU92PJiCfCJLFMQ6OA','https://www.youtube.com/channel/UCuTQE-o6ltEiYfF77bWfEmA','https://www.youtube.com/user/sukapush']

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == "Привет":
		bot.send_message(message.from_user.id, "Привет, сейчас я найду твоего любимого ютубера.")
	elif message.text == "Как дела?":
		bot.send_message(message.from_user.id, random.choice(message_1))	
	elif message.text == "Кинь ивент":
		bot.send_message(message.from_user.id, news())
	elif message.text == "Нормально":
		bot.send_message(message.from_user.id, "Мммм.... понятно")
	elif message.text == "Кинь рандомный канал":
		bot.send_message(message.from_user.id, random.choice(channels_1))
	elif message.text == "/help":
		bot.send_message(message.from_user.id, "Если хочешь, можешь написать (Найди Бустера на ютубе,Найди Шарфа,Найди Мурза)-это для ютуба, или можешь написать любимого стримера на twitch(Найди Санрайза,Найди Бустера на твиче и тд.) бот еще может поговорить с тобой либо ниайти рандомного ютубера просто написав ему (Кинь рандомный канал) также можешь посмотреть киберновости) написав Новости киберспорта")
	elif message.text == "Найди Бустера на ютубе":
		bot.send_message(message.from_user.id, "https://www.youtube.com/channel/UCve3ohcLCBO5uFoQcFGZMPQ")
	elif message.text == "Найди Шарфа":
		bot.send_message(message.from_user.id, "https://www.youtube.com/channel/UCb-Xo1DgpY1YhdgXg8rvjVA")
	elif message.text == "Новости киберспорта":
		bot.send_message(message.from_user.id, "https://www.cybersport.ru/news")
	elif message.text == "Найди Мурза":
		bot.send_message(message.from_user.id, "https://www.youtube.com/channel/UCtDUJoWBgUaYUeHtMA0LNGg")
	elif message.text == "Найди Санрайза":
		bot.send_message(message.from_user.id, "https://www.twitch.tv/sunrise_xxl")
	elif message.text == "Найди Бустера на твиче":
		bot.send_message(message.from_user.id, "https://www.twitch.tv/buster")
	else:
		bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)
		
