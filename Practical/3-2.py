import sys

import numpy as np
from numpy import linalg as LA


def mostFrequent(array):
    n = len(array)
    array.sort()
    max_count = 1
    res1 = array[0]
    curr_count = 1

    for i in range(1, n):
        if array[i] == array[i - 1]:
            curr_count += 1
        else:
            curr_count = 1

        if curr_count > max_count:
            max_count = curr_count
            res1 = array[i - 1]
    return res1


n = input().split()
a, b, c = int(n[0]), int(n[1]), int(n[2])
vectors = []
vectorsRes = []
for i in range(b):
    temp = np.array(input().split()).astype(np.float_)
    vectorsRes.append(temp[-1])
    temp = np.delete(temp, -1)
    vectors.append(temp)
for i in range(c):
    target = np.array(input().split()).astype(np.float_)
    res = []

    for q in range(a):
        arr = []
        min_norm = sys.maxsize
        minIndex = sys.maxsize
        for j in range(0, b):
            if j in res:
                continue
            arr.append(target - vectors[j])
            if LA.norm(arr[-1], 1) < min_norm:
                minIndex = j
                min_norm = LA.norm(arr[-1], 1)
        res.append(minIndex)
    result = []
    for k in res:
        result.append(vectorsRes[k])
    print(int(mostFrequent(result)), end=" ")
