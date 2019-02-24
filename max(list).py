x = []
y = int(input("enter the number of terms: "))
for i in range(y):
    z = input("enter the element: ")
    x.append(z)
print("The max value present in the list is: ",max(x))
print("The min value present in the list is: ",min(x))