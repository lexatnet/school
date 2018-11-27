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



#t.circle(60, steps=6)
t.color("blue")
t.stamp()
t.forward(60)

screen.exitonclick()
