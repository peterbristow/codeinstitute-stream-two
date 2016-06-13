from fractions import Fraction


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    return


class Fractions:
    def __init__(self, float_num):
        float_to_fraction = Fraction(float_num).limit_denominator()
        numerator, denominator = tuple(str(float_to_fraction).split('/', 2))
        numerator = int(numerator)
        denominator = int(denominator)
        common = gcd(numerator, denominator)
        self.num = numerator / common
        self.den = denominator / common

    def __repr__(self):  # representation method
        n, d = divmod(self.num, self.den)
        if n > 0:
            return '%s %s/%s' % (n, d, self.den)
        else:
            return '%s/%s' % (self.num, self.den)

    def __add__(self, other):
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Fractions(num, den)

    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Fractions(num, den)

    def __mul__(self, other):
        return Fractions(self.num * other.num, self.den * other.den)

    def __div__(self, other):
        return Fractions(self.num * other.den, self.den * other.num)

    def __gt__(self, other):
        return (self.num * other.den) > (self.den * other.num)

    def __lt__(self, other):
        return (self.num * other.den) < (self.den * other.num)

    def __eq__(self, other):
        return (self.num * other.den) == (self.den * other.num)

    def __ne__(self, other):
        return (self.num * other.den) != (self.den * other.num)


# f1 = Fractions(7,4)
# f2 = Fractions(2,4)
# f3 = f1 + f2
# print f3
# print f1
# print f2
#
# a = Fraction(0.185).limit_denominator()
# c, d = tuple(str(a).split('/', 2))
# print c
# print d

f1 = Fractions(0.185)
print f1