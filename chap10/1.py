import sys

print(sys.builtin_module_names)

import numpy

arrA = numpy.array([1,2,3,4,5])
arrB = numpy.array([6,7,8,9,10])

print(arrA + arrB)

def helloworld():
    print("hello wrodl!!")

import hello as h

h.helloworld

from matplotlib import pyplot