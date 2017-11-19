inputFile = open('shapes.data', 'r')

# ведем переменных помошников которые нам помогут обращатся к полям наших кортежей в более понятной форме
# по сути они просто содержат номера полей в которых лежат данные
color = 0; # цвет
dimentions = 1; # диаметр
weight = 2; # вес

#введем ограничение на цвета шаров
#это поможет нам избежать ошибок при вводе
avalableColors = ['red', 'green', 'blue']

for line in inputFile:
    splited = line.split('+')
    print('color={} dimentions={} weight={}'.format(splited[color],splited[dimentions],splited[weight]))

inputFile.close()

outputFile = open('shapes.data', 'a')

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
    weight1 = int(weight1)


    bucket.append((color1, int(dimentions1), weight1)) #добавим шар в корзину

newLines = []

print(color);

for i in range(0, len(bucket)):
    item = bucket.pop()
    str = '{}+{}+{}\n'.format(item[color],item[dimentions],item[weight])
    newLines.append(str)

outputFile.writelines(newLines)
