#!/usr/bin/env python

class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real+other.real, self.imaginary+other.imaginary)

    def __sub__(self, other):
        return Complex(self.real-other.real, self.imaginary-other.imaginary)

    def __mul__(self, other):
        return Complex(self.real*other.real-self.imaginary*other.imaginary, self.real*other.imaginary+self.imaginary*other.real)

    def __truediv__(self, other):
        min = other
        min.imaginary = -min.imaginary
        temp = self*min
        temp.real = temp.real/(other.real**2+other.imaginary**2)
        temp.imaginary = temp.imaginary/(other.real**2+other.imaginary**2)
        return temp

    def __str__(self):
        return "{}, {}i".format(self.real,self.imaginary)

z1 = Complex(1,8)
z2 = Complex(2,3)
res = z1 * z2
print(res)