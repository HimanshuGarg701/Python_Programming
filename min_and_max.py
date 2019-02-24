val = {"math":95, "science":93, "english": 90}
x = []
for i,j in val.items():
    x.append(j)

print("The maximun value is: ", max(x))
print("The minimum value is: ", min(x))