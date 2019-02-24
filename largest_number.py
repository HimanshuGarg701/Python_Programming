# finding the largest number of the entered numbers
y = 0
while True:  # its an infinite loop unless a break statement is added
    x = int(input("enter any number(press 0 to exit)"))
    if x == 0:
        break
    elif x > y:
        y = x
    else:
        continue
print("The largest number is",y)
