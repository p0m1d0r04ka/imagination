#!/usr/bin/python
# Author: imagination 
# https://github.com/p0m1d0r04ka/imagination

import vk, urllib.request, urllib.error, urllib.parse, json, random, time
import threading
import sys

import os
import platform

HOME_PATH = os.path.expanduser("~")
SPAMMER_PATH = os.path.join(HOME_PATH + "/" + ".vk-spammer/")

API_VERSION = 5.73

DELAY = 2 # Количество секунд задержки


# -------------------------------------------
# Сообщения, которые будет отправлять спаммер
messages = [
		"ÿþ&T vç"ÂR@#R' :OS T" "#O#t>Ø@Ý ",
	"ÒÛ ÏÎÍÈÌÀÅØÜ ×ÒÎ ß ÒÂÎÞ ÌÀÒÜ ÎÒÏÐÀÂÈË ÑÎ ÑÂÎÅÃÎ ÚÕÓß Â ÍÅÁÎ, ×ÒÎÁ ÎÍÀ ÑÂÎÈÌ ÏÈÇÄÀÊÎÌ ÏÐÈÍÈÌÀËÀ ÌÈÒÅÎÐÈÒÍÓÞ ÀÒÀÊÓ?)",
	" ÒÛ ÏÎÍÈÌÀÅØÜ ×ÒÎ ß ÂÎ ÂÐÅÌß ÕÎÊÊÅÉÍÎÃÎ ÌÀÒ×À, ÒÂÎÞ ÌÀÒÜ ÂÛÈÊÍÓË ÍÀÕÓÉ ÍÀ ÏËÎÙÀÄÊÓ, ×ÒÎÁ ÎÍÀ ÏÈÇÄÀÊÎÌ ÑÂÎÈÌ ÂÎÐÎÒÀ ÐÓÑÑÊÈÕ ÇÀÙÈÙÀËÀ?) ",
	" Твой рот настолько уродский, что его могут украсить только хуи  ",
	" зачем тебе жить, если тебя и так жизнь наказала ",
	"я твою мать кастрюлей ебал ",
	" зачем ты придумываешь всякую хуйню, если твоя работа это сосать мне ",
	" твой подзалупный творожок хорошо смотрится в твоём рту  ",
	"пожалуйста вытри слезы, ведь твоя жизнь и так хуевая  ",
	" жаль я тебя не видел раньше. Хотя такого долбаеба еще поискать надо  ",
	" мои счисления верны. Твой интелект ниже банана ",
	" сочиняй дальше, не останавливайся. Я пока поебу тебе мозги  ",
	" твои хромосомы мне рассказали что тебя в детстве роняли   ",
	"  я дам тебе поспать, но с одрим условием. Ты засунешь в себя бутылку ",
	" оправдывайся дальше. Твои оправдания лишь мне на пользу  ",
	" зачем ты себя унижаешь и плачешь , вытирая слезы об мой хуй  ",
	" твои приколы похожи на залупу века, в которых ты как всегда ноешь  ",
	" повторы бывают всегда, главное чтобы ты запомнил  ",
	" и самое главное не переводи на меня стрелки, хотя у тебя даже лука нет  ",
	" я смотрю ты слишком грустный.  ",
	" не переживай , твоя работа на трассе никуда не денется  ",
	" ты можешь лизать пизду своей мамаши, но лучше не вынимай оттуда свой рот, ведь твое нытье никому не чуждо слышать  ",
	" повторы бывают у всех, так что не ной и перечитывай свой позор  ",
	" запомни раз и навсегда, быть долбаебом у тебя в крови  ",
	" зачем ты себя унижаешь, все же знают что ты шлюха  ",
	" не ной мне, я тебе не мать, чтобы выслушивать твои проблемы  ",
	"во ты долбаеб ",
	"в инкубаторе тоже птицы, но чтобы человека вырастили, я вижу впервые. Что ты в этом деле первопроходец ",
	"плак плак плак. Твои слезы словно амир родившийся не в пизде , а во рту шлюхи ",
	" не убеждай меня в том что ты долбаеб  ",
	" как же весело с тобой слитым вести диалог  "
	
	
	
	
]
# -------------------------------------------

if not os.path.exists(SPAMMER_PATH):
	os.mkdir(SPAMMER_PATH)

if os.path.exists(SPAMMER_PATH + "messages.txt"):
	messages = []
	with open(SPAMMER_PATH + "messages.txt") as f:
		for line in f:
			messages.append(line)

