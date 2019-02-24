# checking whether the entered alphabet is uppercase or lowercase
x = input("enter any alphabet")
if x.isupper():
    print("upper case")
elif x.islower():
    print("lower case")
else:
    print("wrong input")
