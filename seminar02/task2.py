'''
    Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
    Программа должна возвращать сумму и произведение* дробей.
    Для проверки своего кода используйте модуль fractions.
'''

num1 = input('Введите дробь: ')
num2 = input('Введите дробь: ')

num1 = num1.split('/')
num2 = num2.split('/')

a1 = int(num1[0])
b1 = int(num1[1])
a2 = int(num2[0])
b2 = int(num2[1])

a3 = a1 * a2
b3 = b1 * b2
result1 = str(a3) + '/' + str(b3)

b4 = b1 * b2
a4 = (a1 * b2) + (a2 * b1)
result2 = str(a4) + '/' + str(b4)
print(result1, result2)