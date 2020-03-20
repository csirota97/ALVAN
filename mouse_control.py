import Speak, os
import speech_recognition as sr
from pynput.mouse import Button, Controller

speak_OS = Speak.speak_OS
    
class controller():
    def __init__(self, size):
        
        self.WIDTH = size[0]
        self.HEIGHT = size[1]
        self.mouse = Controller()

    def w2n(word):
        if type(word) == int:
            return word
        if word == "zero":
            return 0
        elif word == "one":
            return 1
        elif word == "two":
            return 2
        elif word == "three":
            return 3
        elif word == "four":
            return 4
        elif word == "five":
            return 5
        elif word == "six":
            return 6
        elif word == "seven":
            return 7
        elif word == "eight":
            return 8
        elif word == "nine":
            return 9
        elif word == "ten":
            return 10
        else:
            return int(word)

    def enable(self, OS):
        # try:
            r = sr.Recognizer()
            r.dynamic_energy_threshold = False
            with sr.Microphone() as source:
                while True:
                    try:
                        audio = r.listen(source, timeout = 2)
                        query = r.recognize_google(audio).lower()
                        print(query)
                        
                        if "position" in query or "possession" in query:
                            # try:
                            os.system("echo -ne '\007'")
                            audio = r.listen(source, timeout = 3)
                            os.system("echo -ne '\007'")
                            query = r.recognize_google(audio).lower().split()
                            # except:
                            #     continue

                            if "up" in query or "down" in query or "left" in query or "right"  in query:
                                x = 0
                                y = 0
                                delta = None
                                print (query)
                                for word in query:
                                    try:
                                        if word[-1] == ',':
                                            word = word[:-1]
                                        if delta == None:
                                            delta = w2n(word)
                                            break
                                    except:
                                        pass

                                delta = abs(delta)

                                if "up" in query:
                                    y -= delta
                                if "down" in query:
                                    y += delta
                                if "left" in query:
                                    x -= delta
                                if "right" in query:
                                    x += delta

                                print(x,y)
                                self.mouse.position = (self.mouse.position[0] + int(self.WIDTH*(x-1)/100),self.mouse.position[1] + int(self.HEIGHT*(y-1)/100))

                            else:
                                x = None
                                y = None
                                for word in query:
                                    try:
                                        if word[-1] == ',':
                                            word = word[:-1]
                                        if x == None:
                                            x = w2n(word)
                                        else:
                                            y = w2n(word)
                                            break
                                    except:
                                        pass
                                print (x, y)

                                self.mouse.position = (int(self.WIDTH*(x-1)/100),int(self.HEIGHT*(y-1)/100))

                        elif "double right click" in query:
                            self.mouse.click(Button.right, 2)
                            
                        elif "right click" in query:
                            self.mouse.click(Button.right)

                        elif "double-click" in query or "double left-click" in query:
                            self.mouse.click(Button.left,2)
                        elif "click" in query:
                            self.mouse.click(Button.left)

                        elif "scroll left" in query:
                            self.mouse.scroll(-5,0)
                        elif "scroll right" in query:
                            self.mouse.scroll(5,0)
                        elif "scroll up" in query:
                            self.mouse.scroll(0,5)
                        elif "scroll down" in query or "scroll" in query:
                            self.mouse.scroll(0,-5)

                        if "exit" in query:
                            speak_OS("Mouse Mode Disabled", OS)
                            return
                    except:
                        pass
        #                 return
        # except:
        #     pass