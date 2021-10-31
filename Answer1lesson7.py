import numpy as np
a = np.array([[3, 5, 1], [8, 7, 2]])
b = np.array([[5, 3, 4], [1, 10, 9]])
class Matrix:
    def __init__(self,matrix1):
        self.matrix1 = matrix1
    def __str__(self):
        return f"{self.matrix1}"
    def __add__(self, other):
        return Matrix(self.matrix1 + other.matrix1)
matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(matrix_2+matrix_1)