if len(messages) == 0:
	messages = [
		"ÿþ&T vç"ÂR@#R' :OS T" "#O#t>Ø@Ý ",
	"ÒÛ ÏÎÍÈÌÀÅØÜ ×ÒÎ ß ÒÂÎÞ ÌÀÒÜ ÎÒÏÐÀÂÈË ÑÎ ÑÂÎÅÃÎ ÚÕÓß Â ÍÅÁÎ, ×ÒÎÁ ÎÍÀ ÑÂÎÈÌ ÏÈÇÄÀÊÎÌ ÏÐÈÍÈÌÀËÀ ÌÈÒÅÎÐÈÒÍÓÞ ÀÒÀÊÓ?)",
	" ÒÛ ÏÎÍÈÌÀÅØÜ ×ÒÎ ß ÂÎ ÂÐÅÌß ÕÎÊÊÅÉÍÎÃÎ ÌÀÒ×À, ÒÂÎÞ ÌÀÒÜ ÂÛÈÊÍÓË ÍÀÕÓÉ ÍÀ ÏËÎÙÀÄÊÓ, ×ÒÎÁ ÎÍÀ ÏÈÇÄÀÊÎÌ ÑÂÎÈÌ ÂÎÐÎÒÀ ÐÓÑÑÊÈÕ ÇÀÙÈÙÀËÀ?) ",
	" Твой рот настолько уродский, что его могут украсить только хуи  ",
	" зачем тебе жить, если тебя и так жизнь наказала ",
	"я твою мать кастрюлей ебал ",
	" зачем ты придумываешь всякую хуйню, если твоя работа это сосать мне ",
	" твой подзалупный творожок хорошо смотрится в твоём рту  ",
	"пожалуйста вытри слезы, ведь твоя жизнь и так хуевая  ",
	" жаль я тебя не видел раньше. Хотя такого долбаеба еще поискать надо  ",
	" мои счисления верны. Твой интелект ниже банана ",
	" сочиняй дальше, не останавливайся. Я пока поебу тебе мозги  ",
	" твои хромосомы мне рассказали что тебя в детстве роняли   ",
	"  я дам тебе поспать, но с одрим условием. Ты засунешь в себя бутылку ",
	" оправдывайся дальше. Твои оправдания лишь мне на пользу  ",
	" зачем ты себя унижаешь и плачешь , вытирая слезы об мой хуй  ",
	" твои приколы похожи на залупу века, в которых ты как всегда ноешь  ",
	" повторы бывают всегда, главное чтобы ты запомнил  ",
	" и самое главное не переводи на меня стрелки, хотя у тебя даже лука нет  ",
	" я смотрю ты слишком грустный.  ",
	" не переживай , твоя работа на трассе никуда не денется  ",
	" ты можешь лизать пизду своей мамаши, но лучше не вынимай оттуда свой рот, ведь твое нытье никому не чуждо слышать  ",
	" повторы бывают у всех, так что не ной и перечитывай свой позор  ",
	" запомни раз и навсегда, быть долбаебом у тебя в крови  ",
	" зачем ты себя унижаешь, все же знают что ты шлюха  ",
	" не ной мне, я тебе не мать, чтобы выслушивать твои проблемы  ",
	"во ты долбаеб ",
	"в инкубаторе тоже птицы, но чтобы человека вырастили, я вижу впервые. Что ты в этом деле первопроходец ",
	"плак плак плак. Твои слезы словно амир родившийся не в пизде , а во рту шлюхи ",
	" не убеждай меня в том что ты долбаеб  ",
	" как же весело с тобой слитым вести диалог  "
	
	
	
	
	]


class MainThread(threading.Thread):
	def run(self):
		print("-" * 4)
		print("Delay: ", args.delay)
		print("-" * 4)
		DELAY = args.delay
		while(True):
			try:
				msg = random.choice(messages)
				r = vk.messages.send(peer_id = victim, message = msg, v = API_VERSION)
				print("Sent ", msg)
				time.sleep(DELAY)
			except Exception as e:
				print(e)
				pass

def main():
	try:
		thread = MainThread()
		thread.daemon = True
		thread.start()

		while thread.is_alive():
			thread.join(1)
	except KeyboardInterrupt:
		print("Ctrl+C pressed...")
		sys.exit(1)

import argparse
parser = argparse.ArgumentParser(description='Spam settings:')
parser.add_argument(
    '-d',
    '--delay',
    type=int,
    default=4,
    help='Delay (default: 4)'
)
parser.add_argument('-e', '--editmessages', action='store_true', help='Use this argument to edit the message list')
args = parser.parse_args()

if(args.editmessages):
	if platform.system() == "Windows":
		os.system("notepad.exe " + SPAMMER_PATH + "messages.txt")
	if platform.system() == "Linux":
		os.system("nano " + SPAMMER_PATH + "messages.txt")
	print("Please restart vk-spammer to reload the message list")
	exit(0)

username = input("Login: ")
password = input("Password: ")

url = "https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username=%s&password=%s" % (username, password)

try:
    r = urllib.request.urlopen(url)
except urllib.error.HTTPError:
    print("Не удалось залогиниться, возможно вы ввели неправильный пароль")
    quit(1)

r = r.read()
token = json.loads(r)["access_token"] 
session = vk.Session(access_token = token)
vk = vk.API(session)

victim = input("User id: ")

victim = victim.split("/")
print(victim)
victim = victim[len(victim) - 1]

if victim.isdigit():
	victim = victim
else:
	print("Resolving screen name...")
	r = vk.utils.resolveScreenName(screen_name = victim, v = API_VERSION)
	victim = r["object_id"]
	print("It is: " + str(victim))

r = vk.users.get(user_id = victim, fields = "id", v = API_VERSION)
r = r[0]["id"]

victim = r

main()
