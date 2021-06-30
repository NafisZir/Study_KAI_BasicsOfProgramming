import random
import threading
import time


def lst_print():
    print(lst_main)


def file():
    time.sleep(5)
    lst_main.sort()
    f = open('Laba7.txt', 'w')
    for i in lst_main:
        f.write(i + " ")
    f.close()


lst_main = []
str = ("q w e r t y u i o p a s d f g h j k l z x c v b n m Q W E R T Y U I O P A S D F G H J K L Z X C V B N M")
lst = str.split()
random.shuffle(lst)
i = 0
while i < 1:
    str2 = ''.join([random.choice(lst) for i in range(1, random.randint(2, 10))])
    lst_main.append(str2)
    x = threading.Thread(target=lst_print)
    time.sleep(0.5)
    x2 = threading.Thread(target=file)
    x2.start()
    x.start()


