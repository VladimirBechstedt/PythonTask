'''
    Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
    В результирующем списке не должно быть дубликатов.
'''

arr = [5, 4, 5, 7, 12, 9, 4]
arr2 = []

for x in arr:
    if arr.count(x) > 1 and x not in arr2:
        arr2.append(x)

print(arr, arr2, sep='\n')