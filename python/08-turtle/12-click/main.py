from turtle import Turtle, Screen
import time
screen = Screen()


def create_turtle(x, y):
  t = Turtle(visible=False)
  t.penup()
  t.goto(x, y)
  t.showturtle()

screen.onclick(create_turtle)

screen.mainloop()
