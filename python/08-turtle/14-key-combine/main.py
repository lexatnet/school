from turtle import Turtle, Screen
import time
screen = Screen()

t = Turtle('turtle')

def process_events():
    events = tuple(sorted(key_events))

    if events and events in key_event_handlers:
        (key_event_handlers[events])()

    key_events.clear()

    screen.ontimer(process_events, 200)

def up():
    key_events.add('UP')

def down():
    key_events.add('DOWN')

def left():
    key_events.add('LEFT')

def right():
    key_events.add('RIGHT')

def move_up():
    t.setheading(90)
    t.forward(25)

def move_down():
    t.setheading(270)
    t.forward(20)

def move_left():
    t.setheading(180)
    t.forward(20)

def move_right():
    t.setheading(0)
    t.forward(20)

def move_up_right():
    t.setheading(45)
    t.forward(20)

def move_down_right():
    t.setheading(-45)
    t.forward(20)

def move_up_left():
    t.setheading(135)
    t.forward(20)

def move_down_left():
    t.setheading(225)
    t.forward(20)

key_event_handlers = { \
    ('UP',): move_up, \
    ('DOWN',): move_down, \
    ('LEFT',): move_left, \
    ('RIGHT',): move_right, \
    ('RIGHT', 'UP'): move_up_right, \
    ('DOWN', 'RIGHT'): move_down_right, \
    ('LEFT', 'UP'): move_up_left, \
    ('DOWN', 'LEFT'): move_down_left, \
}

key_events = set()

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.listen()

process_events()

screen.mainloop()
