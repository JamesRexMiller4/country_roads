import geopandas as gpd
import matplotlib.pyplot as plt


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

roads = gpd.sjoin(europe, gdf, predicate='within')

fig, ax = plt.subplots()
roads.plot(ax=ax, lw=0.25)
ax.axis('off')
plt.show()
