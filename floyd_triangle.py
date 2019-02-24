# making a floyd triangle (1 in first row; 1,2 in second row; 1,2,3 in third row and so on)
x = int(input("enter the number: "))
b=0
for i in range(1,x+1):
    for a in range (1,i+1):
        b += 1
        print(b,end="  ")       # end="" means remaining in the same line
    print()
