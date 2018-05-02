print('i\'m __init__.py of submodule2')
import os
file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(file_path)
import sys
sys.path.append(dir_path)

from func7 import func7

def func6():
    print('i\'m func6()')
