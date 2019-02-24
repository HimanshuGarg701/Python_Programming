# finding the square of a number
class Square:
    def __init__(self, num):
        self._num = num

    def display(self):
        print("The square of the number is: ", self._num*self._num)


try:
    x = input("enter a number: ")
    if x.isdigit():
        x = int(x)
        y = Square(x)
        y.display()
    else:
        raise ValueError
except ValueError:
    print("You must enter a valid number")
