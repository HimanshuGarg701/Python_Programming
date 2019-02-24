# returning 0 if entered number is prime else 1
def prime(x):
    count = 0
    for i in range(2,x):
        if x%i==0:
            count += 1
    if count >=1:
        print("0")
    else:
        print("1")

a = int(input("enter any number"))
prime(a)
