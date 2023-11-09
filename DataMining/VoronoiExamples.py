# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay

# Generate random points as seeds for the Voronoi regions
points = np.random.rand(10, 2)  # 10 random points in 2D

# Draw the points with scatter
plt.scatter(points[:,0], points[:,1])
plt.show()

# %%
# Compute Voronoi tessellation
vor = Voronoi(points)

# Compute Delaunay triangulation
tri = Delaunay(points)

# Plot
fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='orange', line_width=2, line_alpha=0.6, point_size=2)
# Plot Delaunay triangulation on top of Voronoi diagram
ax.triplot(points[:, 0], points[:, 1], tri.simplices, 'b-')

# Optionally, add the points as black dots
ax.plot(points[:,0], points[:,1], 'ko')

plt.show()
