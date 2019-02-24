# Displaying details of a car
class Cars:
    def __init__(self, colour, type, price):
        self._colour = colour
        self._type = type
        self._price = price

    def display(self):
        print("The ", self._colour, " car is ", self._type, " type and costs Rs ", self._price)


car1 = Cars("red", "convertible", "10 lakh")
car2 = Cars("blue", "sedan", "6 lakh")
car1.display()
car2.display()
