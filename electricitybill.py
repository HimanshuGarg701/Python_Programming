# applying comditions according to the units consumed
x = float(input("enter the units consumed"))
if x>=0 and x<=150:
    amount = x*3
elif x>150 and x<=350:
    amount = 100 + (x-150)*3.75
elif x>350 and x<=450:
    amount = 250 + (x-350)*4
elif x>450 and x<=600:
    amount = 300 + (x-450)*4.25
else:
    amount = 400 + (x-600)*5

print("The payable amount is: Rs", amount)
