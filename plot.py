from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import animation
from time import sleep
import Particle
from Particle import fun, fun2, Particle
from numpy import sin, cos, e
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')
# Make data.
X = np.arange(-0 * np.pi, 2 * np.pi, 0.1)
Y = np.arange(-0 *np.pi, 2 * np.pi, 0.1)
X, Y = np.meshgrid(X, Y)
#Z = (e**(cos(Y) * sin(X) * 2)  +  X + Y + sin(X) * 5)**3
Z = sin(X) * cos(Y)
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.jet, alpha=0.4,
                       linewidth=0, antialiased=False)

particles = []
for i in range(20):
    particles += [Particle(0.0, 0.5, 0.75, 5, fun)]
x = []
y = []
z = []
for s in range(0):
    for p in particles:
        p.step()

for p in particles:
    x.append(p.position[0])
    y.append(p.position[1])
    z.append(fun(p.position[0], p.position[1]))
#ax.scatter(x,y,z, c='k', s=50, depthshade=False)
d, = ax.plot(x,y,z, 'ro', color='k')

def animate(i):
    for p in particles:
        p.step()
    d.set_3d_properties([p.position[0] for p in particles],
                        [p.position[1] for p in particles],
                        [fun(p.position[0], p.position[1])])
    return d,

#anim = animation.FuncAnimation(fig, animate, frames=100, interval=2000)

plt.show()