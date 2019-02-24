# counting number of times a value is present inside the list
x = []
y = int(input("enter the number of terms: "))
for i in range(y):
    z = input("enter the element: ")
    x.append(z)
y = set(x)              # so that each item is checked once
for i in y:
    if i in x:
        b = x.count(i)
        print(i,"is present ",b,"number of times")
