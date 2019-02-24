# sorting three numbers
def sort(x, y, z):
    if y > x and z > y:
        return True
    else:
        return False


a = int(input("Enter any three numbers: \n"))
b = int(input())
c = int(input())
print(sort(a,b,c))
