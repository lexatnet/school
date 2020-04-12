
import os
file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(file_path)
import sys
sys.path.append(dir_path)

from initialize import initialize
from modify import modify
from render import render
from events import process_events
