from turtle import Turtle, Screen
import time
screen = Screen()
screen.tracer(n=1000)

width = 300
height = 100
border = 10


def create_box_shape(shape_name, width, height, border):
  tmp = Turtle()
  # tmp.speed(1)
  reverse_width  = height
  reverse_height = width
  big_rect = get_rect(tmp, reverse_width, reverse_height, 0)
  small_rect = get_rect(tmp, reverse_width, reverse_height, border)
  tmp.penup()
  tmp.hideturtle()
  tmp.goto(big_rect['top']['x'], big_rect['top']['y'])
  tmp.setheading(180)
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
  screen.register_shape(shape_name, p)

def in_box(pos_x, pos_y, top_x, top_y, bottom_x, bottom_y):
  print(pos_x, pos_y, top_x, top_y, bottom_x, bottom_y)
  print((pos_x > top_x), (pos_x < bottom_x), (pos_y < top_y), (pos_y > bottom_y))
  if(pos_x > top_x) and (pos_x < bottom_x) and (pos_y < top_y) and (pos_y > bottom_y):
    return True
  return False

def get_rect(t, width, height, border):
  pos = t.position()
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

create_box_shape('111', width, height, border)
screen.tracer(n=1)


ball = Turtle()
ball.shape('circle')
ball.color('red')
ball.penup()

box = Turtle()


box.shape('111')

def tu(th,l):
  def f():
    pos = th.position()
    print(pos)
    next_pos = (pos[0], pos[1] + l)
    print(next_pos)
    rect = get_rect(th, width, height, border)
    print(rect)
    if (
        in_box(
          next_pos[0],
          next_pos[1],
          rect['top']['x'],
          rect['top']['y'],
          rect['bottom']['x'],
          rect['bottom']['y']
        )
    ):
      screen.tracer(n=1000)
      th.setheading(90)
      screen.tracer(n=1)
      th.forward(l)
  return f

def td(th, l):
  def f():
    pos = th.position()
    next_pos = (pos[0], pos[1] - l)
    rect = get_rect(th, width, height, border)
    if (
        in_box(
          next_pos[0],
          next_pos[1],
          rect['top']['x'],
          rect['top']['y'],
          rect['bottom']['x'],
          rect['bottom']['y']
        )
    ):
      screen.tracer(n=1000)
      th.setheading(270)
      screen.tracer(n=1)
      th.forward(l)
  return f

def tr(th, l):
  def f():
    pos = th.position()
    next_pos = (pos[0] + l, pos[1])
    rect = get_rect(th, width, height, border)
    if (
        in_box(
          next_pos[0],
          next_pos[1],
          rect['top']['x'],
          rect['top']['y'],
          rect['bottom']['x'],
          rect['bottom']['y']
        )
    ):
      screen.tracer(n=1000)
      th.setheading(0)
      screen.tracer(n=1)
      th.forward(l)
  return f

def tl(th, l):
  def f():
    pos = th.position()
    next_pos = (pos[0] - l, pos[1])
    rect = get_rect(th, width, height, border)
    if (
        in_box(
          next_pos[0],
          next_pos[1],
          rect['top']['x'],
          rect['top']['y'],
          rect['bottom']['x'],
          rect['bottom']['y']
        )
    ):
      screen.tracer(n=1000)
      th.setheading(180)
      screen.tracer(n=1)
      th.forward(l)
  return f


screen.onkey(tu(ball, 10), 'Up')
screen.onkey(tl(ball, 10), 'Left')
screen.onkey(tr(ball, 10), 'Right')
screen.onkey(td(ball, 10), 'Down')
screen.listen()

screen.exitonclick()
