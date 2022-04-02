
from speech_recognition import Microphone, Recognizer, UnknownValueError

class NaveVoice(object):
	"""docstring for NaveVoice"""
	def __init__(self):
		super(NaveVoice, self).__init__()
		self.mic = Microphone()
		self.rec = Recognizer()
		
	def voice_to_text(self):

		with self.mic as source:

			self.rec.adjust_for_ambient_noise(source)
				
			audio = self.rec.listen(source)

		try:

			text = self.rec.recognize_google(audio, language = 'pt-BR')

			return text.lower()

		except UnknownValueError:

			pass
