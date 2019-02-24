# removing all the odd numbered characters
def odd(str_1):
    r = " "
    for i in range(len(str_1)):
        if i in range(0, len(str_1)+1, 2):  # this includes all the odd elements
            continue
        else:
            r += str_1[i]
    return r


line = input("enter tye string: ")
print(odd(line))
