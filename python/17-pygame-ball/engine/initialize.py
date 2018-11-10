import pygame

def initialize(state):
  pygame.init()
  state['screen']['instance'] = pygame.display.set_mode(
    (
      state['screen']['size']['width'],
      state['screen']['size']['height']
    )
  )
  for ball in state['balls']:
    ball['image'] = pygame.image.load(ball['image_path'])
    ball['rect'] = ball['image'].get_rect()
