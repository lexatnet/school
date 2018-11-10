def modify(state):
  width = state['box']['size']['width']
  height = state['box']['size']['height']
  for ball in state['balls']:
    ball['rect'] = ball['rect'].move(ball['speed'])
    if ball['rect'].left < 0 or ball['rect'].right > width:
      ball['speed'][0] = -ball['speed'][0]
    if ball['rect'].top < 0 or ball['rect'].bottom > height:
      ball['speed'][1] = -ball['speed'][1]
