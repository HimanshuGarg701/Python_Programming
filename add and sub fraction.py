# making a class to add and subtract a fraction
class Fraction:
    def __init__(self, a, b, c, d):
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def sum(self):
        add = (self._a / self._b) + (self._c / self._d)
        print("The sum of numbers is: ", add)

    def diff(self):
        sub = (self._a / self._b) - (self._c / self._d)
        print("the difference of the numbers is: ", sub)


w = float(input("enter the numerator of first number"))
x = float(input("enter the denominator of first number"))
y = float(input("enter the numerator of second number"))
z = float(input("enter the denominator of second number"))
result = Fraction(w, x, y, z)
result.sum()
result.diff()
