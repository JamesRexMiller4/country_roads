from shapely.geometry import LineString
import matplotlib.pyplot as plt
import numpy as np

linestring = LineString([[2, 1], [1, 2], [1, 3], [0, 4]])
middle = linestring.length / 2
interpolated_linestring = linestring.interpolate(middle)


plt.plot(linestring.xy[0], linestring.xy[1], color="orange")
plt.scatter(linestring.xy[0], linestring.xy[1], s=200, color="orange", edgecolor="black")
plt.scatter(interpolated_linestring.x, interpolated_linestring.y, s=200, edgecolor="black")
plt.grid(ls="--", lw=1, alpha=0.6)
plt.xticks(np.arange(-1, 4, 1))
plt.yticks(np.arange(0, 6, 1))
plt.show()
