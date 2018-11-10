import pygame

def initialize(state):
  pygame.init()
  state['ball']['image'] = pygame.image.load(state['ball']['image_path'])
  state['ball']['rect'] = state['ball']['image'].get_rect()
  state['screen']['instance'] = pygame.display.set_mode(
    (
      state['screen']['size']['width'],
      state['screen']['size']['height']
    )
  )
