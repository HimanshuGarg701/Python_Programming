# getting the transpose of a matrix
x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i] = x[i][j]
for r in result:            # because r is a list of lists, we need to extract all the lists
    print(r)
