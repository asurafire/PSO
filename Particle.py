from time import sleep
import numpy as np
from numpy import sin, cos, e
import matplotlib.pyplot as plt
from random import random, seed


class Particle:
    p_glob = [100000, 100000]

    def __init__(self, inertia,  b_loc, b_glob, scale, fun):
        self.path = []
        self.position = [random() * scale, random() * scale]
        self.velocity = [0.0, 0.0]
        self.b_loc = b_loc
        self.b_glob = b_glob
        self.inertia = inertia
        self.p_i = self.position
        value = fun(self.position[0], self.position[1])
        value_glob = fun(Particle.p_glob[0], Particle.p_glob[1])
        if value < value_glob:
            Particle.p_glob = self.position

    def step(self):
        v_new = []
        value_old = fun(self.position[0], self.position[1])
        value_glob = fun(Particle.p_glob[0], Particle.p_glob[1])
        for i in range(len(self.position)):
            v_new += [self.inertia * self.velocity[i] + self.b_loc * (self.p_i[i] - self.position[i]) + self.b_glob * (Particle.p_glob[i] - self.position[i])]
            self.position[i] += v_new[i]
        value = fun(self.position[0], self.position[1])
        if value < value_glob:
            Particle.p_glob = self.position
        if value < value_old:
            self.p_i = self.position
        self.velocity = v_new
        return self.position[0], self.position[1]

    def print_members(self):
        print(self.position)
        print(self.velocity)

    def accumulate(self):
        self.path += [fun(self.position[0], self.position[1])]

    def plot(self):
        plt.plot(np.array(self.path).transpose(), "ob")

    def plotstep(self):
        plt.plot([self.position[0]], [self.position[1]],"ob")


def fun(x, y):
    return sin(x) * cos(y)

def fun2(x, y):
    return (e**(cos(y) * sin(x) * 2)  +  x + y + sin(x) * 5)**3

