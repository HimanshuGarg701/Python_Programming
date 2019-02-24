"""making a different pattern: making a square with one diagonal to be $"""
for i in range(1,6):
    print()
    for j in range(1,6):

        if i>=2 and i<5:
            if j>=2 and j<5 and i!=j:
                print(" ",end=" ")
            elif i==j:
                print("$",end=" ")
            else:
                print("*",end=" ")
        else:
            print("*", end=" ")

