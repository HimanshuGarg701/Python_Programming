# finding all the vowels in the entered string
class Vowels:
    def __init__(self, string):
        self._count = 0
        self._string = string

    def check(self):
        for i in self._string:
            if i in ("a","e","i","o","u"):
                self._count += 1
        print("The number of vowels in the string is: ",self._count)


x = input("enter the string: ")
abc = Vowels(x)
abc.check()
