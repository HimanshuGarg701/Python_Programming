# first 50 numbers except those which are divisible by 3 or 6
x = []
for i in range(1,51):
    if i%3==0 or i%6==0:
        x.append(i)
print("The numbers divisible by 3 or 6 in first 50 numbers are: ",x)
