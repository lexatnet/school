from engine import utils

state = {
  'box':{
    'size':{
      'width': 500,
      'height': 600
    }
  },
  'screen':{
    'size':{
      'width': 800,
      'height': 600
    },
    'backgroud_color':(0, 0, 0)
  },
  'balls': [
    {
      'image_path': utils.source_path('intro_ball.gif'),
      'speed':[1, 1]
    },
    {
      'image_path': utils.source_path('intro_ball.gif'),
      'speed':[2, 1]
    }
  ]
}
