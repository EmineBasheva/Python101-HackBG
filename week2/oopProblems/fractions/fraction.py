class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        if self.numerator == 1 and self.denominator == 1:
            return '1'
        elif self.numerator == 0:
            return '0'
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __simplify(self, the_smaller, the_greater):
        for i in range(2, the_smaller + 1):
            while the_smaller % i == 0 and the_greater % i == 0:
                the_smaller /= i
                the_greater /= i

        return int(the_smaller), int(the_greater)

    def simplification_fraction(self):

        if self.numerator < self.denominator:
            simple_fraction = self.__simplify(self.numerator, self.denominator)
        else:
            simple_fraction = self.__simplify(self.denominator, self.numerator)
        self.numerator = simple_fraction[0]
        self.denominator = simple_fraction[1]

    def __add__(self, other):
        result = Fraction(self.numerator * other.denominator + other.numerator * self.denominator, 
                        self.denominator * other.denominator)
        result.simplification_fraction()
        return result

    def __sub__(self, other):
        result = Fraction(self.numerator * other.denominator - other.numerator * self.denominator, 
                        self.denominator * other.denominator)
        result.simplification_fraction()
        return result

    def __mul__(self, other):
        result = Fraction(self.numerator * other.numerator, self.denominator * self.denominator)
        result.simplification_fraction()
        return result

    def __eq__(self, other):
        simple_self = self
        simple_self.simplification_fraction()
        simple_other = other
        simple_other.simplification_fraction()

        return simple_self.numerator == simple_other.numerator and simple_self.denominator == simple_other.denominator
