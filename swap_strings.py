# simply swapping two strings
def swap(str_1, str_2):
    str_1 , str_2 = str_2, str_1
    print("new Value of string 1 is :", str_1)
    print("new Value of string 2 is :", str_2)


string_1 = input("enter the string 1: ")
string_2 = input("enter the string 2: ")
swap(string_1,string_2)
