# student data and exception handling
class Student:
    def __init__(self, name, roll_number):
        self._name = name
        self._roll_number = roll_number

    def display(self):
        print("The name of the student is: ", self._name)
        print("The roll number of the student is: ", self._roll_number)


try:
    x = str(input("Enter the name of the student: "))
    y = int(input("enter the roll number: "))
    z = Student(x, y)
    z.display()
except ValueError:
    print("you must enter valid data")
