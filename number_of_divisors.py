# finding out the divisors of a number
def divisors(x,y):
    for i in range (1,y):
        if x%i==0:
            print(i)
        else:
            continue


a = int(input("enter divident number: "))
b = int(input("enter up to which number you want to find divisors: "))
divisors(a, b)
