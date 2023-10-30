import unittest

from FourthQuestionsGroup import FactorialCalculator


class TestFactorialCalculator(unittest.TestCase):

    def test_positive_n(self):
        calculator = FactorialCalculator()
        calculator.calculate(5)
        factorials = calculator.get_factorials()
        self.assertEqual(factorials, [1, 1, 2, 6, 24])

    def test_zero_n(self):
        calculator = FactorialCalculator()
        calculator.calculate(0)
        factorials = calculator.get_factorials()
        self.assertEqual(factorials, [])

    def test_negative_n(self):
        calculator = FactorialCalculator()
        with self.assertRaises(ValueError):
            calculator.calculate(-3)

    def test_get_factorials_without_calculate(self):
        calculator = FactorialCalculator()
        with self.assertRaises(ValueError):
            calculator.get_factorials()


if __name__ == "__main__":
    unittest.main()
