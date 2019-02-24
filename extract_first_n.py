# extracting the first n characters of a string as provided by user
def extract(str_1,n):
    for i in range(0,len(str_1)):
        if i <n:
            continue
        else:
            print(str_1[i],end="")


string_1 = input("enter the string: ")
m = int(input("enter the number of characers you want to remove: "))
extract(string_1,m)
