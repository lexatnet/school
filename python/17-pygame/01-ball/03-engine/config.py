from engine import utils

state = {
  'box':{
    'size':{
      'width': 400,
      'height': 400
    }
  },
  'screen':{
    'size':{
      'width': 400,
      'height': 400
    },
    'backgroud_color':(0, 0, 0)
  },
  'ball': {
    'image_path': utils.source_path("intro_ball.gif"),
    'speed':[1, 1]
  }
}
