from turtle import Turtle, Screen
import time
import datetime

t = Turtle()
t.hideturtle()
screen =  Screen()
screen.tracer(n=10, delay=100)
# exit_from_prog = False


# def pr():
#   print('exit')
#   exit = True

# screen.onkey(pr,'Escape')
# screen.listen()

while True:
  # if(exit):
  #   break
  t.reset()
  current_time = datetime.datetime.now()
  time_string = current_time.isoformat()
  t.write(time_string, font=("Arial", 20, "normal"))
  time.sleep(1)
