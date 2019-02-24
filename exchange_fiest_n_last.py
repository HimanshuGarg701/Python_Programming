# excahnging the first and last character of a string
def exchange(str):
    r = str[-1] + str[1:len(str)-1] + str[0]
    return r


x = input("enter any string")
print(exchange(x))
