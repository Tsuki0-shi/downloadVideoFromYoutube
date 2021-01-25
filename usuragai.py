import telebot
import pafy
import glob
import os
TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode=None)

title = "WITHOUT TITLE"
def download(url):
	try:
		global title
		global bestaudio
		audio = pafy.new(url)
		bestaudio = audio.getbestaudio()
		bestaudio.download()

		audiostreams = audio.audiostreams
		title = audio.title
		return True
	except:
		return False

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, я бот который скачивает аудио с Ютуба, для тебя! Для скачивания музыки с Ютуб отправь ссылку на него: ")

	
@bot.message_handler(content_types=["text"])
def content_text(message):
	dvideo = download(message.text)
	filename_list = glob.glob('*.' + bestaudio.extension)
	if dvideo == True:
		bot.send_message(message.chat.id, 'Загружено')
		bot.send_message(message.chat.id, 'Отправляю...')

		audio = open(filename_list[0], 'rb')
		bot.send_audio(message.chat.id, audio)
		audio.close()
		os.remove(filename_list[0])
	else:
		bot.send_message(message.chat.id, 'Невалидная ссылка')

bot.polling()

















