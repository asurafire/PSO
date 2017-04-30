import Particle
from Particle import Particle
from Functions import fun1, fun2, rosenbrock, rastrigin, himmelblau
from numpy import sin, cos, e
import numpy as np

f = himmelblau
domain = 6
particles = []
for n in range(10):
    for i in range(50):
        particles += [Particle(0.5, 0.5, 0.75, domain * 2, f)]
    for s in range(100):
        for p in particles:
            p.step(True)
    print("@ "
            + str(Particle.p_glob[0])
            + "  "
            + str(Particle.p_glob[1])
            + "\nvalue: \t\t\t\t\t\t\t\t\t\t\t\t"
            + str(f(Particle.p_glob[0], Particle.p_glob[1])))