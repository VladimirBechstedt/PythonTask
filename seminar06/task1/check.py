__mont_dict = {31:[1, 3, 5, 7, 8, 10, 12], 30:[4, 6, 9, 11]}


def check_date(inp_year):
    day, month, year = map(int, inp_year.split('.'))

    if 0 < day < 32 and 0 < month < 13 and 0 < year < 10000:
        if month != 2:
            if day in __mont_dict:
                return month in __mont_dict[day]
            else:
                return True
        else:
            if _check_year(year):
                return day < 29
            else:
                return day < 30


def _check_year(year):
    if year < 1582 or year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        return True
    else:
        return False



