import os
from json_file import writing as j
from csv_file import writing as c
from pickle_file import writing as p


def parent_directory(dir_path):
    dir_path = dir_path.split('\\')
    return dir_path[-2]


def size(dir_path):
    return os.path.getsize(dir_path)


def dir_size(start_path):
    total_size = 0
    for dir_path, dir_name, file_name in os.walk(start_path):
        for f in file_name:
            fp = os.path.join(dir_path, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


def bypass(path):
    arr = []
    for dir_path, dir_name, file_name in os.walk(path):
        arr.append([dir_path, parent_directory(dir_path), False, True, dir_size(dir_path)])
        for a in map(lambda i: dir_path + '\\' + i, file_name):
            arr.append([a, parent_directory(a), True, False, size(a)])
    return arr


if __name__ == '__main__':
    array = bypass(r'C:\Users\Владимир\Documents\проекты в питоне\PythonTask')
    j(array)
    c(array)
    p(array)
