from turtle import Turtle, Screen
import time

t = Turtle()
t.hideturtle()
t.width(10)
screen =  Screen()
screen.tracer(n=10, delay=100)

full = 360

count = 0

def sec(count, frag):
  return (full / frag ) * (count % frag)


def sec2(count, frag):
  return full - sec(count, frag)


def delta(count, frag):
  return( 20 / frag ) * (count % frag)

while True:
  screen.tracer(n=10000)
  t.penup()
  t.home()
  t.clear()
  t.setx(-delta(count, 120))
  extent = sec(count, 120)
  t.circle(100, extent = extent)
  t.pendown()
  t.circle(100, extent = sec2(count, 120))
  t.forward(20)
  for i in range(0,2):
    t.circle(100)
    t.forward(20)
  t.circle(100, extent = extent)
  count = count+1
  screen.tracer(n=1)
  time.sleep(1/24)

screen.exitonclick()
