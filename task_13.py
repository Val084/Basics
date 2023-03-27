def mt(t):
    for i in t:
        print(*i)


import random
import numpy

a = int(input())
b = int(input())
matr1 = numpy.array([[random.randint(-500, 500) for j in range(b)] for i in range(a)])
c = a
d = b
matr2 = numpy.array([[random.randint(-500, 500) for j in range(d)] for i in range(c)])
matr3 = matr1 + matr2
mt(matr3)
