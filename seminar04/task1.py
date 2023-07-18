'''
    Напишите функцию для транспонирования матрицы
'''


def matrix_transposition(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                break
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    return arr


matrix = [[5, 6, 7, 8],
          [7, 8, 1, 9],
          [2, 6, 7, 2],
          [5, 5, 2, 1]]

print(matrix)
print(matrix_transposition(matrix))
