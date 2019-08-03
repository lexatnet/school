from turtle import Turtle, Screen
import time
from functools import reduce

g = 9.8

# ((x1, y1), (x2, y2))

obj = {
  'position': (0, 0)
  'physics': {
    'weght':10,
    'speed': (0,0)
  },
}

platform1 = {
  'position': (0, 0)
}

def gravity(object):
  object['speed'] = object['speed'] + object['weight'] * g

def force(object):
  object['speed'] = object['speed'] + object['weight'] * g

def vector_sum(vectors):
  return reduce(lambda x, y: (x[0]+y[0], x[1]+y[1]), vectors)

ball = Turtle()
platform = Turtle()

def processing(t):
  collisions = get_collisions()
  get_forces


while True:
  processing(t)
  t.reset()
  current_time = datetime.datetime.now()
  time_string = current_time.isoformat()
  t.write(time_string, font=("Arial", 20, "normal"))
  time.sleep(1)


