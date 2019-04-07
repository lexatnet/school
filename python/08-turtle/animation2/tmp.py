from turtle import Turtle, Screen, Shape
t = Turtle()
t.width(10)
screen =  Screen()

radius = 100

extent = 120

width = 10

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

screen.register_shape('tmp', p3)


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

screen.register_shape('tmp2', p3)

t.shape('tmp2')


screen.exitonclick()
