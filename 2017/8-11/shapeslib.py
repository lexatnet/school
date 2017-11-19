def itemOutput(item):
	color = 0;
	dimentions = 1;
	weight = 2;
	print('shape color={} dimentions={} weight={}'.format(
		item[color],
		item[dimentions],
		item[weight]
		)
	)

def printBucket(bucket, bucketName):
	if (len(bucket) == 0): # проверяем пустая ли корзина
		print('{} is empty'.format(bucketName))
		return
	print('In {}'.format(bucketName))
	for i in range(0, len(bucket)):
		itemOutput(bucket[i])
	message = 'end of bucket {}'.format(bucketName)
	print(message)

def analyseBucket(bucket, redBucket, blueBucket):
    color = 0;
    dimentions = 1;
    weight = 2;
    for i in range(0, len(bucket)):
        item = bucket[i];
        if (item[color] == 'red'):
            redBucket.append(item)
        if ((item[color] == 'blue') and (item[weight] < 2)):
            blueBucket.append(item)

def getNewBucketItems():
    #введем ограничение на цвета шаров
    #это поможет нам избежать ошибок при вводе
    avalableColors = ['red', 'green', 'blue']

    bucket=[]

    while(True):
        color = input('введите цвет(red, green, blue):')
        # сделаем точку выхода из цикла
        # если пользователь программы не ввёл цвет то
        # это будет означать что он закончил ввод шаров
        if(len(color) == 0): #для этого проверим длинну строки которую он ввёл
            print('выход из цикла ввода шаров')
            break # выйдем из цикла
        # проверим правильно ли введен цвет
        if not(color in avalableColors):
            print('неверный цвет')
            continue # если цвет не принадлежит массиву доступных цветов продолжим ввод шаров предположив что пользователь ошибся

        dimentions = input('введите размер(1,2,3,4,5,6):')
        if(len(dimentions) == 0):
            print('нужно ввести размер очередной шар не создан выход из цикла')
            break
        weight = input('введите вес(1,2,3,4,5,6):')
        if(len(weight) == 0):
            print('нужно ввести вес очередной шар не создан выход из цикла')
        weight = int(weight)


        bucket.append((color, int(dimentions), weight)) #добавим шар в корзину
    return bucket;


def loadBucketFromFile(name):
    bucket = []
    file = open(name, 'r')
    for line in file:
        list = line.split(',')
        bucket.append((list[0],int(list[1]),int(list[2])))
    file.close()
    return bucket


def saveBucketItems(name, items):
    color = 0;
    dimentions = 1;
    weight = 2;
    file = open(name, 'a')
    lines = []
    for i in range(0, len(items)):
        str = '{},{},{}\n'.format(items[i][color], items[i][dimentions], items[i][weight])
        lines.append(str)
    file.writelines(lines)
    file.close()

def saveBucket(name, bucket):
    color = 0;
    dimentions = 1;
    weight = 2;
    file = open(name, 'a')
    lines = []
    for i in range(0, len(bucket)):
        item = bucket[i]
        str = '{},{},{}\n'.format(item[color], item[dimentions], item[weight])
        lines.append(str)
    file.writelines(lines)
    file.close()
