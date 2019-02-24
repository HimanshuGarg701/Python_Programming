# naming certain titles and displaying them
class Title:
    def __init__(self, name , faculty, college):
        self._name = name
        self._faculty = faculty
        self._college = college

    def display(self):
        print("The entered name is: ", self._name)
        print("The faculty is: ", self._faculty)
        print("The name of the college is: ", self._college)


x = int(input("enter how many enteries you want: "))
for i in range(x):
    a = input("enter the name: ")
    b = input("enter the faculty: ")
    c = input("enter the college: ")
    A = Title(a, b, c)
    A.display()
