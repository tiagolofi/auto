
from navevoice import NaveVoice
from time import sleep
from pyautogui import PAUSE, press, write, press, hotkey
from sys import exit

class BotNave(object):
	"""docstring for BotNave"""
	def __init__(self):
		super(BotNave, self).__init__()
		self.voice = NaveVoice()
		self.PAUSE = 2
		self.dictionary = {
			'whatsapp': 'https://web.whatsapp.com/',
			'youtube': 'https://www.youtube.com/',
			'netflix': 'https://www.netflix.com/browse',
			'twitter': 'https://twitter.com/home',
			'facebook': 'https://www.facebook.com/',
			'anime': 'https://www.crunchyroll.com/pt-br/videos/anime',
			'git': 'https://github.com/tiagolofi',
			'pesquisar': 'https://www.google.com.br/'
		}

	def browser(self):

		web = self.voice.voice_to_text()

		print(web, '\n')

		if web in list(self.dictionary.keys()):
	
			press('win')

			write('google chrome')

			press('enter')

			sleep(2)

			write(self.dictionary.get(web))

			press('enter')

		elif web == 'fechar guia':

			hotkey('ctrl', 'w')

		elif web == 'encerrar':

			exit()

		else:

			return False
