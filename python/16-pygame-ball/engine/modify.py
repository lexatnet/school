def modify(state):
  ballrect = state['ball']['rect']
  speed = state['ball']['speed']
  width = state['box']['size']['width']
  height = state['box']['size']['height']
  ballrect = ballrect.move(speed)
  if ballrect.left < 0 or ballrect.right > width:
    speed[0] = -speed[0]
  if ballrect.top < 0 or ballrect.bottom > height:
    speed[1] = -speed[1]
  state['ball']['speed'] = speed
  state['ball']['rect'] = ballrect
