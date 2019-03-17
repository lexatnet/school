# Начнём разбираться с простой графической
# библиотекой черепаха(turtle)
# для начала импортируем функцию
# которая создаёт черепаху
from turtle import Turtle, Screen

# создадим черепаху и поместим ее в переменную, это поможет нам управлять этой черепахой
t = Turtle()
screen = Screen()

t.forward(60)
t.left(60)
t.forward(60)
t.right(60)
t.backward(60)
t.goto(100,100)
t.setx(20)
t.sety(20)
t.setheading(180)
t.forward(60)
t.speed(1)
t.home()

t.setheading(275)
t.forward(123)

t.setheading(180)
t.forward(78)

t.dot()
t.setheading(50)
t.forward(38)

t.dot(20)
t.setheading(135)
t.forward(38)

t.dot(10, 'red')
t.setheading(180)
t.forward(38)

screen.exitonclick()
