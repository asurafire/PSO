from random import random
from Functions import *
import matplotlib.pyplot as plt
import numpy as np


class Particle:
    p_glob = [100000, 100000]

    def __init__(self, inertia,  b_loc, b_glob, scale, fun):
        self.path = []
        self.position = [random() * scale - scale/2, random() * scale - scale/2]
        self.velocity = [0.0, 0.0]
        self.b_loc = b_loc
        self.b_glob = b_glob
        self.inertia = inertia
        self.fun = fun
        self.p_i = self.position
        value = fun(self.position[0], self.position[1])
        value_glob = fun(Particle.p_glob[0], Particle.p_glob[1])
        if value < value_glob:
            Particle.p_glob = self.position

    def step(self, rnd):
        v_new = []
        value_old = self.fun(self.position[0], self.position[1])
        value_glob = self.fun(Particle.p_glob[0], Particle.p_glob[1])
        if(rnd):
            v_new = self.upade_position_rand(v_new)
        else:
            v_new = self.upade_position(v_new)
        value = self.fun(self.position[0], self.position[1])
        if value < value_glob:
            Particle.p_glob = self.position
        if value < value_old:
            self.p_i = self.position
        self.velocity = v_new
        return self.position[0], self.position[1]

    def upade_position(self, v_new):
        for i in range(len(self.position)):
            v_new += [self.inertia * self.velocity[i]
                      + self.b_loc * (self.p_i[i] - self.position[i])
                      + self.b_glob * (Particle.p_glob[i] - self.position[i])]
            self.position[i] += v_new[i]
        return v_new
    def upade_position_rand(self, v_new):
        for i in range(len(self.position)):
            v_new += [self.inertia * self.velocity[i]
                      + self.b_loc * random() * (self.p_i[i] - self.position[i])
                      + self.b_glob * random() * (Particle.p_glob[i] - self.position[i])]
            self.position[i] += v_new[i]
        return v_new

    def print_members(self):
        print(self.position)
        print(self.velocity)

    def accumulate(self):
        self.path += [self.fun(self.position[0], self.position[1])]

    def plot(self):
        plt.plot(np.array(self.path).transpose(), "ob")

    def plotstep(self):
        plt.plot([self.position[0]], [self.position[1]],"ob")


