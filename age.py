# enter current year and your birthe year and code will display your age
x = int(input("enter the current date, month and year resp \n"))
y = int(input())
z = int(input())
a = int(input("enter the birth date, month and year resp \n"))
b = int(input())
c = int(input())
age = z - c  # current year minus birth year
z = str(z)
c = str(c)
print("Date of birth is",str(a) +"/",str(b)+"/",str(c[2]),str(c[3]))
print("Current date is",str(x) +"/",str(y)+"/",str(z[2]),str(z[3]))
print("Age of person is",age)
