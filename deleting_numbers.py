# make a list from 1-20 and then delete numbers which are divisible by 5
x = []
for i in range(1,21):
    x.append(i)
print("The numbers are: ",x)
y = []
for j in x:
    if int(j)%5==0:
        continue
    else:
        y.append(j)
print("The new list is: ",y)
