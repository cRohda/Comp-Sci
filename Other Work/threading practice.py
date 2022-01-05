import threading
from time import sleep

def function1():
    a = 1
    while a < 1000:
        print(a)
        a += 2
        sleep(0.3)

def function2():
    sleep(0.1)
    b = 2
    while b < 1000:
        print(b)
        b += 2
        sleep(0.3)

x = threading.Thread(target=function1)
y = threading.Thread(target=function2)

x.start()
y.start()