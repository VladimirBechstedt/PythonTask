'''
    Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
    имена str, ставка int, премия str с указанием процентов вида «10.25%».
    В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
    Сумма рассчитывается как ставка умноженная на процент премии
'''

firstname = ['Anton', 'Iwan', 'Maxim']
bet = [15000, 16200, 35000]
percent = [10.25, 28.3, 42]
new_dict = {a: b * c / 100 for a, b, c in zip(firstname, bet, percent)}
print(new_dict)