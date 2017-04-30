from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import cm
from matplotlib import animation
from time import sleep
import Particle
from Particle import fun1, fun2, Particle, rastrigin
from numpy import sin, cos, e
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

f = rastrigin
fig = plt.figure()
ax = p3.Axes3D(fig)
# Make data.
X = Y = np.arange(-5.12, 5.12, 0.1)
X, Y = np.meshgrid(X, Y)
#Z = (e**(cos(Y) * sin(X) * 2)  +  X + Y + sin(X) * 5)**3
#Z = sin(X) * cos(Y)
Z = rastrigin(X,Y)
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.jet, alpha=0.4,
                       linewidth=0, antialiased=False)

particles = []
plottels = []
for i in range(50):
    p = Particle(0.0, 1, 2, 5.12 * 2, f)
    particles += [p]
    plottels += ax.plot([p.position[0]], [p.position[1]], [f(p.position[0], p.position[1])], "o", c="k")
x = y = z = []


def animate(i, plottels):
    for n in range(len(plottels)):
        particles[n].step(True)
        p = plottels[n]
        p.set_data([particles[n].position[0], particles[n].position[1]])
        p.set_3d_properties(f(particles[n].position[0], particles[n].position[1]))
    return plottels,

anim = animation.FuncAnimation(fig, animate, frames=20, interval=1000, fargs=(plottels,))
anim.save('rastrigin.mp4', fps=10, extra_args=['-vcodec', 'libx264'])
plt.show()
