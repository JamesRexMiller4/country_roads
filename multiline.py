from shapely.geometry import MultiLineString
import matplotlib.pyplot as plt
import numpy as np

multiline_string = MultiLineString([[[5, -1], [4, 0], [4, 2], [5, 3]], [[1, 2], [2, 3], [2, 5], [3, 6]]])

for geom in multiline_string.geoms:
    plt.plot(geom.xy[0], geom.xy[1], color="orange")
    plt.scatter(geom.xy[0], geom.xy[1], s=200, color='orange', edgecolor='black')
    plt.grid(ls="--", lw=1, alpha=0.6)
    plt.xticks(np.arange(0, 7, 1))  
    plt.yticks(np.arange(-2, 8, 1))
    plt.show()
