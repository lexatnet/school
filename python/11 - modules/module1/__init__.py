import os
file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(file_path)
import sys
sys.path.append(dir_path)

from mo2 import some1, func1
from func2 import func2
