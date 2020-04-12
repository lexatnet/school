from turtle import Turtle, Screen, Shape
import time

# t = Turtle()
# t.hideturtle()
# t.width(10)
screen =  Screen()
screen.tracer(n=100000, delay=100)

fragments = 120
full = 360
def sec(count, frag):
  return (full / frag ) * (count % frag)


def sec2(count, frag):
  return full - sec(count, frag)


def delta(count, frag):
  return( 20 / frag ) * (count % frag)

def create_raise_sector_shape(shape_name, radius, extent, width = 10):
  tmp = Turtle()
  tmp.hideturtle()
  tmp.setheading(90)
  tmp.begin_poly()
  tmp.circle(radius, extent = extent)
  tmp.end_poly()
  p1 = tmp.get_poly()
  tmp.reset()
  tmp.setheading(90)
  tmp.setx(-width)
  tmp.begin_poly()
  tmp.circle(radius - width, extent = extent)
  tmp.end_poly()
  p2 = tmp.get_poly()
  tmp.reset()
  p3 = p1 + p2[::-1]
  screen.register_shape(shape_name, p3)

def create_fall_sector_shape(shape_name, radius, extent, width = 10):
  tmp = Turtle()
  tmp.hideturtle()
  tmp.setheading(90)
  tmp.penup()
  tmp.circle(radius, extent = extent)
  tmp.begin_poly()
  tmp.pendown()
  tmp.circle(radius, extent = 360 - extent)
  tmp.end_poly()
  p1 = tmp.get_poly()
  tmp.reset()
  tmp.setheading(90)
  tmp.setx(-width)
  tmp.penup()
  tmp.circle(radius - width, extent = extent)
  tmp.begin_poly()
  tmp.pendown()
  tmp.circle(radius - width, extent = 360 - extent)
  tmp.end_poly()
  p2 = tmp.get_poly()
  tmp.reset()
  p3 = p1 + p2[::-1]
  screen.register_shape(shape_name, p3)



for i in range(0, fragments):
  extent = sec(i, fragments)
  create_raise_sector_shape('raise-sector-{}'.format(extent), 100, extent)
  create_fall_sector_shape('fall-sector-{}'.format(extent), 100, extent)



count = 0
ts = []
turtles_count = 4
step = 20

print(screen.getshapes())
screen.tracer(n=10, delay=100)

for i in range(turtles_count):
  t = Turtle()
  t.penup()
  # t.hideturtle()
  ts.append(t)

while True:
  extent = sec(count, fragments)
  for i in range(turtles_count):
    t = ts[i]
    t.setx((i * step) - delta(count, 120))
    if i == 0:
      t.shape('fall-sector-{}'.format(extent))
    elif i == (len(ts) - 1):
      t.shape('raise-sector-{}'.format(extent))
    else:
      t.shape('fall-sector-0.0')
  count = count+1
  time.sleep(1/60)

screen.exitonclick()
