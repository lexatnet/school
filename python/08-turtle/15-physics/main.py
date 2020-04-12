from turtle import Turtle, Screen
import time
from pdb import set_trace as bp
from lib import get_rectangle_poly, init_objects, processing, jump, g, draw_turtle_polygon, is_out

screen = Screen()
screen.tracer(n=10000)

shapes = [
  {
    'name': 'platform',
    'poly': get_rectangle_poly(500, 30)
  }
]

player = {
  'shape': 'circle',
  'color': 'red',
  'physics': {
    'weight':0.5,
    'speed': (0,0),
    'forces': [
    ]
  },
  'init_params':{
    'position': (0, 10)
  }
}

def fly(obj, collision):
  if collision != None:
    return []
  return [
    (0, g * obj['physics']['weight'])
  ]

def bounce(obj, collision):
  if collision == None:
    return []
  speed = collision['physics']['speed']
  return [
    (-speed[0]*.9, -speed[1]*.9)
  ]

objects = [
  player,
  {
    'shape': 'platform',
    'color': 'blue',
    'physics': {
      'weight':100,
      'speed': (0,0),
      'forces': [
        fly,
        bounce
      ]
    },
    'init_params':{
      'position': (-200, -100)
    }
  },
  {
    'shape': 'platform',
    'color': 'blue',
    'physics': {
      'weight':100,
      'speed': (0,0),
      'forces': [
        fly,
        bounce
      ]
    },
    'init_params':{
      'position': (400, -100)
    }
  }
]

for shape in shapes:
  screen.register_shape(shape['name'], shape['poly'])

screen.onkey(
  jump(
    player,
    (0, 10)
  ),
  'Up'
)

screen.onkey(
  jump(
    player,
    (-10, 5)
  ),
  'Left'
)

screen.onkey(
  jump(
    player,
    (10, 5)
  ),
  'Right'
)

init_objects(objects)
screen.listen()

while True:
  screen.tracer(n=10000)
  for obj in objects:
    processing(obj, objects)
  # for obj in objects:
  #   draw_turtle_polygon(obj['body'])
  # print(objects)
  if is_out(player['body'], (
      (-screen.window_width()/2, -screen.window_height()/2),
      (-screen.window_width()/2, screen.window_height()/2),
      (screen.window_width()/2, screen.window_height()/2),
      (screen.window_width()/2, -screen.window_height()/2)
  )):
    player['physics']['speed'] = (0, 0)
    player['body'].goto((player['init_params']['position']))
  screen.tracer(n=1)
  time.sleep(0.01)

