# counting the number of the uppercase and lowercase letters, press & to exit
upper = 0
lower = 0
digit = 0
while True:
    x = input("enter any character(press & to exit)")
    if x.isupper():
        upper = upper+1
    elif x.islower():
        lower = lower+1
    elif x.isdigit():
        digit += 1
    elif x=='&':
        print("lower case: ",lower)
        print("upper case: ",upper)
        print("digits: ",digit)
        break

