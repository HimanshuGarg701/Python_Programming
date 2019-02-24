# deleting a specified thing for the first thing
def delete(str_1,str_2):    # str_1 is the main string; str_2 is what need to be removed
    result=" "
    for i in str_1:
        if i in str_2:
            continue
        else:
            result += i
    return result


string_1 = input("enter the string: ")
string_2 = input("enter what you want to remove: ")
print(delete(string_1,string_2))
