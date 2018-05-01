# в питоне есть инстументы для асинхронного програмирования.

from asyncio import new_event_loop
import random

loop = new_event_loop()

loop2 = new_event_loop()

def make_loop(loopName, loop):
    def talk():
        phrases = ['bla', 'hello', 'bye']
        word = random.choice(phrases);
        print('{}:{}'.format(loopName, word))
        loop.call_later(2,talk)
    return talk

loop.call_later(2, make_loop('loop1', loop))

loop.run_forever()
