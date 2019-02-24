# finding the average of the numbers entered 
def sum(args, count):
    print(args/count)


x = int(input("how many numbers you want?"))
add = 0
nums = 0
for i in range(1, x+1):
    num = int(input("enter any number: "))
    nums += 1
    add += num
sum(add,nums)
