from gtts import gTTS
import os, playsound


language = 'en'


def speak(msg):
    filename='output.mp3'
    voice_output = gTTS(text=msg, lang=language, slow=False)
    voice_output.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def speak_OS(msg, OS):
    if OS == 0:
        os.system("say {}".format(msg))
    elif OS == 1:
        speak(msg)