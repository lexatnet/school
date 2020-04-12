def modify(state):
  for ball in state['balls']:
    if not state['box']['rect'].contains(ball['rect']):
      if (ball['rect'].left < state['box']['rect'].left):
        ball['rect'].left = state['box']['rect'].left
      if (ball['rect'].right > state['box']['rect'].right):
        ball['rect'].right = state['box']['rect'].right
      if (ball['rect'].top < state['box']['rect'].top):
        ball['rect'].top = state['box']['rect'].top
      if (ball['rect'].bottom > state['box']['rect'].bottom):
        ball['rect'].bottom = state['box']['rect'].bottom

    ball['rect'] = ball['rect'].move(ball['speed'])

    if (
        (ball['rect'].left < state['box']['rect'].left)
        or (ball['rect'].right > state['box']['rect'].right)
    ):
      ball['speed'][0] = -ball['speed'][0]
    if (
        (ball['rect'].top < state['box']['rect'].top)
        or (ball['rect'].bottom > state['box']['rect'].bottom)
    ):
      ball['speed'][1] = -ball['speed'][1]

    other_balls =  [item for item in state['balls'] if item != ball]

    for other_ball in other_balls:
      if not ball['rect'].colliderect(other_ball['rect']):
        continue
      if (
          (ball['rect'].left < other_ball['rect'].right)
          or (ball['rect'].right > other_ball['rect'].left)
      ):
        ball['speed'][0] = -ball['speed'][0]
      if (
          (ball['rect'].bottom > other_ball['rect'].top)
          or (ball['rect'].top < other_ball['rect'].bottom)
      ):
        ball['speed'][1] = -ball['speed'][1]


