from collision import ball_to_box_collision, ball_to_ball_collision

def modify(state):
  for ball in state['balls']:
    allign_ball(ball, state)
    ball['rect'] = ball['rect'].move(ball['speed'])

    box_collision = ball_to_box_collision(ball, state['box'])

    if (box_collision['x']):
      ball['speed'][0] = -ball['speed'][0]
    if (box_collision['y']):
      ball['speed'][1] = -ball['speed'][1]

    other_balls =  [item for item in state['balls'] if item != ball]

    for other_ball in other_balls:
      ball_collision = ball_to_ball_collision(ball, other_ball)
      if (ball_collision['x']):
        ball['speed'][0] = -ball['speed'][0]
      if (ball_collision['y']):
        ball['speed'][1] = -ball['speed'][1]

def allign_ball(ball, state):
  box_collision = ball_to_box_collision(ball, state['box'])
  if (box_collision['x']):
    if ball['rect'].left < 0:
      ball['rect'].left = 0
    if ball['rect'].right > state['box']['size']['width']:
      ball['rect'].right = state['box']['size']['width']
  if (box_collision['y']):
    if ball['rect'].top < 0:
      ball['rect'].top = 0
    if ball['rect'].bottom > state['box']['size']['height']:
      ball['rect'].bottom = state['box']['size']['height']
