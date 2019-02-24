# adding and displaying details of a book using class
class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.publisher = ""
        self.ISBN = 0

    def read(self):
        self.title = input("enter the title: ")
        self.author = input("Enter the author: ")
        self.publisher = input("Enter the publisher: ")
        self.ISBN = int(input("Enter the number: "))

    def display(self):
        print("The title of the books is: ", self.title)
        print("The author of the book is: ", self.author)
        print("The publisher of the book is: ", self.publisher)
        print("The ISBN number of the book is: ", self.ISBN)


z = Book()
x = []
while True:
    y = input("Do you want to enter in the details?(y/n): ")
    if y == "y":
        z.read()
        x.append(z)
    elif y == "n":
        for j in x:
            j.display()
        break
