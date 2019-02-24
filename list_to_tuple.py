x = []
ques = int(input("How many numbers you want in the list: "))
for i in range(ques):
    y = input("enter the elements: ")
    x.append(y)
print("The list form is: ",x)
x = tuple(x)
print("The tuple form is: ",x)