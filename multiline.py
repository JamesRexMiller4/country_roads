from shapely.geometry import MultiLineString, LineString, Point
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd

lines_df = pd.DataFrame({
    "start_lat": [1, 9],
    "start_long": [1, 1],
    "end_lat": [9, 1],
    "end_long": [9, 9],
    "lines": [
        "a",
        "b"
    ]
})

geometry = [
    LineString([Point(start_lat, start_long), Point(end_lat, end_long)])
    for start_lat, start_long, end_lat, end_long in zip(
        lines_df.start_lat, lines_df.start_long, lines_df.end_lat, lines_df.end_long
    )
]

lines_gdf = gpd.GeoDataFrame(lines_df, crs="EPSG:4326", geometry=geometry)

print(lines_gdf)



multiline_string = MultiLineString([[[5, -1], [4, 0], [4, 2], [5, 3]], [[1, 2], [2, 3], [2, 5], [3, 6]]])

for geom in multiline_string.geoms:
    plt.plot(geom.xy[0], geom.xy[1], color="orange")
    plt.scatter(geom.xy[0], geom.xy[1], s=200, color='orange', edgecolor='black')
    plt.grid(ls="--", lw=1, alpha=0.6)
    plt.xticks(np.arange(0, 7, 1))
    plt.yticks(np.arange(-2, 8, 1))
    plt.show()
