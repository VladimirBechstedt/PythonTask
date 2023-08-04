import csv
from random import randint


def generator_csv(a, b):
    arr = []
    for _ in range(1000):
        arr.append([randint(a, b), randint(a, b), randint(a, b)])
    line = ['a', 'b', 'c']
    with open('numbers.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow(line)
        csv_write.writerows(arr)


generator_csv(1, 100)


def substitution(func):
    def wrapper():
        res = []
        with open('numbers.csv', 'r', newline='') as f:
            csv_file = csv.reader(f, dialect='excel-tab')
            next(csv_file)
            for line in csv_file:
                l = list(map(int, line[0].split(' ')))
                result = func(l[0], l[1],  l[2])
                res.append(result)
        print(res)
        return res
    return wrapper()


@substitution
def quadratic_equation(a, b, c):
    d = b**2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        res = -b / (2 * a)
        return res
    else:
        x1 = -b - (d**0.5) / (2 * a)
        x2 = (-b + (d ** 0.5)) / (2 * a)
        res = (x1, x2)
        return res


if __name__ == '__main__':

    print(quadratic_equation)

