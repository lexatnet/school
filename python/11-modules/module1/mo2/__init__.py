import os
file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(file_path)
import sys
sys.path.append(dir_path)

from func1 import func1

# если написать в этом файле функцию или импортировать ее из другого модуля или библиотеки
# то ее можно будет импортировать из текушего модуля
def some1():
    print('some1 is prints')
