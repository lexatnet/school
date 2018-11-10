def ball_to_box_collision(ball, box):
  return {
    'x': ball_to_box_collision_x(ball, box),
    'y': ball_to_box_collision_y(ball, box)
  }


def ball_to_box_collision_x(ball, box):
  width = box['size']['width']
  height = box['size']['height']
  if (ball['rect'].left < 0) or (ball['rect'].right > width):
    return True
  return False


def ball_to_box_collision_y(ball, box):
  width = box['size']['width']
  height = box['size']['height']
  if ball['rect'].top < 0 or ball['rect'].bottom > height:
    return True
  return False


def ball_to_ball_collision(ball_a, ball_b):
  return {
    'x': ball_to_ball_collision_x(ball_a, ball_b),
    'y': ball_to_ball_collision_y(ball_a, ball_b)
  }


def ball_to_ball_collision_x(ball_a, ball_b):
  interval_y = max(ball_a['rect'].bottom, ball_b['rect'].bottom) - min(ball_a['rect'].top, ball_b['rect'].top)
  coverage_y = ball_a['rect'].bottom - ball_a['rect'].top + ball_b['rect'].bottom - ball_b['rect'].top

  interval_x = max(ball_a['rect'].right, ball_b['rect'].right) - min(ball_a['rect'].left, ball_b['rect'].left)
  coverage_x = ball_a['rect'].right - ball_a['rect'].left + ball_b['rect'].right - ball_b['rect'].left

  if (
      (interval_y < coverage_y)
      and
      (interval_x < coverage_x)
  ):
    return True
  return False


def ball_to_ball_collision_y(ball_a, ball_b):
  interval_x = max(ball_a['rect'].right, ball_b['rect'].right) - min(ball_a['rect'].left, ball_b['rect'].left)
  coverage_x = ball_a['rect'].right - ball_a['rect'].left + ball_b['rect'].right - ball_b['rect'].left

  interval_y = max(ball_a['rect'].bottom, ball_b['rect'].bottom) - min(ball_a['rect'].top, ball_b['rect'].top)
  coverage_y = ball_a['rect'].bottom - ball_a['rect'].top + ball_b['rect'].bottom - ball_b['rect'].top
  if (
      (interval_x < coverage_x)
      and
      (interval_y < coverage_y)
  ):
    return True
  return False

def get_ball_to_balls_collisions(balls, ball):
  collisions = []
  print('ball = {}'.format(ball['rect']))
  for test_ball in balls:
    test_ball_collision = ball_to_ball_collision(ball, test_ball)
    print('here')
    if (test_ball_collision['x'] or test_ball_collision['y']):
      print('here 1')
      collisions.append(test_ball)
  return collisions
