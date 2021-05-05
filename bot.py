import telebot;
import os
import subprocess
import re
#получение токена при запуске и возможно его сохранение
bot = telebot.TeleBot('')
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
			os.chdir(path)
			comm = subprocess.Popen('pwd', stdout=subprocess.PIPE) #отлавливать no such file or directory и stderr(-)
			comm_out = comm.communicate()
		elif(lst[0] == 'echo'):
			bot.send_message(message.from_user.id, "нет")##
		elif(lst[0] == ['export']):
			bot.send_message(message.from_user.id, "нет")##
		else:
			comm = subprocess.Popen(message.text.split(' '), stdout=subprocess.PIPE) #отлавливать no such file or directory и stderr
			comm_out = comm.communicate()
			print(comm_out)
		if (comm_out[0] != b''):
			bot.send_message(message.from_user.id, comm_out) #отлавливать пустые строки
bot.polling(none_stop=True, interval=0)
#сделать логи по ID