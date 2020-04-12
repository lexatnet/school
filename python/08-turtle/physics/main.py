from turtle import Turtle, Screen
import time
from functools import reduce
from shapely.geometry import Polygon, Point, LineString
from shapely.affinity import translate, rotate
from shapely.ops import nearest_points
from pdb import set_trace as bp

g = 9.8

screen = Screen()
# ((x1, y1), (x2, y2))

player = {
  'physics': {
    'weight':0.5,
    'speed': (0,0)
  },
  'init_params':{
    'position': (0, 10)
  }
}

platform = {
  'size': {
    'width': 100,
    'height': 10
  },
  'init_params':{
    'position': (0, 0)
  }
}

objects = [
  player,
  platform
]

def vector_sum(vectors):
  return reduce(lambda x, y: (x[0]+y[0], x[1]+y[1]), vectors)

def get_forces(obj, collisions):
  forces = []
  gravity = (0, -g * obj['physics']['weight'])
  forces.append(gravity)
  for o in collisions:
    if 'physics' not in o.keys():
      # resistence = -gravity
      # forces.append(resistence)
      return [(0,0)]
  return forces

def processing(obj, objects):
  collisions = get_collisions(obj, objects)
  forces = get_forces(obj, collisions)
  force = vector_sum(forces)
  speed = (force[0]/obj['physics']['weight'], force[1]/obj['physics']['weight'])
  obj['physics']['speed'] = speed
  current_position = obj['body'].position()
  next_position = (current_position[0]+speed[0], current_position[1]+speed[1])
  point_from = Point(current_position[0],current_position[1])
  point_to = Point(next_position[0],next_position[1])
  track = LineString(point_from, point_to)
  if 
  
  obj['body'].goto(next_position[0],next_position[1])


def get_collisions(obj, objects):
  collisions = []
  for o in objects:
    if o != obj:
      if collision(o['body'], obj['body']):
        collisions.append(o)
  return collisions

def get_polygon(t):
  pos = t.position()
  vert = t.get_shapepoly()
  heading = t.heading()
  print('vert {}'.format(vert))
  p = Polygon(vert)
  p = translate(p, xoff=pos[0], yoff=pos[1])
  p = rotate(p, 90+heading)
  print('polygon {}'.format(p))
  return p


def build_rect(t, width, height, border):
  top_x = -(width/2 - border)
  top_y = (height/2 - border)
  bottom_x = (width/2 - border)
  bottom_y = -(height/2 - border)
  return {
    'top': {
      'x': top_x,
      'y':top_y},
    'bottom': {
      'x':bottom_x,
      'y':bottom_y
    }
  }

def collision(t1,t2):
  p1 = get_polygon(t1)
  p2 = get_polygon(t2)
  if p1.intersects(p2):
    bp()
    return True
  return False

def get_platform_shape(platform):
  tmp = Turtle()
  height = platform['size']['height']
  width = platform['size']['width']
  reverse_width  = height
  reverse_height = width
  rect = build_rect(tmp, reverse_width, reverse_height, 0)
  tmp.penup()
  tmp.hideturtle()
  tmp.goto(rect['top']['x'], rect['top']['y'])
  tmp.pendown()
  tmp.begin_poly()

  tmp.goto(rect['top']['x'], rect['bottom']['y'])
  tmp.goto(rect['bottom']['x'], rect['bottom']['y'])
  tmp.goto(rect['bottom']['x'], rect['top']['y'])
  tmp.goto(rect['top']['x'], rect['top']['y'])

  tmp.end_poly()
  p = tmp.get_poly()
  tmp.reset()
  tmp.hideturtle()
  del tmp
  return p


screen.register_shape('platform', get_platform_shape(platform))

player['body'] = Turtle()
player['body'].hideturtle()
player['body'].penup()
player['body'].shape('circle')
player['body'].color('red')
player['body'].goto(player['init_params']['position'][0], player['init_params']['position'][1])
player['body'].showturtle()

platform['body'] = Turtle()
platform['body'].shape('platform')

def jump(player, force):
  def f():
    player['physics']['speed'] = vector_sum([
      player['physics']['speed'],
      force
    ])
  return f

screen.onkey(jump(player, (0, 40)), 'Up')

screen.listen()

while True:
  processing(player, objects)
  time.sleep(0.01)

