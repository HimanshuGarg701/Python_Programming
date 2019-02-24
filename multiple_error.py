# showing multiple errors in classes (Number guessing game)
class NumberError(Exception):
    def display(self):
        print("The number is too small")


class LargeError(Exception):
    def display(self):
        print("The number is too large")


num = 100
while True:
    try:
        x = int(input("enter a number: "))
        if x == num:
            print("Number guessed is right")
            break
        elif x < num:
            raise NumberError
        elif x > num:
            raise LargeError
    except NumberError as i:
        i.display()
    except LargeError as j:
        j.display()






