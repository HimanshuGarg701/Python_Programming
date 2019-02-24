# inserting elements at user's desired position of the list
x = []
y = int(input("enter the number of terms: "))
for i in range(y):
    z = input("enter the element: ")
    x.append(z)
print("the current list is: ",x)
a = int(input("enter the position where you want to insert: "))
b = input("enter what you want to insert: ")
x.insert(a+1, b)            # added 1 because the counting starts from 0
print("new lis is: ",x)
