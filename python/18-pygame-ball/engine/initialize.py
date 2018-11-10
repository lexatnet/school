import pygame, sys
from collision import ball_to_box_collision, ball_to_ball_collision, get_ball_to_balls_collisions
gap = 20

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
    other_balls = [item for item in state['balls'] if ((item != ball) and ('rect' in item.keys()))]
    print('other rects = {}'.format([b['rect'] for b in other_balls]))
    print('other rects right = {}'.format([b['rect'].right for b in other_balls]))
    for other_ball in other_balls:
      count = 0
      while True:
        print('other rect = {}'.format(other_ball['rect']))
        count = count + 1
        if count > 1000 :
          break

        ball_collision = ball_to_ball_collision(ball, other_ball)
        box_collision = ball_to_box_collision(ball, state['box'])

        if (ball_collision['x']):
          print('move right')
          print('other rect right = {}'.format(other_ball['rect'].right))
          print('ball rect before = {}'.format(ball['rect']))
          ball['rect'].x = other_ball['rect'].right
          print('ball rect after = {}'.format(ball['rect']))
          continue
        if (box_collision['x']):
          ball['rect'].x = 0
          print('move down')
          collisions = get_ball_to_balls_collisions(other_balls, ball)
          bottom_collisions = max([item['rect'].bottom for item in collisions])
          ball['rect'].y = bottom_collisions
          continue
        if (box_collision['y']):
          print('Error: not enough place for ball in box.')
          sys.exit()
        break
  print('balls = {}'.format(state['balls']))

