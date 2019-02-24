# adding, subtracting and multiplying two matrices
class Matrix:
    def __init__(self, matrix1, matrix2):
        self._matrix1 = matrix1
        self._matrix2 = matrix2
        self._adding = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

        self._subtract = [[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]

        self._multiply = [[0, 0, 0],
                          [0, 0, 0],
                          [0, 0, 0]]

    def add(self):
        for i in range(len(self._matrix1)):
            for j in range(len(self._matrix1)):
                self._adding[i][j] = self._matrix1[i][j] + self._matrix2[i][j]
        print("The sum of the matrices is: \n")
        for r in self._adding:
            print(r)

    def sub(self):
        for a in range(len(self._matrix1)):
            for b in range(len(self._matrix1)):
                self._subtract[a][b] = self._matrix1[a][b] + self._matrix2[a][b]
        print("The difference of the matrices is: \n")
        for s in self._subtract:
            print(s)

    def multiply(self):
        for c in range(len(self._matrix1)):
            for d in range(len(self._matrix1)):
                self._multiply[c][d] = self._matrix1[d][c] * self._matrix2[c][d]
        print("the product of the matrices is: \n")
        for t in self._multiply:
            print(t)


result1 = [[1, 4, 7],
           [2, 5, 8],
           [3, 6, 9]]
result2 = [[4, 5, 6],
           [7, 8, 9],
           [1, 2, 3]]
x = Matrix(result1, result2)
x.add()
x.sub()
x.multiply()
