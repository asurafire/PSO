import numpy as np
from numpy.core.umath import sin, cos, e, absolute, sqrt, pi, power


def fun1(x, y):
    return sin(x) * cos(y)


def fun2(x, y):
    return (e**(cos(y) * sin(x) * 2)  +  x + y + sin(x) * 5)**3


def rosenbrock(x, y):
    Z = (power((1 - x), 2) + 100 * power((y - x * x), 2))
    return Z


def rastrigin(x,y):
    return 20 + (x * x - 10 * cos(2 * np.pi * x)) + (y * y - 10 * cos(2 * np.pi * y))

def himmelblau(x,y):
    return (x * x + y -11)**2 + (x + y * y - 7)**2

def htable(x,y):
    return - absolute(sin(x) * cos(x) * power(e, (absolute(1 - (sqrt(x * x + y * y)/pi)))))