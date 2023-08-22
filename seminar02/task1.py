import unittest


class SquareEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.x1 = None
        self.x2 = None
        self.discriminant = None
        self.text = ""

    def roots(self):
        self.x1 = None
        self.x2 = None

        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    self.text = "уравнений имеет бесконечное число корней"
                else:
                    self.text = "ошибка записи уравнения"
            else:
                self.x1 = self.x2 = -self.c / self.b

        else:
            self.discriminant = self.b ** 2 - 4 * self.a * self.c
            if self.discriminant < 0:
                pass
            elif self.discriminant == 0:
                self.x1 = self.x2 = -self.b / (2 * self.a)

            else:
                self.x1 = (-self.b + self.discriminant ** 0.5) / (2 * self.a)
                self.x2 = (-self.b - self.discriminant ** 0.5) / (2 * self.a)


        return  self.x1, self.x2

class TestCaseNumbers(unittest.TestCase):
    def test_2(self):
        self.assertEqual(SquareEquation(1, -4, 4).roots(), (2 , 2), msg='Test failed')
    def test_3(self):
        self.assertEqual(SquareEquation(0, 0, 0).roots(), (None , None), msg='Test failed')
