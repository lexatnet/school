from prompt_toolkit.shortcuts.dialogs import button_dialog
import os

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
    bucket=[]

    while(True):
        create_shape = button_dialog(
            title='Create shape',
            text='Create new shape?',
            buttons=[
                ('Yes', True),
                ('No', False),
            ],
        )
        
        if not create_shape:
            break;
        
        color = button_dialog(
            title='Button dialog example',
            text='Are you sure?',
            buttons=[
                ('Red', 'red'),
                ('Green', 'green'),
                ('Blue', 'blue'),
            ],
        )
        
        values = [
            ('1', 1),
            ('2', 2),
            ('3', 3),
            ('4', 4),
            ('5', 5),
            ('6', 6),
            ('7', 7),
            ('8', 8),
        ]

        dimentions = button_dialog(
            title='Dimentions',
            text='Select shape dimentions:',
            buttons=values,
        )
        weight = button_dialog(
            title='Weight',
            text='Select shape weight:',
            buttons=values,
        )


        bucket.append((color, dimentions, weight)) #добавим шар в корзину
    return bucket;


def loadBucketFromFile(name):
    bucket = []
    
    file_path = os.path.realpath(__file__)
    dir_path = os.path.dirname(file_path)
    
    path = os.path.join(dir_path, name)

    if os.path.exists(path):
        file = open(path, 'r')
        for line in file:
            list = line.split(',')
            bucket.append((list[0],int(list[1]),int(list[2])))
        file.close()
    return bucket


def saveBucketItems(name, items):
    color = 0;
    dimentions = 1;
    weight = 2;
    file_path = os.path.realpath(__file__)
    dir_path = os.path.dirname(file_path)
    
    path = os.path.join(dir_path, name)

    if os.path.exists(path):
        file = open(path, 'a')
    else:
        file = open(path, 'w')
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
