# determining whether the character entered is a digit or alphabet
x = input("enter any character")
if x.isdigit():     # checking for digit
    print("enter input is digit")
elif x.isalpha():    # checking for alphabet
    print("input is alphabet")
elif x.isspace():    # checking for space
    print("white space")
else:
    print("wrong input")
