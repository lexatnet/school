import pygame

def render(state):
  ball = state['ball']['image']
  ballrect = state['ball']['rect']
  screen = state['screen']['instance']
  screen.fill(state['screen']['backgroud_color'])
  screen.blit(ball, ballrect)
  pygame.display.flip()
