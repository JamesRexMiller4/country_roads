import geopandas as gpd
import matplotlib.pyplot as plt
from shapely import Point, LineString
import numpy as np


europe = gpd.read_parquet("./europe.parquet.gz")
# Europe's Roadways
# fig, ax = plt.subplots(facecolor="#090909")
# europe.plot(ax=ax, column="GP_RTP", cmap="inferno_r", lw=0.5)
# ax.axis("off")
# ax.set_xlim(-12.5, 30)
# ax.set_ylim(35, 73)
# plt.show()

df = gpd.read_file("./ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp")
gdf = df.loc[df['ADMIN'] == 'France']
gdf2 = gpd.GeoDataFrame({'geometry': [Point(2.3522, 48.8466)]}, crs="EPSG:4326")

roads = gpd.sjoin(europe, gdf, predicate='within')

distances = roads.distance(gdf2.iloc[0].geometry)

roads['distance2paris'] = distances
print(roads)

roads['distance2paris_lw'] = 1 / np.exp(roads['distance2paris'])

leftSpan = np.amax(roads['distance2paris_lw']) - np.amin(roads['distance2paris_lw'])
rightSpan = 0.9 - 0.05
valueScaled = (roads['distance2paris_lw'] - np.amin(roads['distance2paris_lw'])) / leftSpan
roads['distance2paris_lw'] = 0.05 + (valueScaled * rightSpan)

fig, ax = plt.subplots(facecolor="#090909")
roads.plot(ax=ax, column="GP_RTP", cmap="afmhot_r", lw=roads['distance2paris_lw'])
ax.axis('off')
plt.show()
