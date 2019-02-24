# search for all the words that starts with the user's entered character and print them
x = []
y = int(input("enters the number of terms: "))
for i in range(y):
    z = input("enter the element: ")
    x.append(z)
a = input("enter the element whose extended version you want to see: ")
count = 0
for b in range(len(x)):
    if a==x[b][0]:
        print(x[b])
        count += 1
if count == 0:
    print("SORRY!!!, No words found")
