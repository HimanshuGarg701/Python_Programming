# printing the sum of all the even positioned elements of a list
z = []
x = int(input("enter the number of terms you want in list: "))
for i in range(1,x+1):
    y = int(input("enter the number you want in the list: "))
    z.append(y)
sum = 0
for x in range(1,x,2):
    sum += z[x]
print(sum)
