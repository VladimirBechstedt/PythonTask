'''
    Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
    Используйте правило для проверки: «Число является простым,
    если делится нацело только на единицу и на себя».
    Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч
'''

number = int(input('Введите число от 0 до 100000: '))

while True:
    if 0 < number < 100000:
        for i in range(2, 99999):
            if number % i == 0 and i != number:
                print('Это составное число')
                break
            if i == number:
                print('Это простое число')
                break
        break
    number = int(input('Введите число от 0 до 100000: '))