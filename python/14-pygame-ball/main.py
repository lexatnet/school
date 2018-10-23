# Напишем простое графическое приложение в котором
# мяч будет "летать" по "ящику" отражаясь от его стенок
# как будто его кинули в каком-то направлении внутри "ящка"
# для этого нам необходимы две библиотеки:
# sys - для использования функции позволяющей принудительно завершить нашу программу
# pygame - 


import sys, pygame

# инициализируем библеотеку
pygame.init()

size = width, height = 768, 1024
# 
speed = [1, 1]
# 
black = 0, 0, 0

# 
screen = pygame.display.set_mode(size)

# 
ball = pygame.image.load("intro_ball.gif")
# 
ballrect = ball.get_rect()

# Опишем событийный цикл
# для этого используем бесконечный цикл
while 1:
    # 
    for event in pygame.event.get():
        # 
        if event.type == pygame.QUIT: sys.exit()

    # 
    ballrect = ballrect.move(speed)
    # 
    if ballrect.left < 0 or ballrect.right > width:
        # 
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        # 
        speed[1] = -speed[1]

    # Для начала отчистим экран от того что было нарисовано
    screen.fill(black)
    # 
    screen.blit(ball, ballrect)
    # 
    pygame.display.flip()
