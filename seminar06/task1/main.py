from check import check_date
from queen import check_queen, arrange_queen
from sys import argv

if __name__ == '__main__':
    print('Start')
    print(check_date(argv[1]))
    print('А сейчас на шахмотной доске будут в рандомных местах будут раставлены 8 ферзей и если они не будут рубить \
друг друга то на экране появиться надпись "Trye"')
    print(check_queen(arrange_queen()))
