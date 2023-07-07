'''
    Программа загадывает число от 0 до 1000.
    Необходимо угадать число за 10 попыток.
    Программа должна подсказывать «больше» или «меньше» после каждой попытки.
'''

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
a = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

while a > 0:
    option = int(input('Ваш вариант'))
    if num == option:
        print('Вы отгадали')
        break
    elif num < option:
        print('меньше')
    else:
        print('больше')
    a -= 1