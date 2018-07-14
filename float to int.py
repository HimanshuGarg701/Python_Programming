x = float(input("enter any number"))
y = float(input("enter the second number"))
print("the value of first num is: "+str(x))
print("the value of second number is: "+str(y))
print("the sum of the numbers is: " + str(int(x+y)))

# =================================SIMPLE INTEREST=======================================================
principal = x
rate = y
time = int(input("Enter time in years"))
SI = principal * rate * time/100
print(SI)


# ===================================power================================================================

a = int(input("enter the number"))
b = int(input("enter the power"))
power = a**b
print("the power is given as " + str(power))