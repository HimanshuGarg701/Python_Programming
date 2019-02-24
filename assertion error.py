# The numberes should be entered as asked unless display to correct mistake
x = int(input("enter the larger number: "))
y = int(input("enter the smaller number: "))
try:
    if x > y:
        print("you entered the right numbers")
    else:
        raise AssertionError
except AssertionError:
    print("Sorry you didn't entered the numbers correctly")
