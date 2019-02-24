# finding the prime factors of a number
x = int(input("enter any number"))
for i in range(2,x):
    if x%i==0:
        for a in range(2,x):
            if i%a==0:
                break
        if i==a:
            print(i)
