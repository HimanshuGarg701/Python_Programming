# use a loop to reverse the list
x = []
y = int(input("enters the number of terms: "))
for i in range(y):
    z = input("enter the element: ")
    x.append(z)
print("The list you entered is: ",x)
a = []
b = y
while b>0:
    a.append(x[b-1])
    b = b-1
print("The reversed list is: ",a)
