# finding the numbers which are not divisible 2 and 3
for i in range(1,101):
    if (i%2==0 or i%3==0):
        continue
    print(i)
