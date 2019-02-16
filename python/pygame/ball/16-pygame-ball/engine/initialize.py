import pygame
import os

def initialize(state):
  pygame.init()
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
