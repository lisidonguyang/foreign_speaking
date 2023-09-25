from gtts import gTTS
import os

tts = gTTS(text='kannst du an bisschen am arsch licken?', lang='de')
tts.save("good.mp3")
file = "good.mp3"
os.system("afplay " + file)