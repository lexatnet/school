from turtle import Turtle, Screen
import time
import datetime

t = Turtle()
t.hideturtle()
screen =  Screen()
screen.tracer(n=10, delay=100)


clock_radius = 100;

t.penup()
t.goto(0, - clock_radius)
t.pendown()
t.circle(clock_radius)
t.penup()
t.home()

def create_arrow_shape(shape_name, length, color):
  tmp = Turtle()
  tmp.hideturtle()
  tmp.color(color)
  tmp.begin_poly()
  tmp.setheading(90)
  tmp.forward(length)
  tmp.end_poly()
  p = tmp.get_poly()
  tmp.clear()
  screen.register_shape(shape_name, p)

create_arrow_shape('sec', 100, 'red')
create_arrow_shape('min', 60, 'red')
create_arrow_shape('hour', 40, 'red')


k_sec = 360/60
k_min = 360/(60*60)
k_hour = 360/(60*60*12)



secs = Turtle()
secs.shape('sec')
mins = Turtle()
mins.shape('min')
hours = Turtle()
hours.shape('hour')

def transform_orintation(deg):
  return 90 + (360 - deg)

while True:
  current_time = datetime.datetime.now()
  deg_sec = k_sec * current_time.second
  deg_min = k_min * (current_time.minute * 60 + current_time.second)
  deg_hour = k_hour * (current_time.hour * 60 * 60 + current_time.minute * 60 + current_time.second)
  secs.setheading(transform_orintation(deg_sec))
  mins.setheading(transform_orintation(deg_min))
  hours.setheading(transform_orintation(deg_hour))
  time.sleep(0.1)
