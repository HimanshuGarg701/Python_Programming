# sum of unique series (12/1 + 22/2 + 32/3 + 42/4 + -------)
x = int(input("enter the number of terms: "))
sum = 0
for i in range(1,x+1):
    sum += float((i*10+2)/i)    # sum += x means sum = sum + x
print(sum)
