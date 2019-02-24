# sorting the elements of a list
x = []
y = int(input("enter the number of elements: "))
for i in range(y):
    z = str(input("enter any element: "))
    x.append(z)
x.sort()
print("The sorted order of the list is: ", x)
