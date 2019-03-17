from turtle import Turtle, Screen
import random

# Специально назову создаваемые нами объекты черепахи и экрана по одругому

c = Turtle()
d = Screen()
d.tracer(n=10, delay=100)

c.forward(200)
c.setheading(270)
c.forward(200)
c.setheading(180)
c.forward(200)
c.setheading(90)
c.forward(200)

for i in range(36):
    if(i == 0):
        c.penup()
        c.goto(10, -10)
        c.pendown()
        x, y = c.position()
    else:
        x = x + 20 + 10
        if( i%6 == 0):
            x = 10
            y = y - 20 - 10
    empty = random.choice([True, False])
    if(not empty):
        c.goto(x, y)
        c.pendown()
        c.setheading(0)
        c.forward(20)
        c.setheading(270)
        c.forward(20)
        c.setheading(180)
        c.forward(20)
        c.setheading(90)
        c.forward(20)
        c.penup()

d.exitonclick()
