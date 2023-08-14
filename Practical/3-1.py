import sys

import numpy
import numpy as np
from numpy import linalg as LA

n = int(input())
matrix = []
for i in range(n):
    vector = np.array(input().split()).astype(np.float_)
    vector = numpy.divide(vector, LA.norm(vector, 2))
    matrix.append(vector)
matrix = np.matrix(matrix)
matrixT = np.transpose(matrix)
res = np.matmul(matrix, matrixT)
m = int((res.size ** (1 / 2)))
np.fill_diagonal(res, 0)
col = np.argmax(res) % m + 1
row = np.argmax(res) // m + 1
print(row, col)
np.fill_diagonal(res, sys.maxsize)
col = np.argmin(res) % m + 1
row = np.argmin(res) // m + 1
print(row, col)
