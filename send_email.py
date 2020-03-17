import smtplib, config, os, Speak
import speech_recognition as sr

speak = Speak.speak

def send_email(query, OS):
    import contacts
    if 'to' in query:
        names = " ".join(query.split()[query.split().index('to')+1:])
    else:
        names = None
        
    try:

        r = sr.Recognizer()
        with sr.Microphone() as source:

            if names == None:
                while True:
                    try:
                        if OS == 0:
                            os.system('say "Who would you like to email?"')
                        elif OS == 1:
                            speak("Who would you like to email?")
                        os.system("echo -ne '\007'")
                        audio = r.listen(source, timeout = 2)
                        os.system("echo -ne '\007'")
                        query = r.recognize_google(audio).lower()
                        valid = True
                    except:
                        valid = False

                    if valid:
                        break
            else:
                query = names

            if " and " in query:
                query = query.split(" and ")
            else:
                query = [query]
                
            addresses = []
            for name in query:
                try:
                    addresses.append(contacts.contacts[name])
                except:
                    if OS == 0:
                        os.system("say Could not find email address for: {}".format(name))
                    elif OS == 1:
                        speak("Could not find email address for: {}".format(name))

            print(addresses)

            while True:
                try:
                    if OS == 0:
                        os.system('say "What would you like the subject to be?"')
                    elif OS == 1:
                        speak("What would you like the subject to be?")
                    os.system("echo -ne '\007'")
                    audio = r.listen(source, timeout = 4)
                    os.system("echo -ne '\007'")
                    subject = r.recognize_google(audio)
                    valid = True
                except:
                    valid = False

                if valid:
                    break

            while True:
                try:
                    if OS == 0:
                        os.system('say "What would you like the message to say?"')
                    elif OS == 1:
                        speak("What would you like the message to say?")
                    os.system("echo -ne '\007'")
                    audio = r.listen(source, timeout = 5)
                    os.system("echo -ne '\007'")
                    msg = r.recognize_google(audio)
                    valid = True
                except:
                    valid = False

                if valid:
                    break

            msg = msg.replace("new line ", "\n")
            msg = msg.replace("New line ", "\n")
            msg = msg.replace("new line", "\n")
            msg = msg.replace("New line", "\n")

            msg = "\n".join([x.capitalize() for x in msg.split('\n')])


            while "YES" not in query:

                if OS == 0:
                    os.system('say "Are you sure you would like to send this?"')
                elif OS == 1:
                    speak("Are you sure you would like to send this?")
                try:
                    os.system("echo -ne '\007'")
                    audio = r.listen(source, timeout = 4)
                    os.system("echo -ne '\007'")
                    query = r.recognize_google(audio).upper()
                    if "NO" in query or "CANCEL" in query:
                        return
                    elif "READ" in query:

                        if len(addresses) > 2:
                            names = ", ".join(addresses)
                            for i in range(len(names)):
                                if names[-i] == ',':
                                    names = names[:-i+1] + ' and' + names[-i+1:]
                                    break

                        elif len(addresses) == 2:
                            names = addresses[0]+ ' and ' + addresses[1]

                        if OS == 0:
                            os.system('say "The message to {}, with subject {}, says the following: {}"'.format(names, subject, msg))
                        elif OS == 1:
                            speak("The message to {}, with subject {}, says the following: {}".format(names, subject, msg))

                except:
                    pass

        send_mail(addresses, subject, msg)


        if OS == 0:
            os.system('say "Message sent"')
        elif OS == 1:
            speak("Message sent")

    except:
        if OS == 0:
            os.system('say "Message could not be sent"')
        elif OS == 1:
            speak("Message could not be sent")

def send_mail(target ,subject, message):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
        msg = 'Subject: {}\n\n{}'.format(subject, message)
        server.sendmail(config.EMAIL_ADDRESS, target, msg)
        server.quit()

    except:
        pass
