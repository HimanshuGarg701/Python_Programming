# adding and subtracting 2 complex numbers using class
class Complex:
    def __init__(self, real1, img1, real2, img2):
        self._real1 = real1
        self._img1 = img1
        self._real2 = real2
        self._img2 = img2

    def sum(self):
        add_real = self._real1 + self._real2
        add_img = self._img1 + self._img2
        print("The sum of complex numbers is: ", add_real," + (",add_img, "i)")

    def sub(self):
        sub_real = self._real1 - self._real2
        sub_img = self._img1 - self._img2
        print("The difference of complex numbers is: ", sub_real, " + (", sub_img, "i)")


a = float(input("enter the real part of first number: "))
b = float(input("enter the imaginary part of first number: "))
c = float(input("enter the real part of second number: "))
d = float(input("enter the imaginary part of second number: "))
result = Complex(a, b, c, d)
result.sum()
result.sub()

