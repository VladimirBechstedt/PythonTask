'''
    Создайте функцию генератор чисел Фибоначчи
'''


def fibonacci(n):
    a = 0
    b = 1
    while n > 0:
        f = a + b
        a, b = b, f
        n -= 1
        yield f


for i in fibonacci(10):
    print(i)
