# рассмотрим очень удобный тип данных под названием словари(dictionaries)
# он немного похож на листы(lists) рассмотренные ранее
# удобным в нем является то что ключами могут являтся значения различных типов данных
# словари(dictionaries) это изменяемый тип данных
# это значит что можно поменять данные на которые указывает ключь в словаре этим они похожи на списки(lists)
# и непохожи на кортежи в которых данные под ключами менять нельзя


# словарь можно определить с помощью фигурных скобок
# например пустой словарь можно объявить следующим образом
someData = {}

print('empty dictionary {}'.format(someData))

# теперь добавим в него данные
someData['someKey'] = 'someValue'

print('after add key:value pair {}'.format(someData))

# определим словарь содержащий несколько ключей
# словарь состоит из пар - ключ:значение разделённых двоеточием
# сами пары разделены запятой
someoOtherData = {
    'key1': 1, # ключами могут быть строковые значения
    'key2': 'someValue', # сами значения могут быть тоже различными
    1: 3.4, # как видим ключами могут быть целые числа как в списках
    'example': {} # а в этом случае значением является пустой словарь
}

# словари могут использоваться вместе с другими типами данных и образовыать довольно сложные структуры которые удобно читать
user = {
    'id':1,
    'name':'Peter',
    'friends':[
        {
            'id':2,
            'name':'Ivan'
        },
        {
            'id':3,
            'name':'Jenya'
        }
    ],
    'mom':{
        'name':'Yuliya'
    },
    'dad':{
        'name':'Sergey'
    },
    'attributes':{}
}

# можно получить список ключей которые есть в словаре
fields=list(user.keys())

# поменять данные можно обратившись к ним с помощью цепочки ключей
user['friends'][0]['name'] = 'Fedor'

# выведем в консоль список ключей
print('user keys -> {}'.format(fields))

# или например в цикле выведем все значения которые лежат по ключам
for field in fields:
    print('({}) -> ({})'.format(field, user[field]))