from turtle import Turtle, Screen
import time
from shapely.geometry import Polygon
from shapely.affinity import translate, rotate

screen = Screen()
screen.tracer(n=1000)

width = 300
height = 100
border = 10

def create_box_shape(shape_name, width, height, border):
  tmp = Turtle()
  reverse_width  = height
  reverse_height = width
  big_rect = build_rect(tmp, reverse_width, reverse_height, 0)
  small_rect = build_rect(tmp, reverse_width, reverse_height, border)
  tmp.penup()
  tmp.hideturtle()
  tmp.goto(big_rect['top']['x'], big_rect['top']['y'])
  tmp.pendown()
  tmp.begin_poly()

  tmp.goto(big_rect['top']['x'], big_rect['bottom']['y'])
  tmp.goto(big_rect['bottom']['x'], big_rect['bottom']['y'])
  tmp.goto(big_rect['bottom']['x'], big_rect['top']['y'])
  tmp.goto(big_rect['top']['x'], big_rect['top']['y'])

  tmp.goto(small_rect['top']['x'], small_rect['top']['y'])
  tmp.goto(small_rect['bottom']['x'], small_rect['top']['y'])
  tmp.goto(small_rect['bottom']['x'], small_rect['bottom']['y'])
  tmp.goto(small_rect['top']['x'], small_rect['bottom']['y'])
  tmp.goto(small_rect['top']['x'], small_rect['top']['y'])

  tmp.end_poly()
  p = tmp.get_poly()
  tmp.reset()
  tmp.hideturtle()
  del tmp
  screen.register_shape(shape_name, p)

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

def collision(t1,t2):
  p1 = get_polygon(t1)
  p2 = get_polygon(t2)
  if p1.intersects(p2):
    return True
  return False

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

create_box_shape('box', width, height, border)
screen.tracer(n=1)

ball = Turtle()
ball.shape('circle')
ball.color('red')
ball.penup()

box = Turtle()
box.shape('box')
box.setheading(30)

def tu(th,l):
  def f():
    pos = th.position()
    next_pos = (pos[0], pos[1] + l)
    th_shadow = th.clone()
    th_shadow.hideturtle()
    th_shadow.goto(next_pos[0], next_pos[1])
    if (not collision(box, th_shadow)):
      screen.tracer(n=1000)
      th.setheading(90)
      screen.tracer(n=1)
      th.goto(next_pos[0], next_pos[1])
    del th_shadow
  return f

def td(th, l):
  def f():
    pos = th.position()
    next_pos = (pos[0], pos[1] - l)
    th_shadow = th.clone()
    th_shadow.hideturtle()
    th_shadow.goto(next_pos[0], next_pos[1])
    if (not collision(box, th_shadow)):
      screen.tracer(n=1000)
      th.setheading(270)
      screen.tracer(n=1)
      th.goto(next_pos[0], next_pos[1])
    del th_shadow
  return f

def tr(th, l):
  def f():
    pos = th.position()
    next_pos = (pos[0] + l, pos[1])
    th_shadow = th.clone()
    th_shadow.hideturtle()
    th_shadow.goto(next_pos[0], next_pos[1])
    if (not collision(box, th_shadow)):
      screen.tracer(n=1000)
      th.setheading(0)
      screen.tracer(n=1)
      th.goto(next_pos[0], next_pos[1])
    del th_shadow
  return f

def tl(th, l):
  def f():
    pos = th.position()
    next_pos = (pos[0] - l, pos[1])
    th_shadow = th.clone()
    th_shadow.hideturtle()
    th_shadow.goto(next_pos[0], next_pos[1])
    if (not collision(box, th_shadow)):
      screen.tracer(n=1000)
      th.setheading(180)
      screen.tracer(n=1)
      th.goto(next_pos[0], next_pos[1])
    del th_shadow
  return f


screen.onkey(tu(ball, 5), 'Up')
screen.onkey(tl(ball, 5), 'Left')
screen.onkey(tr(ball, 5), 'Right')
screen.onkey(td(ball, 5), 'Down')
screen.listen()

screen.exitonclick()
