# finding the square root of a number
import math
x = int(input("enter the number: "))
try:
    if x == 0:
        print("The square root of zero is 0")
    elif x > 0:
        y = math.sqrt(x)
        print("The square root of ", x, " is: ", y)
    else:
        raise ValueError
except ValueError:
    print("Sorry you can't enter negative numbers")
