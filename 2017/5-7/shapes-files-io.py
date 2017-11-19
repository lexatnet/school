# напишем программу которая использует текстовый файл для получения данныйх
# о том какие шары находятся в корзине
# будем испльзовать файл `shapes.data`
# для того чтобы считать данные из файла нам надо открыть его для чтения
inputFile = open('shapes.data', 'r')

# ведем переменных помошников которые нам помогут обращатся к полям наших кортежей в более понятной форме
# по сути они просто содержат номера полей в которых лежат данные
color = 0; # цвет
dimentions = 1; # диаметр
weight = 2; # вес

#введем ограничение на цвета шаров
#это поможет нам избежать ошибок при вводе
avalableColors = ['red', 'green', 'blue']


# теперь выведем содержимое файла
# перебирая все строки в файле по порядку
for line in inputFile:
    # разобьём строку с помощью разделителя `+`
    splited = line.split('+')
    # выведем информацию о каждом шаре из файла
    print('color={} dimentions={} weight={}'.format(splited[color],splited[dimentions],splited[weight]))

# после использования файлы необходимо закрывать
# чтобы избежать конфликтов при обращени к файлу из различных мест в программе
inputFile.close()

# Откроем файл для записи
# используем для этого ключ `a`
#  в этом случае информация будет дописываться в конец файла
outputFile = open('shapes.data', 'a')

# добавим возможность добавления новых шаров в бесконечном цикле
bucket=[]
while(True):
    color1 = input('введите цвет(red, green, blue):')
    # сделаем точку выхода из цикла
    # если пользователь программы не ввёл цвет то
    # это будет означать что он закончил ввод шаров
    if(len(color1) == 0): #для этого проверим длинну строки которую он ввёл
        print('выход из цикла ввода шаров')
        break # выйдем из цикла
    # проверим правильно ли введен цвет
    if not(color1 in avalableColors):
        print('неверный цвет')
        continue # если цвет не принадлежит массиву доступных цветов продолжим ввод шаров предположив что пользователь ошибся

    dimentions1 = input('введите размер(1,2,3,4,5,6):')
    if(len(dimentions1) == 0):
        print('нужно ввести размер очередной шар не создан выход из цикла')
        break
    weight1 = input('введите вес(1,2,3,4,5,6):')
    if(len(weight1) == 0):
        print('нужно ввести вес очередной шар не создан выход из цикла')
    # незабудем что мы ввели строковые данные и нам нужно преобразовать их в число
    weight1 = int(weight1)
    # добавим данные о щаре сразу определив кортеж (цвет, размер, вес)
    bucket.append((color1, int(dimentions1), weight1)) #добавим шар в корзину

# теперь запишем данные о новых шарах в файл
# для этого прелбразуем информацию о шарах в строки
# для каждого нового шара у нас будет новая строка
newLines = [] # переменная пустой лист которая будет накапливать строки которые мы допишем в файл
for i in range(0, len(bucket)):
    # берём очередной добавленный нами шар
    item = bucket.pop()
    # преобразуем данные о взятом шаре в строковое представление в файле
    # где каждый шар на новой строке(строки разделяются символом `\n` ) а значения разделены `+`
    str = '{}+{}+{}\n'.format(item[color],item[dimentions],item[weight])
    newLines.append(str)

# теперь запишем все новые строки в файл
outputFile.writelines(newLines)
# и закроем его
outputFile.close()
