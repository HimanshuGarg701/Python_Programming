# program to find the area of a triangle
import math # importing math module
def area(x,y,z):
    s = (x + y + z)/2
    ar = math.sqrt(s*(s-x)*(s-y)*(s-z))     # this is the formula to find area 
    return ar


a = int(input("Enter a side: "))
b = int(input("Enter a side: "))
c = int(input("Enter a side: "))
print(area(a,b,c))
