import socket, config, random, Speak, threading

speak = Speak.speak_OS

ID = str(random.randint(0,0xFFFE))
all_ID = '1111'
while len(ID) < 4:
    ID = "0" + ID

destinations = {}
messages = []
OS = None

SYSTEM_NAME = 'DEFAULT_ALVAN'

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
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2.bind(('', config.port-1))

def set_OS(os):
    OS = os

def send(op_code, recipient=None, message=None):
    if recipient == None:
        message = SYSTEM_NAME
        msg_len = str(len(message))
        while len(msg_len) < 4:
            msg_len = "0" + msg_len

        op_code = str(op_code)
        while len(op_code) < 4:
            op_code = '0' + op_code

        msg = message
        while len(msg) < 1008:
            msg = msg + '0'
        message = all_ID + ID + op_code + msg_len + msg
        s2.sendto(message.encode('utf-8'),('192.168.2.255', config.port))
        print("SENT")

    else:
        msg_len = str(len(message))
        while len(msg_len) < 4:
            msg_len = "0" + msg_len

        op_code = str(op_code)
        while len(op_code) < 4:
            op_code = '0' + op_code

        msg = message
        while len(msg) < 1008:
            msg = msg + '0'
        message = all_ID + ID + op_code + msg_len + msg
        try:
            s2.sendto(message.encode('utf-8'),(destinations[recipient], config.port))
        except:
            print("Receiver not found")

            
def set_name(str):
    SYSTEM_NAME


def process_msgs():
    while True:
        try:
            msg, addr = messages[0]
            msg = msg.decode('utf-8')
            print("MSG: ",msg)
            messages.pop(0)
            if msg[:4] != ID or msg[:4] != all_ID:
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
                s.sendto(frm + ID + "0001" + name_len + name, (addr[0], config.port))
        
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
    proc_thread = threading.Thread(target=process_msgs, daemon=True)
    proc_thread.start()

    while True:
        try:
            messages.append( s.recvfrom(1024))
        except:
            print("length",len(messages))
