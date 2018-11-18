# Черепаха

Это библиотека позволяет создавать графические приложения.
И на первый взгляд простые концепции предоставляют мощьный инструментарий.



# Команды для черепашки

# Перемещение

forward() | fd() - движение вперёд

backward() | bk() | back() - движение назад

right() | rt() - поворот направо

left() | lt() - поворот налево

goto() | setpos() | setposition() - перемещение в позицию

setx() - устанавливаем позицию по координате - X

sety() - устанавливаем позицию

setheading() | seth()

home() - перемещение в начало координат

circle() - рисуем круг

dot() - рисуем точку

stamp() - ставим штамп

clearstamp()

clearstamps()

undo() - отменяем действие

speed() - устанавливаем скорость

# Узнаем состояние
position() | pos() - в какой позиции черепашка
towards() - узнаём угол между направлением черепашки и вектором от черепашки до точки с координатами 
xcor() - какая координата по оси
ycor() - какая координата по оси
heading() - узнаём ориентацию черепашки
distance() - определение расстояния от черепашки до точки с координатами

Setting and measurement
degrees()
radians()

# Управление пером
pendown() | pd() | down() - опускаем перо
penup() | pu() | up() - поднимаем перо
pensize() | width() - устанавливам ширину пера
pen() - возвращает словарь в котором определены настройки пера 
isdown() - узнаём опущено или поднято перо


# Управление цветом
color() - устанавливаем цвет
pencolor() - цвет пера
fillcolor() - цвет заливки
# Заливка цветом
filling()
begin_fill()
end_fill()

More drawing control
reset()
clear()
write()
# Turtle state
Visibility
showturtle() | st() - показываем черепашку
hideturtle() | ht() - скрываем черепашку
isvisible() - узнаём спрятана ли черепашка

# Внешний вид
shape() - форма черепашки
resizemode()
shapesize() | turtlesize()
shearfactor()
settiltangle()
tiltangle()
tilt()
shapetransform()
get_shapepoly()

# Использование событий
onclick()
onrelease()
ondrag()
# Специальные методы
begin_poly()
end_poly()
get_poly()
clone()
getturtle() | getpen()
getscreen()
setundobuffer()
undobufferentries()
# Методы экрана
Window control
bgcolor()
bgpic()
clear() | clearscreen()
reset() | resetscreen()
screensize()
setworldcoordinates()

# Комтролирование анимации
delay()
tracer()
update()

# Использование событие
listen() -
onkey() | onkeyrelease() - обрабатывам отпускание клавишы
onkeypress() - обрабатываем нажатие клавишы
onclick() | onscreenclick() - обрабатываем нажатие млавишы мышки на экране
ontimer() - устанавливаем таймер
mainloop() | done()

# Настройки
mode()
colormode()
getcanvas()
getshapes()
register_shape() | addshape()
turtles()
window_height()
window_width()

# Методы ввода
textinput()
numinput()

# Методы специфичные для экрана
bye()
exitonclick()
setup()
title()
