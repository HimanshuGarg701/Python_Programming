# using the ZeroDivisionError
while True:
    try:
        x = int(input("Enter the numerator: "))
        y = int(input("Enter the denominator: "))
        z = x/y
        print("The result of ", x, "/", y, " is: ", z)
        break
    except ZeroDivisionError:
        print("The value of denominator can't be zero")
