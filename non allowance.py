# if the name of the person is rahul, then he must be removed
x = str(input("Enter the name: "))
x = x.lower()
try:
    if x!="rahul":
        print("Hello ", x," welcome to python!")
    else:
        raise ValueError
except ValueError:
    print("Sorry Rahul you are not allowed to access this feature")
