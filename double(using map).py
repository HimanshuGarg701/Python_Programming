# returning the doubled version of a number in list form using map
def double(ar):
    for i in ar:
        i = int(i)
        return 2*i


z= []
x = int(input("how many numbers you want ot enter: "))
for i in range(x):
    y = input("enter the numbers: ")
    z.append(y)
print(list(map(double, z)))
