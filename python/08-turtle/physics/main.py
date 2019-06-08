from turtle import Turtle, Screen
import time

g = 9.8

# ((x1, y1), (x2, y2))

turtle_params = {
  'weght':10,
  'vector': ((0,0),(0,0))
}

def gravity(object):
  object['speed'] = object['speed'] + object['weight'] * g
  
  
def force(object):
  object['speed'] = object['speed'] + object['weight'] * g
  
def vector(v1, v2):
  v1[1][0] - v1[0][0]
  v2[1][0] - v2[0][0]
