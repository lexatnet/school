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


t.forward(30)
t.dot(30)
t.forward(30)
t.dot(30, 'red')
t.forward(30)
t.dot(30, '#ff6600')
t.forward(30)
t.dot(30, (0.2, 0.2, 0.2))


step = 60
radius = 30

t.home()
t.sety(step)
t.pendown()
t.circle(radius)
t.penup()

for i in range(3, 7):
    t.forward(step)
    t.pendown()
    t.circle(radius, steps=i)
    t.penup()


def stamp_range(t):
    stamps = []
    for i in range(0, 10):
        r = 0.1*((i+2)%10)  
        g = 0.1*((i+4)%10)
        b = 0.1*((i+6)%10)
        color = (r, g, b)
        t.color(color)
        stamp = t.stamp()
        stamps.append(stamp)
        t.forward(20)
    return stamps

t.home()
t.sety(-30)
stamp_range(t)



t.home()
t.sety(-60)
stamps = stamp_range(t)

for index, stamp in enumerate(stamps):
    if ((index%3)==0):
        t.clearstamp(stamp)

t.home()
t.sety(-90)
stamps = stamp_range(t)
t.clearstamps(len(stamps)//3)
t.clearstamps(-len(stamps)//3)

t.home()
t.sety(-120)
stamps = stamp_range(t)
t.undo()

t.home()
t.sety(-150)
undosize_before = t.undobufferentries()
stamps = stamp_range(t)
undosize_after = t.undobufferentries()
undosize_delta = undosize_after - undosize_before
for i in range(0, ((undosize_delta//3) - ((undosize_delta//3) % 3))):
    t.undo()


t.pensize(20)
t.penup()
t.pendown()


screen.exitonclick()
