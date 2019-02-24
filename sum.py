# adding all the elements of the list
z = []
x = int(input("enter how many numbers you want to enter: "))
while x>0:
    x -= 1
    y = int(input("enter the number: "))
    z.append(y)
print("the sum of the numbers is: ", sum(z))
