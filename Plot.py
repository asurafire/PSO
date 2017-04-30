from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import cm
from matplotlib import animation
from time import sleep
import Particle
from Particle import Particle
from Functions import fun1, fun2, rastrigin, himmelblau, htable, rosenbrock
from numpy import sin, cos, e
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
domain = 10
f = himmelblau
fig = plt.figure()
ax = p3.Axes3D(fig)
# Make data.
X = Y = np.arange(-domain, domain, 0.1)
X, Y = np.meshgrid(X, Y)
#Z = (e**(cos(Y) * sin(X) * 2)  +  X + Y + sin(X) * 5)**3
#Z = sin(X) * cos(Y)
Z = f(X,Y)
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.jet, alpha=1,
                       linewidth=0, antialiased=False)

particles = []
plottels = []
for i in range(50):
    p = Particle(0.5,0.5, 0.75, domain * 2, f)
    particles += [p]
    plottels += ax.plot([p.position[0]], [p.position[1]], [f(p.position[0], p.position[1])], "o", c="k", markersize=2)
x = y = z = []
text = ax.text2D(0.05, 0.90, "Best Value {:.7f}\nAt ({:.3f},{:.3f})".format(f(Particle.p_glob[0], Particle.p_glob[1]), Particle.p_glob[0], Particle.p_glob[1]), transform=ax.transAxes, bbox=dict(facecolor='red', alpha=0.5))

frames = 100

def animate(i, plottels):
    text.set_text("Best Value: {:.7f}\nAt ({:.3f},{:.3f})".format(f(Particle.p_glob[0], Particle.p_glob[1]), Particle.p_glob[0], Particle.p_glob[1]))
    if i == frames - 1:
        plt.close()
    #fig.savefig('animations\\rosenbrock{}.svg'.format(i), format='svg', dpi=1200)
    for n in range(len(plottels)):
        particles[n].step(True)
        p = plottels[n]
        p.set_data([particles[n].position[0], particles[n].position[1]])
        p.set_3d_properties(f(particles[n].position[0], particles[n].position[1]))
    return plottels,

anim = animation.FuncAnimation(fig, animate, frames=frames, repeat=False, interval=100, fargs=(plottels,))
#anim.save('rastrigin.mp4', fps=10, extra_args=['-vcodec', 'libx264'])
plt.show()