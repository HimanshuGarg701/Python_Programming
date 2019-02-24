"""
    if string has 2 uppercase letters in the first four characters
    then change all characters to upper case,
    else dont change anything.

"""

def upper(str):
    count = 0
    for i in range(0,4):
        if str[i].isupper():
            count +=1
            if count >=2:
                new_str = str.upper()
        else:
            continue
    if count<2:
        return str
    return new_str


line = input("enter any string: ")
print(upper(line))
