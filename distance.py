# finding the distances using 2 coordinates
import math


class Distance:
    def __init__(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

    def dis(self):
        result = ((self._x2 - self._x1) + (self._y2 - self._y1))
        if result < 0:
            result = -result
            outcome = math.sqrt(result)
        elif result > 0:
            outcome = math.sqrt(result)

        print("The distance between the points is: ", outcome)


a = float(input("enter the x coordinate of first point: "))
b = float(input("enter the x coordinate of second point: "))
c = float(input("enter the y coordinate of first point: "))
d = float(input("enter the y coordinate of second point: "))
answer = Distance(a, b, c, d)
answer.dis()
