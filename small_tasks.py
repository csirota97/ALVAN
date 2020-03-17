import random, time, os
import speech_recognition as sr
import Speak

speak = Speak.speak_OS

def flip_coin():
    if random.randint(0,1):
        return "Heads"
    return "Tails"

def roll_die():
    num = random.randint(1,6)
    if num == 1:
        return '1'
    elif num == 2:
        return '2'
    elif num == 3:
        return '3'
    elif num == 4:
        return '4'
    elif num == 5:
        return '5'
    return '6'

def count(query, OS):
    if 'to' not in query:
        r = sr.Recognizer()

        with sr.Microphone() as source:

            while True:
                try:
                    speak('how would you like to count?', OS)
                    os.system("echo -ne '\007'")
                    audio = r.listen(source, timeout = 4)
                    os.system("echo -ne '\007'")
                    # print('e')
                    query = r.recognize_google(audio).lower()
                    valid = True
                    # print('c')
                except:
                    valid = False

                if valid:
                    break
    try:
        to = 1
        t = False
        tf = False
        frm = 1
        f = False
        ff = False
        by = 1
        b= False
        bf = False

        words = query.split()

        for word in words:
            if word == "to":
                t = True
                tf = True
            elif t == True:
                t = False
                to = int(word)
            if word == "from":
                f = True
                ff = True
            elif f == True:
                f = False
                frm = int(word)
            if word == "by" or word == "x":
                b = True
                bf = True
            elif b == True:
                b = False
                by = int(word)

        if bf and not ff:
            frm = by

        if to > 100:
            return "Try something smaller"

        sequence = str(frm)

        if frm+by <= to:
            for i in range(frm+by, to+1, by):
                sequence += "\; {}".format(i) 

        return sequence
    except:
        return "Please try again"