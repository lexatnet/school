from turtle import Turtle, Screen

# создадим черепаху и поместим ее в переменную, это поможет нам управлять этой черепахой
t = Turtle()

# можно создать несколько черепах например создадим ещё одну, и также присвоем её переменной
t2 = Turtle()

# библиотека содержит функцию `Screen` которая создаёт объект экрана
# этот оъект позволяет нам общаться с окном которое открыло наша программа а так же с экраном компьютера.
# это как мы увидим далее очень полезно.
screen = Screen()

# каждая черепаха оснащена пером которое будет оставлять след за ней если его не поднять
t.penup()
# можно поменять размер и цвет пера

shape = 'b.gif'
screen.register_shape(shape)
t.shape(shape)


# можно перемещать черепаху вперёд и назад
t.forward(50)
t2.backward(50)

# поворачивать ее на различные углы
# и делать множество полезных интересных и полезных вещей


# ознакомися с концепцией событийного програмирования

def tf(th,l):
    def f():
        th.setheading(90)
        th.forward(l)
    return f

def tb(th, l):
    def f():
        th.setheading(270)
        th.forward(l)
    return f

def tr(th, l):
    def f():
        th.setheading(0)
        th.forward(l)
    return f

def tl(th, l):
    def f():
        th.setheading(180)
        th.forward(l)
    return f


screen.onkey(tf(t, 20), 'Up')
screen.onkey(tl(t, 20), 'Left')
screen.onkey(tr(t, 20), 'Right')
screen.onkey(tb(t, 20), 'Down')
screen.listen()
screen.exitonclick()
