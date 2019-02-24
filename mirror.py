# creating mirror image of a string 
def mirror(str):
    rev = str[::-1]     # [::-1] reverses the string
    return (str + "="+rev)

x = input("enter any string: ")
print(mirror(x))
