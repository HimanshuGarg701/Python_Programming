# checking the aveage of sum of odd and even numbers
even = 0
odd = 0
count_even = 0
count_odd = 0
while True:
    x = int(input("enter any number(press -1 to exit): "))
    if x > 0:
        if x%2==0:      # includes all even numbers
            even += x
            count_even +=1
        else:           # includes all odd numbers
            odd += x
            count_odd +=1

    elif x==-1:
        print("The average of even numbers is: ",even/count_even)
        print("the average of odd numbers is: ", odd/count_odd)
        break
