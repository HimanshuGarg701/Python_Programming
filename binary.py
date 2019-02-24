# converting a decimal number into a binary number
while True:
    decimal_number = int(input("enter any number(press 999 to exit): "))
    if decimal_number<0:
        continue
    elif decimal_number>0 and decimal_number!=999:
        i = 0
        binary_num = 0
        while (decimal_number!=0):
            remainder = decimal_number%2
            binary_num = binary_num + remainder*(10**i)
            decimal_number = int(decimal_number/2)
            i += 1
        print("binary number of is: ", binary_num)
    elif decimal_number==999:
        break

