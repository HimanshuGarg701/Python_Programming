# program to print first 2 and last 2 characters of a string if length of string > 2.
def find_ch(st):
    if len(st)<2:
        return " "
    elif len(st)>2:
        new_str = str(st[0:2]) + str(st[-2:])       # new_str is a new variable here
        return new_str

string = input("enter any string")
print(find_ch(string))
