# для того чтобы сделать нашу программу более гибкой
# сделаем так что она сама будет искать файлы в директори в которой лежит файл программы

# импортируем библиотеку операционной системы
# в которой есть множество полезных функций для работы с директориями и файлами
import os

# специальная переменная `__file__` которая содержит имя текущего файла программы
# полное имя файла(абсолютный путь): тоесть путь до файла начиная от корня файловой системы
# в Windows это путь начинающийся с буквы диска. Например: C:\someDir\anotherDir\fileName
# можете посмотеть ее значение просто распечатав ее например как указано в следующей строке
# print('file name \'{}\''.format(__file__))

# Получим действительное имя файла(это на тот случай если используются ссылки на файл программы)
# мы получим именно имя исполняемого файла а не имя ссылки на файл
file_path = os.path.realpath(__file__)

# теперь откинем имя файла и получим имя дериктории в которой лежит файл
dir_path = os.path.dirname(file_path)

# определим как будет называться наша база данных
db_name = 'db.data'

# теперь можно состыковать имя деректории и имя файла базы данных и получить абсолютный путь до файла базы данных
# но лучше использовать другой вариант
#db_path = '{}\\{}'.format(dir_path, db_name)

# дело в том что в библиотеке есть специальная функция на такой случай
# она стыкует при помощи разделителя который используется в операционной системе все аргументы переданные в нее
# например:
# path = os.path.join('c:', 'someDir', 'anotherDir', 'fileName')
# print(path) # выведет C:\someDir\anotherDir\fileName
db_path = os.path.join(dir_path, db_name)

# теперь можно без проблем открыть файл базы даных передав абсолютный путь до неё
input_file = open(db_path,'r')
