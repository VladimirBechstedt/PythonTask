'''
    Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
    Функцию hex используйте для проверки своего результата.
'''

num = int(input('Введите число: '))
result1 = ''
result2 = hex(num)

while num != 0:
    a = num % 16
    if a >= 10:
        match a:
            case 10:
                result1 = 'a' + result1
            case 11:
                result1 = 'b' + result1
            case 12:
                result1 = 'c' + result1
            case 13:
                result1 = 'd' + result1
            case 14:
                result1 = 'e' + result1
            case 15:
                result1 = 'f' + result1
    else:
        result1 = str(a) + result1
    num //= 16
result1 = '0x' + result1

print(result1)
print(result1 == result2)