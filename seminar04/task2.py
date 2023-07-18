'''
    Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
    где ключ — значение переданного аргумента, а значение — имя аргумента.
    Если ключ не хешируем, используйте его строковое представление.
'''


def to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result


print(to_dict(name='Владимир', age=25, speed=24.38))
