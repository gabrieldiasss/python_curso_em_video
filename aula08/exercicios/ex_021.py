# Tocar mp3
from pygame import mixer

mixer.init()

mixer.music.load('musica.mp3')
mixer.music.play()
x = input('Digite algo para parar...')
