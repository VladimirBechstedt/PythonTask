'''Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
'''


class Atm:
    def __init__(self, x, y):
        self.geodata = {'X': x,
                        'Y': y}
        self.opened = []
        self.FACTOR = 50
        self.WEALTH = 5_000_000
        self.PERCENTAGE_OF_WEALTH_TAX = 0.1
        self.PERCENTAGE_FOR_WITHDRAWAL = 0.015
        self.SUM_MIN = 30
        self.SUM_MAX = 600
        self.counter = {0: [],
                        1: [],
                        2: []}

    def come_in(self, client, password):
        if client not in self.opened:
            if client.verification(password):
                self.opened.append(client)
                self.counter[0].append(client)
                print(f'Добро пожаловать {client.firstname}')
            else:
                print('Не верный пароль')
        else:
            print('Вы уже вошли в систему')

    def come_out(self, client):
        if client in self.opened:
            self.opened.remove(client)
            for i in self.counter.keys():
                if client in self.counter[i]:
                    self.counter[i].remove(client)
            print(f'{client.firstname}, Вы вышли из системы')

    def _checking_for_multiplicity(self, credit):
        if credit % self.FACTOR == 0:
            return True
        else:
            return False

    def _checking_counter(self, client):
        if client in self.counter[0]:
            self.counter[0].remove(client)
            self.counter[1].append(client)
        elif client in self.counter[1]:
            self.counter[1].remove(client)
            self.counter[2].append(client)
        else:
            self.counter[2].remove(client)
            self.counter[0].append(client)
            client.cash = client.cash + int(client.cash * 0.3)

    def _wealth_tax(self, client):
        if client.cash > self.WEALTH:
            a = int(client.cash * self.PERCENTAGE_OF_WEALTH_TAX)
            client.cash -= a
            print(f'Налог на богатство составил {a}')

    def _check_range(self, credit):
        if self.SUM_MIN < credit < self.SUM_MAX:
            return True
        else:
            return False

    def _withdrawal_tax(self, credit):
        return int(credit * self.PERCENTAGE_FOR_WITHDRAWAL)

    def replenish(self, client):
        if client in self.opened:
            multiple = False
            credit = None
            while not multiple:
                credit = int(input(f'Введите сумму кратную {self.FACTOR}: '))
                multiple = self._checking_for_multiplicity(credit)
            client.cash += credit
            self._checking_counter(client)
            self._wealth_tax(client)
            print(f'{client.firstname}, денег на вашем счету: {client.cash}')
        else:
            print('Вы не вошли в систему операции с вашем счетом не возможны')

    def take_off(self, client):
        if client in self.opened:
            multiple = False
            credit = None
            while not multiple:
                credit = int(input(f'Введите сумму кратную {self.FACTOR} и не меньше {self.SUM_MIN} '
                                   f'и не больше {self.SUM_MAX}: '))
                multiple = self._checking_for_multiplicity(credit) and self._check_range(credit)
            client.cash = client.cash - credit - self._withdrawal_tax(credit)
            self._checking_counter(client)
            self._wealth_tax(client)
            print(f'{client.firstname}, денег на вашем счету: {client.cash}')
        else:
            print('Вы не вошли в систему операции с вашем счетом не возможны')


class Client:
    def __init__(self, name, lastname, age, cash, password):
        self.firstname = name
        self.lastname = lastname
        self.age = age
        self.cash = cash
        self.__password = password

    def verification(self, password):
        if self.__password == password:
            return True
        else:
            return False


class Customers:
    def __init__(self):
        self.arr_client = []


customers = Customers()
atm = Atm(54.929405, 71.267699)
customers.arr_client.append(Client('Петр', 'Петров', 25, 200_000_000, '1234'))
customers.arr_client.append(Client('Иван', 'Иванов', 40, 400_000, '5555'))
atm.come_in(customers.arr_client[0], '1234')
atm.come_in(customers.arr_client[1], '5555')
print(atm.opened)
atm.come_out(customers.arr_client[0])
print(atm.counter)
atm.replenish(customers.arr_client[0])
atm.replenish(customers.arr_client[1])
atm.take_off(customers.arr_client[1])
