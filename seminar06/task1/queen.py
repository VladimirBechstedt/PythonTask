from random import randint


def arrange_queen():
    arr = [(randint(0, 7), randint(0, 7))]
    while len(arr) != 8:
        i = (randint(0, 7), randint(0, 7))
        if i not in arr:
            arr.append(i)
    return arr


# def chess_board(arr):
#     chess = []
#     for i in range(8):
#         chess.append([])
#         for j in range(8):
#             chess[i].append(0)
#
#     for i, j in arr:
#         chess[i][j] = 1
#
#     return chess


def check_queen(arr):
    for i in range(8):
        for j in range(i + 1, 8):
            if arr[i][0] == arr[j][0] or arr[i][1] == arr[j][1] or \
                    abs(arr[i][0] - arr[j][0]) == abs(arr[i][1] - arr[j][1]):
                return False

    return True
