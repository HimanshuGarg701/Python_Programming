# show the price of the ordered dish (using dictionary)
menu = {"burger":50, "noodles":80, "fries":30,"cake":100, "pizza":100}
while True:
    x = str(input("enter what you want to eat: "))

    if x in menu.keys():
        print("Your order of ",x,"will cost you Rupees ",menu[x])
        break
    else:
        print("SORRY THIS ITEM IS UNAVAILABLE, PLEASE RE-ENTER THE ORDER")
        continue
