basic_pay = float(input("enter the basic pay of the user"))
HRA = basic_pay/10
TA = basic_pay*5/100
salary = basic_pay-HRA-TA

print("the salary of the person is: "+ str(salary))
