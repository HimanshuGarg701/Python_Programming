# removing the character of a specified position
def remove(string, n):
    r = " "
    for i in range(len(string)):
        if i==n-1:
            continue
        else:
            r += string[i]
    return r


str = input("enter any string: ")
m = int(input("enter the index number you want to remove: "))
print(remove(str,m))
