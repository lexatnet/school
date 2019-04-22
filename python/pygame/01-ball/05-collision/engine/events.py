import pygame, sys

def process_events(state):
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
