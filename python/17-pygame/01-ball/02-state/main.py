# Теперь немного модифицируем нашу программу используя знания полученные нами на предыдущих занятиях

# Разделим код на логически независимые части

# дело в том что наиболее удобным пердставляется схема приложения в которой есть:
# 1. Часть которая хранит состояние всей системы
# 2. Часть которая модифицирует состояние
# 3. Часть которая отображает состояние

import sys, pygame
pygame.init()

# сделаем словарь который будит ханить востояние системы в относительно удобном структурированном виде
state = {
  # сделаем поправку на то что коробка по которой летает наш неугомонный мяч может отличаться от размеров
  # видимой нами области через окно оа может быть как меньше так и больше неё
  'box':{
    'size':{ # поэтому зададим отдельно размер коробки
      'width': 200,
      'height': 200
    }
  },
  'screen':{
    'size':{ # и отдельно зададим размер окна
      'width': 300,
      'height': 300
    },
    'backgroud_color':(0, 0, 0)
  },
  'ball': { # соберём все данные о нашем мяче в одном разделе словаря
    'image_path': "intro_ball.gif",
    'speed':[1, 1]
  }
}


# Действия выполняюшиеся один единственный раз переред запуском событийного цикла так же можно сгруппировать
def init_state(state):
  import os
  file_path = os.path.realpath(__file__)
  dir_path = os.path.dirname(file_path)
  ball_image = os.path.join(dir_path, state['ball']['image_path'])
  state['ball']['image'] = pygame.image.load(ball_image)
  state['ball']['rect'] = state['ball']['image'].get_rect()
  state['screen']['instance'] = pygame.display.set_mode(
    (
      state['screen']['size']['width'],
      state['screen']['size']['height']
    )
  )

# Вынесим код который занимался перемещением мяча в отдельную функцию
def modify_state(state):
  # при упаковке кода в функции и наличии длинных имён или адресов данных к которым нам надо обратиться
  # становится удобным использование временных преременных которые вводятсяв основном для удобства и сокращеня записи
  # скопируем данные во временные преременные
  ballrect = state['ball']['rect']
  speed = state['ball']['speed']
  width = state['box']['size']['width']
  height = state['box']['size']['height']
  ballrect = ballrect.move(speed)
  if ballrect.left < 0 or ballrect.right > width:
    speed[0] = -speed[0]
  if ballrect.top < 0 or ballrect.bottom > height:
    speed[1] = -speed[1]
  # не забываем обновить изменённые данные так как мы работали с копиями надо теперь подменить ими оригиналы
  state['ball']['speed'] = speed
  state['ball']['rect'] = ballrect


# Так же вынесим код который отвечал за отображение в отдельную функцию
def render_state(state):
  # в данном случае тоже можно использовать временные переменные для удобства и для большей читабельности кода
  ball = state['ball']['image']
  ballrect = state['ball']['rect']
  screen = state['screen']['instance']
  screen.fill(state['screen']['backgroud_color'])
  screen.blit(ball, ballrect)
  pygame.display.flip()
  # так как на данном этапе мы не меняем состояние а просто отображаем его
  # то возвращать изменения из временных переменных нет необходимости


# Небольшой кусочек который обрабатывал события тоже можно поместить в отдельную функцию
def process_events(state):
  # в данную функцию мы тоже будем передавать состояние так как возможно оно нам пригодиться в будушем
  # но на данный момент использовать мы его никак не будим
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()


# не забудьте сохранить структуру программы вызвав соответствуюшие функции в необходимом порядке
init_state(state)
while 1:
  process_events(state)
  modify_state(state)
  render_state(state)
