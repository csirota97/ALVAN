import socket, config, random, Speak, threading

speak = Speak.speak_OS

ID = str(random.randint(0,0xFFFE))
while len(ID) < 4:
    ID = "0" + ID

destinations = {}
messages = []
OS = None

SYSTEM_NAME = DEFAULT_ALVAN

PING = 0
PING_CONFIRM = 1
READ_MESSAGE = 2
FILE_INCOMING = 3       #TODO: complete OP_CODEs 3 and 4
FILE_PACKET = 4
                        #TODO: sending messages
                        #TODO: TEST ALL THE GOODS

#MESSAGE FORMAT
#4 bytes DESTINATION ID | 4 bytes SOURCE ID | 4 bytes OP CODES | 4 bytes Message Length | 1012 bytes message
#WXYZABCD00010013HelloWorld123000000000000000000000000000000000000000000000...

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', config.port))

def set_OS(os):
    OS = os

def set_name(str):
    SYSTEM_NAME


def process_msgs():
    while True:
        try:
            msg, addr = messages[0]
            messages.pop(0)
            if msg[:4] != ID:
                msg = None
                continue

            frm = msg[4:8]

            if frm == ID:
                msg = None
                continue
            
            OP_CODE = int(msg[8:12])

            size = int(msg[12:16])

            msg = msg[16:16+size]

            if OP_CODE == PING:
                name_len = str(len(SYSTEM_NAME))
                while len(name_len) < 4:
                    name_len = "0" + name_len

                name = SYSTEM_NAME
                while len(name) < 1008:
                    name = name + '0'
                s.sendto(frm + ID + "0001" + name_len + name, ('255.255.255.255', config.port))
        
            elif OP_CODE == PING_CONFIRM:
                found = False
                destinations[frm] = (msg, addr)

            elif OP_CODE == READ_MESSAGE:
                speak("Message from: {}:".format(destinations[frm][0]))
                speak(msg,OS)


            msg = None

        except IndexError:
            pass

def recv_thread():
    proc_thread = threading.Thread(target=process_msgs, daemon=False)
    proc_thread.start()

    while True:
        messages.append(s.recv(1024).decode('utf-8'))

