# checking whether a number is a power of 2 or not
x = int(input("enter the number"))
while True:
    if x%2==0:
        x = x/2
        if x==1:
            print("power of 2")
            break
        else:
            continue
    else:
        print("Not a power of 2")
        break
