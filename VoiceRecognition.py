import speech_recognition as sr
import tkinter as tk
from pynput.keyboard import Controller as Controls, Key
from pynput.mouse import Controller as Mouse_Controls
from gtts import gTTS
from googlesearch import search
import os,send_email, volume, weather, small_tasks, playsound, platform, Speak, mouse_control, Joke
import threading, file_transfer

root = tk.Tk()
screen_dim = (root.winfo_screenwidth(), root.winfo_screenheight())
mouse = mouse_control.controller(screen_dim)
root.destroy()
kb = Controls()
ms = Mouse_Controls()
print(screen_dim)


KEYWORD = 'alvin'
no_no_words = []

speak = Speak.speak
speak_OS = Speak.speak_OS

op = platform.platform()

if op[:5] == "macOS":
    OS = 0
elif op[:5] == "Windo":
    OS = 1
else:
    speak("System Error")
    exit()

file_transfer.set_OS(OS)
print("OS: {}".format(OS))

recv_thread = threading.Thread(target= file_transfer,daemon = False)
recv_thread.start()


def responses(query):

    if 'open application' in query:
        if OS == 0:
            os.system('say Opening {0}; open -a {0}'.format("\ ".join([x.capitalize() for x in query.split()][query.split().index('application')+1:])))
        if OS == 1:
            text = "\ ".join([x.capitalize() for x in query.split()][query.split().index('application')+1:])
            speak("Opening {0}".format(text))
            os.system('start {0}'.format(text))

    elif 'look up' in query:
        search_query = " ".join(query.split()[query.split().index('up')+1:])
        for i in search(search_query, tld="com", num=10, stop=1, pause=2):
            if OS == 0:
                os.system("say Here is what I found for {}; open {}".format(search_query, i))
            elif OS == 1:
                speak("Here is what I found for {}".format(search_query))
                os.system('start {}'.format(i))

    elif 'chrome' in query:
        if OS == 0:
            os.system('say Opening chrome; open -a Google\ Chrome')
        elif OS == 1:
            speak("Opening Chrome")
            os.system('start www.google.com')

    elif 'safari' in query:
        if OS == 0:
            os.system('say Opening Safari; open -a Safari')
        elif OS == 1:
            speak("This application does not exist for Windows")
    elif 'terminal' in query or 'command prompt' in query:
        if OS == 0:
            os.system('say Opening terminal; open -a terminal')
        elif OS == 1:
            speak("Opening Command Prompt")
            os.system('start cmd')


    elif 'send mail' in query or 'send email' in query:
        send_email.send_email(query, OS)
            

    # SPOTIFY SECTION DOES NOT WORK ON WINDOWS
    elif 'play spotify' in query or 'play music' in query:
        if OS == 0:
            os.system('Spotify play')
        else:
            speak("This feature is not currently available for Windows")
    elif 'pause spotify' in query or 'pause music'in query:
        if OS == 0:
            os.system('Spotify pause')
        else:
            speak("This feature is not currently available for Windows")
    elif 'next song' in query:
        if OS == 0:
            os.system('Spotify next')
        else:
            speak("This feature is not currently available for Windows")
    elif 'previous song' in query or 'last song' in query:
        if OS == 0:
            os.system('Spotify back')
        else:
            speak("This feature is not currently available for Windows")
    elif 'replay song' in query or 'repeat song' in query:
        if OS == 0:
            os.system('Spotify replay')
        else:
            speak("This feature is not currently available for Windows")


    elif 'volume' in query:
        if OS == 0:
            volume.volume_mac(query)
        elif OS == 1:
            volume.volume_windows(query)

    elif 'weather' in query: #DOES NOT WORK
        weather.weather(query)


    elif 'flip a coin' in query:
        speak_OS(small_tasks.flip_coin(), OS)
    elif 'roll a die' in query:
        speak_OS(small_tasks.roll_die(), OS)
    elif 'count' in query:
        speak_OS(small_tasks.count(query, OS),OS)

    elif "type" in query:
        kb.type(" ".join(query.split()[query.split().index("type")+1:]))
    elif "hit enter" in query:
        kb.press(Key.enter)
        kb.release(Key.enter)

    elif 'mouse' in query:
        speak_OS("Mouse mode enabled", OS)
        mouse.enable(OS)

    elif "scroll left" in query:
        ms.scroll(-5,0)
    elif "scroll right" in query:
        ms.scroll(5,0)
    elif "scroll up" in query:
        ms.scroll(0,5)
    elif "scroll down" in query or "scroll" in query:
        ms.scroll(0,-5)

    elif "joke" in query:
        speak_OS(Joke.joke(), OS)



    elif 'kill yourself' in query:
        speak_OS("Goodbye.", OS)
        global dead
        dead = True
    

def command():
    i = 1
    r = sr.Recognizer()

    with sr.Microphone() as source:

        # while True:
        # try:
            query = ""
            # print('a')

            try:
                audio = r.listen(source, timeout = 2)
                # print('e')
                query = r.recognize_google(audio).lower()
                # print('c')
            except:
#                print("ERROR")
                return

            if KEYWORD in query:
                os.system("echo -ne '\007'")

                audio = r.listen(source, timeout = 5)
                
                os.system("echo -ne '\007'")


                # try:
                query = r.recognize_google(audio).lower()
                print(query)
                for word in query.split():
                    if word in no_no_words:
                        query = ""
                        speak_OS('I am sorry. I can not do that',OS)
                responses(query)

                    
        #         except:
        #             print("I did not catch that")
        # except:
        #     print("ERROR")

 


print("Speak Anything : ")
i = 0
dead = False
while True:
    i+=1
    print(i)
    command()
    if dead:
        break
