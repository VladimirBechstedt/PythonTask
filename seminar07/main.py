import os


def counter(count):
    a = int('1' + '0' * count)
    for i in range(a):
        yield str((count - (len(str(i)))) * '0' + str(i))


def multiple_renaming(*, new_file_name, count, expansion_to, expansion_after, range_orig):
    num = counter(count)
    for i in os.listdir():
        if i.endswith(f'.{expansion_to}'):
            file_name = i[range_orig[0] - 1: range_orig[1]] + new_file_name + next(num) + '.' + expansion_after
            os.rename(i, file_name)
            print(file_name, i)


if __name__ == '__main__':
    multiple_renaming(new_file_name='newfile', count=4, expansion_to='txt', expansion_after='doc', range_orig=(3, 6))
