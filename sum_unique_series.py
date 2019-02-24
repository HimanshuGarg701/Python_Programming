# summing up a unique series (-1 + 4 - 9 + 16 -25 + 36 -------------)
import math
x = int(input("enter any number"))
odd = 0
even = 0
for i in range(1,11):
    if i%2==0:
        even += (x**i)
    elif i%2!=0:
        odd += (x**i)
result = even - odd
print(result)

print("==================================NEW QUESTION==================================================")
# new question for summing up numbers upto n
y = int(input("enter the length of series"))
sum = 0
for i in range(1,y+1):
    for j in range(1,i+1):
        sum += j
print("The sum is:", sum)

print("====================================NEW Question=================================================")
# sum of (-x^2/1! + x^2/2! - x^/3! -----------)
z = int(input("enter the length of number"))
v = int(input("enter any number"))
oddd = 0
evenn = 0
for k in range(0,z):
    if k%2==0:
        evenn += v**k/(math.factorial(k))
    elif k%2!=0:
        oddd += v**k/(math.factorial(k))
resultt = evenn - oddd
print("The result of the equation is: ", resultt)
