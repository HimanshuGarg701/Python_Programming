# reversing a string using recursion 
def reverse(x):
    if x =="":
        return x
    else:
        return reverse(x[1:]) + x[0]
print(reverse("abcde"))
