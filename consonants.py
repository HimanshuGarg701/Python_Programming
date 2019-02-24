# print all the consonants present in all the words of the list
x = []
y = int(input("enters the number of terms: "))
for i in range(y):
    z = input("enter the element: ")
    x.append(z)
print("the entered list is: ", x)

for b in x:
    print()
    for c in range(0,len(b)):
        if b[c] not in ("aeiou"):
            print(b[c],end=",")

