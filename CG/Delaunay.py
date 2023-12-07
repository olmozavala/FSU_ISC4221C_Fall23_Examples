# %% 
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

# Generate some random points
np.random.seed(0)  # Seed for reproducibility
points = np.random.rand(30, 2)  # 30 points in 2 dimensions
print(points)

# Compute Delaunay triangulation
triangulation = Delaunay(points)

# %% Plotting

print(triangulation.simplices)
# %% Plotting
plt.triplot(points[:, 0], points[:, 1], triangulation.simplices)
plt.plot(points[:, 0], points[:, 1], 'ro')  # Plot the points

plt.show()
