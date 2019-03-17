from turtle import Turtle, Screen
import random

s =  Screen()

s.tracer(10)

def hole(r, color):
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()    
    t.circle(r)
    t.end_fill()
    
def random_color():
    hexdig = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    return '#{}{}{}{}{}{}'.format(
        hexdig[random.randint(0, 15)],
        hexdig[random.randint(0, 15)],
        hexdig[random.randint(0, 15)],
        hexdig[random.randint(0, 15)],
        hexdig[random.randint(0, 15)],
        hexdig[random.randint(0, 15)]
    )

cheese_length = 300
cheese_height = 200
t = Turtle()

t.fillcolor(random_color())
t.begin_fill()
for i in range(2):
    t.forward(cheese_length)
    t.left(90)
    t.forward(cheese_height)
    t.left(90)
t.end_fill()

for i in range(50):
    t.penup()
    r = random.randint(5, 20)
    x = random.randint(0, cheese_length)
    y = random.randint(0, cheese_height)
    t.goto(x, y)
    if (
        (x-r)>0 
        and (y)>0 
        and (x+r)<cheese_length 
        and (y+2*r)<cheese_height
        ):
        hole(r, random_color())


s.exitonclick()
