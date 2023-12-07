# %%
import sympy as sp

# Define a matrix
A = sp.Matrix([
    [1, 0, 1, 0, 1, 0],
    [0, -1, -1, 0, -1, -1],
    [1, 2, 2, 1, 1, 1]
])

# Compute the Reduced Row Echelon Form
rref, pivot_columns = A.rref()

print("The Reduced Row Echelon Form is:")
print(rref)
print("Pivot columns are:")
print(pivot_columns)

# %%
