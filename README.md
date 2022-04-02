# Automações com Python

### Módulo de reconhecimento de voz

[**NaveVoice**](navevoice.py)

### Módulo de navegação automatizada

[**BotNave**](botnave.py)

### Integrações

- Whatsapp
- Facebook
- Instagram
- Spotify
- Netflix
- Crunchyroll
- YouTube
- Trello
- Github
- Google
- Poki
- Telegram
- Linkedin

### Código do Bot

```python

from botnave import BotNave

bot = BotNave()

while True:

	bot.main()

```

### Compilando com Pyinstaller

```
> pyinstaller --onefile -w --icon=imagebot.ico --splash botscreen.png bot.py
```

