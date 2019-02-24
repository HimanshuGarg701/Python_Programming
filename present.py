# cchecking the searched element is present in the list or not
x = []
y = int(input("enters the number of terms: "))
for i in range(y):
    z = input("enter the element: ")
    x.append(z)
a = input("enter the element you want to check: ")
if a in x:
    print("yessss the searched item is present in the list")
else:
    print("No, the searched item is not in the list")
