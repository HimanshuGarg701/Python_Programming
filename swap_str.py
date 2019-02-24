# getting single string from two strings and swap the first 2 characters of both stings
def single(str1, str2):
    new_str = str1[1]+str1[0]+ str1[2:] +" "+ str2[1]+ str2[0] + str2[2:]
    return new_str

str_1 = input("enter the first string")
str_2 = input("enter the second string")
print(single(str_1, str_2))
