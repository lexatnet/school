print('i\'m __init__.py of module2')
import os
file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(file_path)
import sys
sys.path.append(dir_path)


from func5 import func5
import submodule2

def func4():
    print('i\'m func4()')
