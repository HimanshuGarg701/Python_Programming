# reversing a number using recursion 
def reverse(x):
    if x < 10:
        print(x,end="")
    else:
        print(x%10,end="")
        reverse(x//10)


a = int(input("Enter any number: "))
reverse(a)
