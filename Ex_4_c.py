#!/usr/bin/env python


a=[1,2,12,4]
b=[2,4,2,8]
iloczyn=[]
for i in range(len(a)):
    iloczyn.append(a[i]*b[i])

iloczyn=sum(iloczyn)
print(iloczyn)