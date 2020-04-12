import pygame, sys
gap = 20

def initialize(state):
  pygame.init()
  state['screen']['instance'] = pygame.display.set_mode(
    (
      state['screen']['size']['width'],
      state['screen']['size']['height']
    )
  )
  state['screen']['rect'] = pygame.Rect(
    0,
    0,
    state['screen']['size']['width'],
    state['screen']['size']['height']
  )
  state['box']['rect'] = pygame.Rect(
    0,
    0,
    state['box']['size']['width'],
    state['box']['size']['height']
  )
  for ball in state['balls']:
    ball['image'] = pygame.image.load(ball['image_path'])
    ball['rect'] = ball['image'].get_rect()
    other_balls = [item for item in state['balls'] if ((item != ball) and ('rect' in item.keys()))]
    for other_ball in other_balls:
      count = 0
      while True:
        count = count + 1
        if count > 1000 :
          break

        if (ball['rect'].colliderect(other_ball['rect'])):
          ball['rect'].left = other_ball['rect'].right + ball['rect'].width/2
          continue
        if (not state['box']['rect'].contains(ball['rect'])):
          ball['rect'].left = state['box']['rect'].left
          other_rects = [i['rect'] for i in other_balls]
          collisions_indexes = ball['rect'].collidelistall(other_rects)
          collisions = [other_balls[i] for i in collisions_indexes]
          bottoms = [item['rect'].bottom for item in collisions]
          if bottoms:
            ball['rect'].top = max(bottoms) + ball['rect'].height/2
          continue
        if not state['box']['rect'].contains(ball['rect']):
          print('Error: not enough place for ball in box.')
          sys.exit()
        break
  print('balls = {}'.format(state['balls']))

