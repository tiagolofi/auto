"""Source for BotNave"""

from navevoice import NaveVoice
from time import sleep
from pyautogui import PAUSE, press, write, press, hotkey
from sys import exit
from playsound import playsound

class BotNave(object):
	"""docstring for BotNave"""
	def __init__(self):
		super(BotNave, self).__init__()
		self.voice = NaveVoice()
		self.PATH = 'C:/Users/usuario/Documents/Ambientes/AUTOMATION/auto/audios/'
		self.PAUSE = 0.5
		self.dictionary = {
			'whatsapp': 'https://web.whatsapp.com/',
			'youtube': 'https://www.youtube.com/',
			'netflix': 'https://www.netflix.com/browse',
			'twitter': 'https://twitter.com/home',
			'facebook': 'https://www.facebook.com/',
			'anime': 'https://www.crunchyroll.com/pt-br/videos/anime',
			'repositório': 'https://github.com/tiagolofi',
			'instagram': 'https://www.instagram.com/',
			'pesquisar': 'https://www.google.com.br/',
			'jogar': 'https://poki.com.br/g/repuls-io',
			'trelo': 'https://trello.com/tiagomatos60/boards',
			'música': 'https://open.spotify.com/artist/58oPVy7oihAEXE0Ott6JOf',
			'telegram': 'https://web.telegram.org/k/',
			'link': 'https://www.linkedin.com/feed/'
		}

	def main(self):

		command = self.voice.voice_to_text()

		if command == 'navegador':

			press('win')

			write('google chrome')

			press('enter')

			playsound(self.PATH + 'navegador.mp3')

		elif command in list(self.dictionary.keys()):

			hotkey('ctrl', 't')

			playsound(self.PATH + 'nova_pagina.mp3')

			write(self.dictionary.get(command))

			press('enter')

			if command == 'pesquisar':

				texto = self.voice.voice_to_text()

				if len(texto) == 0:

					pass

				else:

					write(texto)

					press('enter')

		elif command == 'fechar':

			hotkey('ctrl', 'w')

			playsound(self.PATH + 'guia_fechada.mp3')

		elif command == 'encerrar':

			exit()

		elif command == None:

			pass

		else:

			playsound(self.PATH + 'desculpas.mp3')
