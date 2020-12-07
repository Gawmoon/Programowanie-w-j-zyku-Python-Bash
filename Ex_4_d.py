#!/usr/bin/env python

import random
import numpy as np

A=[]
B=[]
for i in range(128):
    rowA=[]
    rowB=[]
    for j in range(128):
        rowA.append(random.randint(-50,50))
        rowB.append(random.randint(-50, 50))
    A.append(rowA)
    B.append(rowB)

suma=np.zeros((128,128))
for i in range(128):
    for j in range(128):
        suma[i][j]=A[i][j]+B[i][j]