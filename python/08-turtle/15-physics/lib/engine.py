from turtle import Turtle
from utils import get_collisions, vector_sum, draw_turtle_polygon
from pdb import set_trace as bp

g = .4

def get_forces(obj, collisions):
  forces = []
  gravity = (0, -g * obj['physics']['weight'])
  forces.append(gravity)
  if ('physics' in obj.keys()) and ('forces' in obj['physics'].keys()):
    for f in obj['physics']['forces']:
      if callable(f):
        fs = f(obj, None)
        forces=[*forces, *fs]
      elif isinstance(f, tuple) and (len(f) == 2):
        forces.append(f)
      else:
        print('bad forces configuration for object', obj)
  for o in collisions:
    if ('physics' in o.keys()) and ('forces' in o['physics'].keys()):
      for f in o['physics']['forces']:
        if callable(f):
          fs = f(o, obj)
          # bp()
          forces+=fs
        elif isinstance(f, tuple) and (len(f) == 2):
          forces.append(f)
        else:
          print('bad forces configuration for object', o)

  return forces

def processing(obj, objects):

  collisions = get_collisions(obj, objects)

  forces = get_forces(obj, collisions)

  force = vector_sum(forces)

  speed = (
    obj['physics']['speed'][0]+force[0]/obj['physics']['weight'],
    obj['physics']['speed'][1]+force[1]/obj['physics']['weight']
  )

  obj['physics']['speed'] = speed

  current_position = obj['body'].position()

  next_position = (
    current_position[0]+speed[0],
    current_position[1]+speed[1]
  )

  # point_from = Point(current_position[0], current_position[1])
  # point_to = Point(next_position[0], next_position[1])
  # track = LineString(point_from, point_to)

  obj['body'].goto(next_position[0], next_position[1])

def init_objects(objects):
  for obj in objects:
    obj['body'] = Turtle()
    obj['body'].hideturtle()
    obj['body'].penup()
    obj['body'].goto(
      obj['init_params']['position'][0],
      obj['init_params']['position'][1]
    )
    obj['body'].shape(obj['shape'])
    obj['body'].color(obj['color'])
    obj['body'].showturtle()

def jump(player, force):
  def f():
    player['physics']['speed'] = vector_sum([
      player['physics']['speed'],
      # сила прыжка
      force
    ])
  return f
