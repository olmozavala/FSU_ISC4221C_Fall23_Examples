# %%
from shapely.geometry import Point, LineString, Polygon
import matplotlib.pyplot as plt
import numpy as np

# %% ----------- Points -------------
points = [Point(0, 0), Point(1, 1), Point(0, 1), Point(1, 0)]

# Plotting
fig, ax = plt.subplots()
ax.scatter([p.x for p in points], [p.y for p in points], marker='o', color='red')
ax.set_aspect('equal', adjustable='box')
plt.title('Point')
plt.show()

# %% ----------- Lines -------------
# Create a line
line = LineString([(0, 0), (1, 1), (2, 1)])

# Plotting
fig, ax = plt.subplots()
x, y = line.xy
ax.plot(x, y, color='blue', linewidth=3, solid_capstyle='round', zorder=2)
ax.set_aspect('equal', adjustable='box')
plt.title('Line')
plt.show()


# %% ----------- Polygon -------------
# Create a polygon
polygon = Polygon([(0, 0), (1, 1), (1, 0)])

# Plotting
fig, ax = plt.subplots()
x, y = polygon.exterior.xy
ax.fill(x, y, alpha=0.5, fc='green', ec='black')
ax.set_aspect('equal', adjustable='box')
plt.title('Polygon')
plt.show()


# %% ----------- Example -------------
p1 = np.array([0, 4])
p2 = np.array([3, 1])
x, y = zip(*(p1, p2))
v = p2 - p1
print(v)

fig, ax = plt.subplots()
ax.plot(x, y, alpha=0.5)
ax.scatter(x, y, alpha=0.5, fc='green', ec='black')
# ax.scatter(0, 4, alpha=0.5, fc='green', ec='black')
ax.set_aspect('equal', adjustable='box')
plt.title('Polygon')
plt.show()

# %% ----------- line_parameter_s -------------
def line_parameter_s( p1, p2, p):
  v1 = (p2 - p1)
  v2 = (p  - p1)
  s  = np.dot(v2,v1) / np.dot(v1,v1)

  return s

p1 = np.array([0, 4])
p2 = np.array([3, 1])
# p = np.array([-2, 6])
# p = np.array([3, 1])
# p = np.array([1.5, 2.5])
# p = np.array([2.3, 1.3])
# print(line_parameter_s(p1, p2, p))
p = np.array([[-2, 6], [4, 0], [2, 2], [1, 3], [3, 1]])
print(line_parameter_s(p1, p2, p))

# %% Multiple points
p = np.array([[-2, 6], [4, 0], [2, 2], [1, 3], [3, 1]])
print(line_parameter_s(p1, p2, p))

# %% Point outside of line
p = np.array([-2, 6.1])
print(line_parameter_s(p1, p2, p))

# %% Vectorization operation

x = np.array([1, 2, 3, 4, 5])
y = 5

print(x * y)