import smtplib, config



def send_mail(subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
        msg = 'Subject: {}\n\n{}'.format(subject, message)
        server.sendmail(config.EMAIL_ADDRESS, "csirota97@gmail.com", msg)
        server.quit()

    except:
        pass

import speech_recognition as sr
from gtts import gTTS
from googlesearch import search
import os,send_email, volume, weather, small_tasks, playsound

KEYWORD = 'alvin'
no_no_words = []
language = 'en'

def speak(msg, filename='output.mp3'):
    voice_output = gTTS(text=msg, lang=language, slow=False)
    voice_output.save(filename)
    playsound.playsound(filename)

    
speak("Hello")
speak("World")