
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
			'instagram': 'https://www.instagram.com/',
			'pesquisar': 'https://www.google.com.br/',
			'jogar': 'https://poki.com.br/g/repuls-io'
		}

	def browser(self):

		web = self.voice.voice_to_text()

		if web == 'navegador':

			print(web, '\n')

			press('win')

			write('google chrome')

			press('enter')

		else:

			pass

	def navegation(self):

		web = self.voice.voice_to_text()

		if web in list(self.dictionary.keys()):

			print(web, '\n')

			hotkey('ctrl', 't')

			sleep(2)

			write(self.dictionary.get(web))

			press('enter')

			if web == 'pesquisar':

				texto = self.voice.voice_to_text()

				if len(texto) == 0:

					pass

				else:

					write(texto)

					press('enter')

		elif web == 'fechar':

			print(web, '\n')

			hotkey('ctrl', 'w')

		elif web == 'encerrar':

			print(web, '\n')

			exit()

		else:

			pass
