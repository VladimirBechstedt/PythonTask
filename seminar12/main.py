import csv


class UserException(Exception):
    pass


class RangeError(UserException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Значение {self.value} выходит за пределы диапозона'


class UserNameError(UserException):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Имя пользователя {self.name} должно начинаться с заглавной буквы.\n' \
                f'И состоять только из букв.'


class StringNames:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.isalpha():
            raise UserNameError(value)
        if not value[0].isupper():
            raise UserNameError(value)


class Range:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise RangeError(value)
        if self.min_value is not None and value < self.min_value:
            raise RangeError(value)
        if self.max_value is not None and value > self.max_value:
            raise RangeError(value)


class Student:
    firstname = StringNames()
    patronymic = StringNames()
    lastname = StringNames()
    estimation = Range(2, 5)
    test = Range(0, 100)
    estimation_average = 0

    def __init__(self, firstname, patronymic, lastname):
        try:
            self.firstname = firstname
            self.patronymic = patronymic
            self.lastname = lastname
        except UserNameError as u:
            print(u)
            exit()
        self.discipline = self.discipline_dict('discipline.csv')

    def __repr__(self):
        return f'Student(name={self.firstname}, age={self.patronymic}, grade={self.lastname})'

    def discipline_dict(self, path):
        discipline = {}
        with open(path, 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.reader(f)
            next(csv_file)
            for line in csv_file:
                discipline[line[0]] = {'estimation': [[], 0.0],
                                       'test': [[], 0.0]}
        return discipline

    def add_estimation(self, discipline, rating):
        try:
            self.estimation = rating
        except RangeError as r:
            print(r)
            return
        self.discipline[discipline]['estimation'][0].append(self.estimation)
        self.average()

    def add_test(self, discipline, rating):
        try:
            self.test = rating
        except RangeError as r:
            print(r)
            return
        self.discipline[discipline]['test'][0].append(self.test)
        self.average()

    def average(self):
        sum_estimation_average = 0
        for key in self.discipline.keys():
            value = 0
            for i in self.discipline[key]['estimation'][0]:
                value += i
            if not value == 0:
                a = value / len(self.discipline[key]['estimation'][0])
                sum_estimation_average += a
                self.discipline[key]['estimation'][1] = a

        for key in self.discipline.keys():
            value = 0
            for i in self.discipline[key]['test'][0]:
                value += i
            if not value == 0:
                self.discipline[key]['test'][1] = value / len(self.discipline[key]['test'][0])

        self.estimation_average = sum_estimation_average / len(self.discipline.keys())


if __name__ == '__main__':
    student = Student('Владимир', 'Петрович', 'Бехштедт')
    student.add_estimation('физика', 400)
    student.add_estimation('физика', 3)
    student.add_estimation('физика', 2)
    student.add_test('физика', 2)
    student.add_test('физика', 1000)
    student.add_test('физика', 55)
    print(student.discipline)
    print(student.estimation_average)
