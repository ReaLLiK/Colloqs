import math


class FactorialCalculator:
    def __init__(self):
        self.factorials = None

    def calculate(self, n):
        if n < 0:
            raise ValueError("n должно быть неотрицательным числом")

        self.factorials = [math.factorial(i) for i in range(n)]

    def get_factorials(self):
        if self.factorials is None:
            raise ValueError("Факториалы еще не рассчитаны. Вызовите метод calculate() сначала.")
        return self.factorials


def main():
    calculator = FactorialCalculator()
    try:
        n = 5
        calculator.calculate(n)
        factorials = calculator.get_factorials()
        print(f"Первые {n} факториалов: {factorials}")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
