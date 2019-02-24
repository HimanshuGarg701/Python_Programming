# fibonacci series using recursion (0,1,1,2,3,5,8,13,21,34,------) 
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


x = int(input("enter the length of series"))
for i in range(0,x):
    print(fibonacci(i),end=" ")
