class Rational:
    def __init__(self, numerator: int, denominator: int):
        if isinstance(numerator, int) and isinstance(denominator, int):
            self.__numerator = numerator
            self.__denominator = denominator
            self.__normalise()
        else:
            raise TypeError('Numerator and denominator must be integers,')

    @property
    def get_denominator(self):
        return self.__denominator

    @property
    def get_numerator(self):
        return self.__numerator

    def __str__(self):
        return f'{self.__numerator} / {self.__denominator}'

    def __mul__(self, other: 'Rational') -> 'Rational':
        new_num = (self.__numerator * other.__numerator)
        new_den = (self.__denominator * other.__denominator)
        return Rational(numerator=new_num, denominator=new_den)

    def __truediv__(self, other: 'Rational') -> 'Rational':
        new_num = (self.__numerator * other.__denominator)
        new_den = (self.__denominator * other.__numerator)
        return Rational(numerator=new_num, denominator=new_den)

    def __add__(self, other: 'Rational') -> 'Rational':
        new_num = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        new_den = self.__denominator * other.__denominator
        return Rational(numerator=new_num, denominator=new_den)

    def __sub__(self, other: 'Rational') -> 'Rational':
        new_num = self.__numerator * other.__denominator - self.__denominator * other.__numerator
        new_den = self.__denominator * other.__denominator
        return Rational(numerator=new_num, denominator=new_den)

    def __eq__(self, other: 'Rational') -> bool:
        first_fraction = self.__numerator * other.__denominator
        second_fraction = self.__denominator * other.__numerator
        return first_fraction == second_fraction

    def __ne__(self, other: 'Rational') -> bool:
        return not self == other

    def __lt__(self, other: 'Rational') -> bool:
        first_fraction = self.__numerator * other.__denominator
        second_fraction = self.__denominator * other.__numerator
        return first_fraction < second_fraction

    def __gt__(self, other: 'Rational') -> bool:
        first_fraction = self.__numerator * other.__denominator
        second_fraction = self.__denominator * other.__numerator
        return first_fraction > second_fraction

    def __le__(self, other: 'Rational') -> bool:
        first_fraction = self.__numerator * other.__denominator
        second_fraction = self.__denominator * other.__numerator
        return first_fraction <= second_fraction

    def __ge__(self, other: 'Rational') -> bool:
        first_fraction = self.__numerator * other.__denominator
        second_fraction = self.__denominator * other.__numerator
        return first_fraction >= second_fraction

    @staticmethod
    def nod(a: int, b: int) -> int:
        """find GCD using the fast Euclidean algorithm"""
        if a < b:
            a, b = b, a

        while b != 0:
            a, b = b, a % b

        return a

    def __normalise(self):
        """reduce the fraction"""
        nod: int = Rational.nod(self.__numerator, self.__denominator)
        self.__numerator //= nod
        self.__denominator //= nod

        if self.__denominator < 0:
            self.__numerator = self.__numerator * -1,
            self.__denominator = self.__denominator * -1


if __name__ == '__main__':
    first_fract = Rational(10, 5)
    second_fract = Rational(7, 4)

    assert first_fract / second_fract == Rational(8, 7)
    assert first_fract * second_fract == Rational(7, 2)
    assert first_fract + second_fract == Rational(15, 4)
    assert first_fract - second_fract == Rational(1, 4)

    assert Rational(20, 4) == Rational(5, 1)
    assert Rational(12, 32) != Rational(2, 4)

    assert Rational(4, 6) < Rational(2, 1)
    assert Rational(6, 4) <= Rational(3, 2)
    assert Rational(8, 4) <= Rational(6, 3)

    assert Rational(3, 3) > Rational(2, 8)
    assert Rational(2, 5) >= Rational(2, 7)
    assert Rational(2, 7) >= Rational(2, 7)

    assert Rational(-10, -6) == Rational(10, 6)
    assert str(first_fract) == '2 / 1'

    a = Rational(1, 4)
    b = Rational(3, 2)
    c = Rational(1, 8)
    d = Rational(156, 100)
    assert a * (b + c) + d == Rational(1573, 800)
