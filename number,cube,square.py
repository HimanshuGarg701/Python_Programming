# printing the cubes and squares of numbers
x = int(input("enter the number of terms"))
print("number" + "\t\t" + "square" + "\t\t" + "cube")
for i in range(1, x+1):
    print(i, "    \t\t", i**2, "    \t\t", i**3)
