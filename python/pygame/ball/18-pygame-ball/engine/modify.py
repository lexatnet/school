from collision import ball_to_box_collision, ball_to_ball_collision

def modify(state):
  for ball in state['balls']:
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


