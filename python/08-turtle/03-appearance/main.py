from turtle import Turtle, Screen


# библиотека содержит функцию `Screen` которая создаёт объект экрана
# этот оъект позволяет нам общаться с окном которое открыло наша программа а так же с экраном компьютера.
# это как мы увидим далее очень полезно.
screen = Screen()

gap = 60
step = 100
canvwidth, canvheight = screen.screensize()
screen.setworldcoordinates(0 - gap, 0 - gap, (canvwidth*2 - gap), (canvheight*2 - gap))


predefined_shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']

turtles = []
for index, shape in enumerate(predefined_shapes):
    turtle  = Turtle()
    turtle.penup()
    turtle.sety(gap*index)
    turtle.shape(shape)
    turtles.append(turtle)

t = Turtle()
t.home()
t.left(150)
t.begin_poly()
for i in range(1, 4):
    t.fd(20)
    t.right(60)
    t.fd(20)
    t.left(300)

t.setheading(90)
t.speed(1)
t.fd(20)
t.right(60)
t.fd(20)
t.left(120)
t.fd(20)
t.left(60)
t.fd(20)
t.left(120)
t.fd(20)
t.right(60)
t.fd(20)
t.right(120)
t.fd(20)
t.right(60)
t.fd(20)
t.right(120)
t.fd(20)
t.end_poly()
p = t.get_poly()
t.reset()
shape = 'myShape'
screen.register_shape(shape, p)
t.penup()
t.sety(len(turtles)*gap)
t.shape(shape)
turtles.append(t)

import os
file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(file_path)
shape = os.path.join(dir_path, 'b.gif')
screen.register_shape(shape)
t = Turtle()
t.penup()
t.sety(len(turtles)*gap)
t.shape(shape)
turtles.append(t)

new_turtles = []
for turtle in turtles:
    new_turtle = turtle.clone()
    new_turtle.setx(step)
    new_turtle.pendown()
    new_turtle.stamp()
    new_turtle.forward(step*2)
    new_turtle.shapesize(2, 2, 2)
    new_turtle.stamp()
    new_turtle.forward(step*2)
    new_turtle.shearfactor(1)

screen.exitonclick()
