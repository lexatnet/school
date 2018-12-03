from turtle import Turtle, Screen

screen = Screen()

screen.bgcolor('green')
screen.screensize(100, 100)

screen_width, screen_height = screen.screensize()
screen.setworldcoordinates(0, 0, screen_width, screen_height)

t = Turtle()

t.goto(screen_width//2, screen_height//2)

screen.exitonclick()
