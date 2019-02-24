# Finding the area of a triangle using class
import math


class Triangle:
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
        self._semi_perimeter = 0

    def semi(self):
        self._semi_perimeter = (self._side1 + self._side2 + self._side3)/2
        area = math.sqrt((self._semi_perimeter)*(self._semi_perimeter-self._side1)
                         *(self._semi_perimeter-self._side2)*(self._semi_perimeter-self._side3))
        print("The area of the given triangle is", area)


a = int(input("enter the first side: "))
b = int(input("enter the second side: "))
c = int(input("enter the third side: "))
AREA = Triangle(a, b, c)
AREA.semi()

