import numpy as np
import matplotlib.pyplot as plt

imort pdb
pdb.set_trace()
myDict = {}
myList = [1,2,3,4]
myList1 = [[1,2,3,4],
           [2,3,4,5]]

print myList
print myList1

class AverageNumber1(object):

    def __init__(self, A=32, B=54):
        self.A = A
        self.B = B

    def sum(self):

        summ = self.A + self.B
        return summ


class AverageNumber2(AverageNumber1):

    def __init__(self, C=10):
        super(AverageNumber2, self).__init__()
        self.C = C

    def minus(self):

        result = self.C - self.B

        return result


def func_a(a, b, c):

    return a, b, c


func1 = func_a(a=3, b=4, c=19)
a, b, c = func_a(a=3, b=4, c=19)
print type(func1)

a = func1[0]
b = func1[1]
c = func1[2]


method1 = AverageNumber1(45, 76)
summation = method1.sum()

method2 = AverageNumber2(C=30)
minus_result = method2.minus()
summation2 = method2.sum()

print 'summation={}, variable={}'.format(summation, summation2)
print 'sumation = %3.3f, variable=%3f'%(float(summation/1.82332), float(summation2/2.2243))


