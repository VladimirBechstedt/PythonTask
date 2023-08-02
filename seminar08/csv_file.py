import csv


def writing(arr):
    line = ['absolute_path', 'parent_directory', 'file', 'directory', 'size']
    with open('new_biostats.csv', 'a', newline='', encoding='utf-8') as f_write:

        csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow(line)
        csv_write.writerows(arr)
