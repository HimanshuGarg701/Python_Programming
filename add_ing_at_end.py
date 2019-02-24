# adding ing at the end if character is longer then 3, if ing already there then add ly
def string(str_1):
    if len(str_1)<3:            # len shows the length of the string
        return str_1
    elif len(str_1)>3:
        if str_1[len(str_1)-3:] != "ing":
            return str_1 + "ing"
        elif str_1[len(str_1)-3:] == "ing":
            return str_1 + "ly"


line = input("enter the string: ")
print(string(line))
