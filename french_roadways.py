import geopandas as gpd
import matplotlib.pyplot as plt


europe = gpd.read_parquet("./europe.parquet.gz")

fig, ax = plt.subplots(facecolor="#090909")
europe.plot(ax=ax, column="GP_RTP", cmap="inferno_r", lw=0.5)
ax.axis("off")
ax.set_xlim(-12.5, 30)
ax.set_ylim(35, 73)
plt.show()
