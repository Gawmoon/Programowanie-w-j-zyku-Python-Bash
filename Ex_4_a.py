#!/usr/bin/env python

import math
import sys
def equation(a,b,c):
    delta=b*b - 4*a*c
    if delta<0:
        print("No solutions in R")
        return
    delta=math.sqrt(delta)
    x1=(b-2*b -delta)/(2*a)
    x2=(b-2*b +delta)/(2*a)
    print("First soultion={}".format(x1))
    print("Second soultion={}".format(x2))


if __name__ == "__main__":
    equation(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))