# removing the specified character from the main string
def remove(str,ch):
    r=" "
    for i in range(len(str)):
        if ch==str[i]:
            continue
        else:
            r +=str[i]
    return r

x = input("enter any string: ")
y = input("enter the character you want to remove: ")
print(remove(x,y))
