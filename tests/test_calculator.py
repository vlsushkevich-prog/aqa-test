import unittest
from calculator import calculator


class TestCalculator(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(calculator(1, 2, '+'),
                         3)
        self.assertEqual(calculator(-1, 1, '+'),
                         0)
        self.assertEqual(calculator(2.5, 2.5, '+'),
                         5)

    def test_sub(self):
        self.assertEqual(calculator(6, 1, '-'),
                         5)
        self.assertEqual(calculator(0, 0, '-'),
                         0)
        self.assertEqual(calculator(6.5, 6, '-'),
                         0.5)


    def test_mul(self):
        self.assertEqual(calculator(3, 3, '*'),
                         9)
        self.assertEqual(calculator(-9, 0, '*'),
                         0)
        self.assertEqual(calculator(-1.1, -10, '*'),
                         11)

    def test_div(self):
        self.assertEqual(calculator(18, 3, '/'),
                         6)
        self.assertEqual(calculator(12, 1.2, '/'),
                         10)
        self.assertEqual(calculator(18, -6, '/'),
                         -3)

    def test_div_zero(self):
        self.assertEqual(calculator(1, 0, '/'),
                         'Деление на ноль')
        self.assertEqual(calculator(-1, 0, '/'),
                         'Деление на ноль')
        self.assertEqual(calculator(0, 0, '/'),
                         'Деление на ноль')

    def test_unsupported_operator(self):
        self.assertEqual(calculator(1, 0, '&'),
                         'Неподдерживаемый оператор')
        self.assertEqual(calculator(1, 0, '!'),
                         'Неподдерживаемый оператор')
        self.assertEqual(calculator(1, 0, '%'),
                         'Неподдерживаемый оператор')

if __name__ == '__main__':
    unittest.main()