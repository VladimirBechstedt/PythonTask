import numpy as np


class Matrix:
    def __init__(self, *args):
        if self._check(args):
            self.arr = args
            self.y = len(args)
            self.x = len(args[0])
        else:
            raise AttributeError('Ошибка создании матрицы')

    def _check(self, arr):
        y = len(arr)
        x = len(arr[0])
        for i in range(y):
            if len(arr[i]) != x:
                return False
        return True

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return all([self.arr[i][j] == other.arr[i][j] for i in range(self.y) for j in range(self.x)])
        else:
            return False

    def __add__(self, other):
        if self.x == other.x and self.y == other.y:
            arr = []
            for i in range(self.y):
                arr.append([])
                for j in range(self.x):
                    arr[i].append(self.arr[i][j] + other.arr[i][j])
            return Matrix(*arr)
        else:
            raise IndexError('tuple index out of range')

    def __mul__(self, other):
        if self.x == other.y or self.x == other.x and self.y == other.y:
            arr = np.matmul(self.arr, other.arr)
            return Matrix(*arr)
        else:
            raise IndexError('tuple index out of range')

    def __str__(self):
        arr = ''
        for i in self.arr:
            for j in i:
                arr += f' {j}'
            arr += '\n'
        return arr


a = Matrix([1, 2, 3, 2], [1, 2, 3, 4], [1, 2, 3, 4], [54, 8, 9, 77])
b = Matrix([1, 2, 3, 6], [1, 2, 3, 7], [1, 2, 3, 9], [4, 5, 77, 1])

d = a * b
p = a + b
print(d == p)
print(d, p)
