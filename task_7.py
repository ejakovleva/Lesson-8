class Complex:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return Complex(self.num_1 + other.num_1, self.num_2 + other.num_2)

    def __mul__(self, other):
        return Complex(self.num_1 * other.num_1 - self.num_2 * other.num_2, self.num_1 * other.num_2 + self.num_2 *
                       other.num_1)

    def __str__(self):
        return f"{self.num_1}{f'{self.num_2}j' if self.num_2 != 0 else ''}"


complex_1 = Complex(9, -8)
complex_2 = Complex(10, 1)
complex_3 = Complex(8, 1)
print(complex_1 + complex_2 + complex_3)
print(complex_1 * complex_2)
