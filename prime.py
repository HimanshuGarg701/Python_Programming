# finding all the prime numbers from 1 to 100
for i in range(2,101):
    for a in range(2,101):
        if i%a==0:
            break
    if i==a:
            print(i)
