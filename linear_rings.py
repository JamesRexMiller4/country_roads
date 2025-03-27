from shapely.geometry import LinearRing
import matplotlib.pyplot as plt
import numpy as np

linear_ring = LinearRing([[-2, 3], [-2, 6], [3, 6], [3, 3]])

plt.plot(linear_ring.xy[0], linear_ring.xy[1], color="orange")
plt.scatter(linear_ring.xy[0], linear_ring.xy[1], s=200, color="orange", edgecolor='black')
plt.grid(ls="--", lw=1, alpha=0.6)
plt.xticks(np.arange(-3, 5, 1))
plt.yticks(np.arange(2, 8, 1))
plt.show()
