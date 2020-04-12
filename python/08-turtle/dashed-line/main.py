from turtle import Turtle, Screen
from math import sin

t = Turtle()

s = Screen()

def dashed(th, x, y, lenght = 20):
  pos = th.pos()

  angle = th.towards(x, y)

  th.left(angle)

  is_pendown = True

  # th_shadow = th.clone()
  # th_shadow.hideturtle()

  while (th.distance(x, y) > lenght):
    th.forward(lenght)
    is_pendown = not is_pendown
    if is_pendown:
      th.pendown()
    else:
      th.penup()
  th.goto((x,y))

dashed(t, 300, 10)

s.exitonclick()
