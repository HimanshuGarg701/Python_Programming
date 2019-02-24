# reverse a string if the length is greater then 4; else return as it is
def reverse(str):
    if len(str)<4:
        return str
    else:
        return str[::-1]


string = input("enter any string: ")
print(reverse(string))
