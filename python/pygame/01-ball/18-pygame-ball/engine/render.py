import pygame

def render(state):
  screen = state['screen']['instance']

  screen.fill(state['screen']['backgroud_color'])

  for ball in state['balls']:
    screen.blit(ball['image'], ball['rect'])

  pygame.display.flip()
