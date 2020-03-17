import os

def volume_mac(query):
    words = query.split()
    if '%' in query:
        for word in words:
            if '%' in word:
                break
        word = word[:-1]
    else:
        nums = ['0','1','2','3','4','5','6','7','8','9']
        for word in words:
            if word[0] in nums:
                break

    if int(word) > 100:
        word == "100"
    elif int(word) < 0:
        word == "0"

    print(word)
    os.system("osascript -e 'set volume output volume {}'".format(word))

def volume_windows(query):
    words = query.split()
    if '%' in query:
        for word in words:
            if '%' in word:
                break
        word = word[:-1]
    else:
        nums = ['0','1','2','3','4','5','6','7','8','9']
        for word in words:
            if word[0] in nums:
                break

    if int(word) > 100:
        word == "100"
    elif int(word) < 0:
        word == "0"

    os.system('SetVol {}'.format(word))