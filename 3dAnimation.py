from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation
from numpy import e

fig = plt.figure()
ax = p3.Axes3D(fig)
# Setting the axes properties
ax.set_zbound(1, 10)
# create the parametric curve
t = np.arange(0, 21*np.pi, 2*np.pi/100)
x = np.cos(t)
y = np.sin(t)
z = (1.5*t / (2.0 * np.pi)) - 2

# create the first plot
points = []
for i in range(8):
    points += ax.plot([x[i]], [y[i]], [z[i]], 'o', c='crimson'),
line, = ax.plot(x, y, z, c='k', alpha=0.5)
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 15])

# second option - move the point position at every frame
def update_point(n, x, y, z, points):
    offset = 0
    for p in points:
        if n + offset >= len(x):
            break
        p = p[0]
        p.set_data(np.array([x[n + offset], y[n + offset]]))
        p.set_3d_properties(z[n + offset], 'z')
        offset += 25
    return points

anim=animation.FuncAnimation(fig, update_point, frames=1050, interval=10,  fargs=(x, y, z, points))
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()

