import os
file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(file_path)
import sys
sys.path.append(dir_path)

from func1 import func1
def some1():
    print('some1 is prints')
