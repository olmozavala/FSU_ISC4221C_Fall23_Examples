# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Generate synthetic data: 30 random points in 2-D
np.random.seed(0)  # Seed for reproducibility
points = np.random.rand(30, 2)  # 30 points in 2 dimensions
print(points)

# %% Compute the convex hull
hull = ConvexHull(points)
print(hull.vertices)

# %%
plt.plot(points[:,0], points[:,1], 'o')  # plot the points
for simplex in hull.simplices:
    print(simplex)
    plt.plot(points[simplex, 0], points[simplex, 1], 'r-') # plot the convex hull

plt.show()

# %%
