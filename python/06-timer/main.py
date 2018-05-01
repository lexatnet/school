from threading import Timer
from time import sleep
def hello():
    print("hello, world")

t = Timer(30.0, hello)
t.start() # after 30 seconds, "hello, world" will be printed
print('program statrted')
