# making a square pattern
for i in range(1,6):
    print()     # this helps to get a new line
    for j in range(1,6):
        if i>=2 and i<5:
            if j>=2 and j<5:
                print(" ",end=" ")
            else:
                print("*", end=" ")
        else:
            print("*", end=" ")

