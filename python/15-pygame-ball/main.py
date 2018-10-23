import sys, pygame
pygame.init()

state = {
  'box':{
    'size':{
      'width': 768,
      'height': 1024
    }
  },
  'screen':{
    'size':{
      'width': 768,
      'height': 1024
    },
    'backgroud_color':(0, 0, 0)
  },
  'ball': {
    'image_path': "intro_ball.gif",
    'speed':[1, 1]
  }
}









def init_state(state):
  state['ball']['image'] = pygame.image.load(state['ball']['image_path'])
  state['ball']['rect'] = state['ball']['image'].get_rect()
  state['screen']['instance'] = pygame.display.set_mode(
    (
      state['screen']['size']['width'],
      state['screen']['size']['height']
    )
  )


def modify_state(state):
  ballrect = state['ball']['rect']
  state['ball']['rect'] = ballrect
  speed = state['ball']['speed']
  width = state['box']['size']['width']
  height = state['box']['size']['height']
  ballrect = ballrect.move(speed)
  if ballrect.left < 0 or ballrect.right > width:
    speed[0] = -speed[0]
  if ballrect.top < 0 or ballrect.bottom > height:
    speed[1] = -speed[1]
  state['ball']['speed'] = speed
  state['ball']['rect'] = ballrect


def render_state(state):
  ball = state['ball']['image']
  ballrect = state['ball']['rect']
  screen = state['screen']['instance']
  screen.fill(state['screen']['backgroud_color'])
  screen.blit(ball, ballrect)
  pygame.display.flip()


def process_events(state):
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()



init_state(state)


while 1:
  process_events(state)
  modify_state(state)
  print(state)
  render_state(state)
