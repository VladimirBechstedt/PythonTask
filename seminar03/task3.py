'''
    Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
    Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
    Достаточно вернуть один допустимый вариант.
'''

LOAD_CAPACITY = 13
backpack = []
weight = 0
dictionary_of_things = {'Удочка': 2,
                        'Пакет': 1,
                        'Ложку': 2,
                        'Гриль': 3,
                        'Генератор': 4,
                        'Мясо': 3,
                        'Спички': 1}

for key, values in dictionary_of_things.items():
    if weight + values <= LOAD_CAPACITY:
        backpack.append(key)
        weight += values

print(backpack)