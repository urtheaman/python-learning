from gtts import gTTS
from playsound import playsound
import random
name = str(random.randrange(0,15)) + ".mp3"
print(name)
def convert_audio(text):
    my_audio = gTTS(text)
    my_audio.save(name)

x = input("Enter What You Want to convert : ")
convert_audio(x)
playsound(f'E:/Jarvis/{name}')
