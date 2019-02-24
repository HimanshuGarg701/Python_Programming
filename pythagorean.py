# using pythagorean theorem to find hyp
import math
def hyp(a,b):
    return(math.sqrt(a*a+b*b))

x = int(input("enter tye first side: "))
y = int(input("enter the second side: "))
print(hyp(x,y))
