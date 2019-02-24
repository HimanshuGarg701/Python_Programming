# cehcking the longest number from the entered numbers
 def longest(args):
    s = 0
    z = 0
    for i in args:
        if len(i) > s:
            s = len(i)
            z = i

        else:
            continue
    return (z)


y=[]                # its an empty list
for j in range(1, 100):
    x = str(input("enter any number of strings (press 0 to exit): "))
    if x != '0':
        y.append(x)     # append adds on the items to the list
    elif x=='0':
        break
print(longest(y))
