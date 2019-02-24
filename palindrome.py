# palindrome is something in which the word remains the same whether read from starting or from end
def palindrome(str_1):
    rev = str_1[::-1]
    if str_1==rev:      # checking if palindrome
        print("This is a palindrome")
    else:
        print("This is not a palindrome")


x = str(input("enter anything: "))
(palindrome(x))
