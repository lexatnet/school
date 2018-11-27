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

def tf(th):
    def f():
        th.forward(10)
    return f

def tb(th):
    def f():
        th.backward(10)
    return f

def tr(th):
    def f():
        th.right(10)
    return f

def tl(th):
    def f():
        th.left(10)
    return f


screen.onkey(tf(t), 'Up')
screen.onkey(tl(t), 'Left')
screen.onkey(tr(t), 'Right')
screen.onkey(tb(t), 'Down')
screen.listen()
input()