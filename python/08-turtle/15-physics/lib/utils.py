from turtle import Turtle
from shapely.geometry import Polygon, Point, LineString
from shapely.affinity import translate, rotate
from shapely.ops import nearest_points
from functools import reduce

def get_collisions(obj, objects):
  collisions = []
  for o in objects:
    if o != obj:
      if collision(o['body'], obj['body']):
        collisions.append(o)
  return collisions

def draw_polygon(polygon):
  tmp = Turtle()
  tmp.hideturtle()
  tmp.pensize(10)
  # tmp.penup()
  tmp.color('green')
  for pos in polygon.exterior.coords:
    tmp.goto(pos)

def draw_turtle_polygon(t):
  draw_polygon(get_polygon(t))

def get_polygon(t):
  pos = t.position()
  vert = t.get_shapepoly()
  heading = t.heading()
  # print('vert {}'.format(vert))
  p = Polygon(vert)
  p = translate(p, xoff=pos[0], yoff=pos[1])
  p = rotate(p, 90+heading)
  # print('polygon {}'.format(p))
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

def get_rectangle_poly(width,height):
  tmp = Turtle()
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

def vector_sum(vectors):
  return reduce(lambda x, y: (x[0]+y[0], x[1]+y[1]), vectors)

def collision(t1,t2):
  p1 = get_polygon(t1)
  p2 = get_polygon(t2)
  if p1.intersects(p2):
    return True
  return False

def is_out(turtle, bounds):
  p1 = get_polygon(turtle)
  p2 = Polygon(bounds)
  if p1.intersects(p2):
    return False
  return True
