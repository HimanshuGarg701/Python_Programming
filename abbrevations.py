# example The Jungle Book should be displaye as TJB
def abs(str_1):
    str_2 = str_1.split(" ") # .split(" ") seprates the words at blank
    for i in str_2:
        print(i[0].upper(),end="")


string_1 =input("enter the string: ")
abs(string_1)
