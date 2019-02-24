# adding or verifying the birth date of a person using a dictionary
birth = {"raju": "Jan 1, 2000", "baju":"Jan 4, 2000", "kaju":"Jan7, 2000"}
x = str(input("enter the name you are looking for: "))

if x in birth.keys():
    print("The birth date of",x, "is: ",birth[x])


elif x!= birth.keys():
    print("your searched name is not mentioned here, please provide the birth date")
    z = input("enter the date: ")
    birth[x] = z
    print("the new dict is: ",birth)

