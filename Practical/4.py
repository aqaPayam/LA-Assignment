import numpy as np

v = 0
n = int(input())
arr = []
for i in range(n):
    elements = list(map(int, input().split()))
    v += np.sum(elements)
    arr.append(elements)
adjacencyMatrix = np.array(arr).reshape(n, n)
v //= 2

none = True
for i in range(n):
    for j in range(n):
        if i < j:
            if adjacencyMatrix[i][j] == 1:
                pol = True
                tempMatrix = np.copy(adjacencyMatrix)
                tempMatrix[i][j] = 0
                tempMatrix[j][i] = 0
                tempMatrix2 = np.copy(tempMatrix)
                for k in range(1, v):
                    tempMatrix2 = np.matmul(tempMatrix, tempMatrix2)
                    if tempMatrix2[i][j] != 0:
                        pol = False
                        break
                if pol:
                    none = False
                    print(i, j)
if none:
    print("none")
