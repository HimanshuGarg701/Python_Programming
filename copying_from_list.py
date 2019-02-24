# there is a predefined list and a tuple, return the common elements in form of list
x = ["1", "2", "abc", "def", "ghi", "4", "5"]
y = ("abc", "2", "5", "def", 3)
z = []
for i in y:
    if i in x:
        z.append(i)
print(z)
