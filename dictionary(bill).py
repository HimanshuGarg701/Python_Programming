# making a food bill for all the items in a dictionary
price = {"apple": 50, "mango": 25, "banana": 30, "tomato": 40}
sum = 0
for i,j in price.items():
    print("price of " ,i, "is Rupees ",j)
    sum += int(j)
print("The total price to be paid is Rupees ",sum)
