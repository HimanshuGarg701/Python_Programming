# doing operations on integers using class
class Integers:
    def __init__(self, list1):
        self._list1 = list1
        self._add = 0

    def display(self):
        print("The given list is: ",self._list1)

    def find_largest(self):
        largest = max(self._list1)
        print("The largest number is: ", largest)

    def find_smallest(self):
        smallest = min(self._list1)
        print("The smallest number is: ", smallest)

    def sum(self):
        self._add = sum(self._list1)
        print("The sum of the numbers is: ", self._add)

    def mean(self):
        mean = self._add /(len(self._list1))
        print("The mean of the numbers is: ", mean)


x = int(input("Enter the numbers of elements: "))
y = []
for i in range(x):
    z = int(input("enter the number: "))
    y.append(z)

result = Integers(y)
result.display()
result.find_largest()
result.find_smallest()
result.sum()
result.mean()
