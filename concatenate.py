# concatenating strings without directly adding two string 
def conc(str_1, str_2):
    x = " "
    for i in range(0,len(str_1)):
        x += str_1[i]               # x becomes equal to str_1 after finishing loop
    for j in range(0,len(str_2)):
        x += str_2[j]               # x further adds on str_2
    return x


strn_1 = input("enter any first string: ")
strn_2 = input("enter any second string: ")
print(conc(strn_1,strn_2))
