import telebot;
import os
import subprocess
import re
#получение токена при запуске и возможно его сохранение
file = open("Token", "r")
token = file.read()
file.close()
bot = telebot.TeleBot(token)
os.system("echo запущено")
@bot.message_handler(content_types=['text'])
def get_text_messages(message): 
	if message.text == "/start":
		bot.send_message(message.from_user.id, "bashbot для Телеграмм список основных команд /help")
	elif message.text == "/help":
		bot.send_message(message.from_user.id, "здесь пока что пусто") ##
	else:
		comm_out=(b'',)
		lst = message.text.split(' ')
		print(lst[0]) 
		if (lst[0] == 'cd'):
			del lst[0]
			if not lst: 
				lst = ['/root']
			path="".join(lst)
			try:
				os.chdir(path)
			except FileNotFoundError:
				bot.send_message(message.from_user.id, "No such file or directory")
			else:
				comm = subprocess.Popen('pwd', stdout=subprocess.PIPE) 
				comm_out = comm.communicate()				
		elif(lst[0] == 'echo'):
			comm = subprocess.Popen(lst, stdout=subprocess.PIPE) 
			comm_out = comm.communicate()
			print(comm_out)##
		elif(lst[0] == 'export'):
			c = "".join(lst)
			print(message.text)
			os.system(message.text)
			bot.send_message(message.from_user.id, "не готово")##
		else:
			try:
				comm = subprocess.Popen(message.text.split(' '), stdout=subprocess.PIPE) 
				comm_out = comm.communicate()
				print(comm_out)
			except FileNotFoundError:
				bot.send_message(message.from_user.id, "No such file or directory")
		if (comm_out[0] != b''):
			bot.send_message(message.from_user.id, comm_out) 
bot.polling(none_stop=True, interval=0)
#сделать логи по ID
#добавить clear