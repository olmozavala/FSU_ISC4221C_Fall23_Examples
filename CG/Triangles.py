# %%
import numpy as np 
import matplotlib.pyplot as plt

a = np.array([4,1])
b = np.array([8,3])
c = np.array([0,9])
# %% Plot the triangle

plt.plot(a[0], a[1], 'o')
plt.plot(b[0], b[1], 'o')
plt.plot(c[0], c[1], 'o')
# Show the vertices labels
plt.text(a[0], a[1]+0.2, 'A')
plt.text(b[0], b[1]+0.2, 'B')
plt.text(c[0], c[1]+0.2, 'C')
plt.axis('square')
plt.axis([-1,10,0,10])
# Fill the triangle
plt.fill([a[0],b[0],c[0]],[a[1],b[1],c[1]], alpha=0.2)
plt.grid()

# %% ------------ Sides
ab = np.linalg.norm(b-a)
ac = np.linalg.norm(c-a)
bc = np.linalg.norm(c-b)
# print the sides
print(f"ab = {ab:.2f}, bc = {bc:.2f}, ca = {ac:.2f}")

# %% ------------ Angles
alpha = np.arccos((ab**2 + ac**2 - bc**2) / (2 * ab * ac))
beta = np.arccos((ab**2 + bc**2 - ac**2) / (2 * ab * bc))
gamma = np.arccos((ac**2 + bc**2 - ab**2) / (2 * ac * bc))

# Convert radians to degrees
alpha_deg = np.degrees(alpha)
beta_deg = np.degrees(beta)
gamma_deg = np.degrees(gamma)

print(f"alpha = {alpha_deg:.2f} degrees, beta = {beta_deg:.2f} degrees, gamma = {gamma_deg:.2f} degrees")

# %% ----------- Area
# with determinant
area = 0.5 * abs(np.linalg.det(np.column_stack((a-c, b-c))))
print(f"Area = {area:.2f}")
# with cross product
area = 0.5 * np.linalg.norm(np.cross(a-c, b-c))
print(f"Area = {area:.2f}")

# %% ----------- Orientation
# The orientation of the triangle is the sign of the determinant
# of the matrix formed by the vectors ab and ac
orientation = np.linalg.det(np.column_stack((a-b, a-c)))
# orientation = np.linalg.det(np.column_stack((b-a, b-c)))
if orientation > 0:
    print("The triangle is oriented counter-clockwise")
else:
    print("The triangle is oriented clockwise")

# %% ----------- Inside or outside
# The point P is inside the triangle if the sum of the areas of the triangles
# PAB, PBC and PAC is equal to the area of the triangle ABC
p_tests = np.array([[5,5],[8,5]])
# Plot the point P
for i, P in enumerate(p_tests):
    plt.plot(P[0], P[1], 'o')
    plt.text(P[0], P[1]+0.2, f'P{i+1}')
# Fill the triangle
plt.fill([a[0],b[0],c[0]],[a[1],b[1],c[1]], alpha=0.2)
plt.grid()
# %%
def line_side(p1, p2, p):
    # Returns a boolean 1 if p is on the left of v12 = p2-p1
    # o otherwise
    v1 = p2 - p1
    v2 = p - p1
    nv = np.array([-v1[1], v1[0]])
    t = np.dot(nv, v2)
    side = (0 <= t)
    return side

def triangle_contains( tri, p):
    contains = (line_side(tri[0], tri[1], p) and  
                line_side(tri[1], tri[2], p) and 
                line_side(tri[2], tri[0], p))
    return contains
    
tri = [a,b,c]
# Check if P is inside the triangle
for i, P in enumerate(p_tests):
    print(f"P{i+1} ({P}) is inside the triangle: {triangle_contains(tri, P)}")
# %%
