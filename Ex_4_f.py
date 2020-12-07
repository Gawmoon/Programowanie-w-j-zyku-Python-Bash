#!/usr/bin/env python


import random
from copy import deepcopy

def determinant(A, det=0):
    columns= list(range(len(A)))
    if len(A) == 2 and len(A[0]) == 2:
        result = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return result
    for column in columns:
        B = deepcopy(A)
        B = B[1:]
        rows = len(B)
        for row in range(rows):
            B[row] = B[row][0:column] + B[row][column + 1:]
        change_sign = (-1) ** (column % 2)
        temp_det = determinant(B)
        det += change_sign * A[0][column] * temp_det
    return det

A = [[random.randint(0, 10) for i in range(0, 4)] for j in range(0, 4)]
print(determinant(A))