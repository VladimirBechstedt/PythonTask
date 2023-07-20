'''
    Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
    Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''


def file_path(path):
    a = ''
    path_arr = path.split('\\')
    file_name = path_arr[len(path_arr) - 1].split('.')
    for i in range(0, len(path_arr) - 1):
        a += path_arr[i] + '\\'
    return (a, file_name[0], file_name[1])


path = 'C:\\Users\\Владимир\\Documents\\PythonTask\\citrys.txt'
print(file_path(path))