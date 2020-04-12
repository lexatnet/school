import os
file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(file_path)
import sys
sys.path.append(dir_path)

from utils import get_rectangle_poly, draw_turtle_polygon, is_out
from engine import processing, jump, init_objects, g
