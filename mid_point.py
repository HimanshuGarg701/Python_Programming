# finding the mid point between 2 points
class Point:
    def __init__(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

    def solving(self):
        solution1 = (self._x1 + self._y1)/2
        solution2 = (self._x2 + self._y2)/2
        print("The mid point of the 2 points is: (",solution1,",",solution2,")")


a = float(input("enter the x coordinate of first point"))
b = float(input("enter the y coordinate of first point"))
c = float(input("enter the x coordinate of second point"))
d = float(input("enter the y coordinate of second point"))
mid_point = Point(a, b, c, d)
mid_point.solving()
