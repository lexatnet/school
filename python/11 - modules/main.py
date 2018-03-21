# для лучшей оганизации кода в python используются модули
# модуль это набор файлов которые могут быть трактованы как библиотека
# так как лучший способ оъеденить файлы это положить их в одну папку
# именно поэтому модуль это дериктория с некоторыми особенностями
#  -- а именно : она содержит специальный файл __init__.py
#  именно этот файл и показывает Python что мы имеем дело с модулем
#  тоесть простейший путь создать модуль это создать директорию
#  с одним __init__.py файлом лежащем внутри

from module1 import some1, func1, func2

some1()
func1()
func2()
