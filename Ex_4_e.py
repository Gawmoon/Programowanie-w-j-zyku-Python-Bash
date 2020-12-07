#!/usr/bin/env python

import random
import numpy as np

A=[]
B=[]
for i in range(8):
    rowA=[]
    rowB=[]
    for j in range(8):
        rowA.append(random.randint(-50,50))
        rowB.append(random.randint(-50, 50))
    A.append(rowA)
    B.append(rowB)
multiplicated=np.zeros((8,8))
for i in range(8):
   for j in range(8):
       for k in range(8):
           multiplicated[i][j] += A[i][k] * B[k][j]