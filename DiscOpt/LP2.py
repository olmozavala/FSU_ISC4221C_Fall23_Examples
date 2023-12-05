# %%
import sympy as sp

# Define a matrix
A = sp.Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Compute the Reduced Row Echelon Form
rref, pivot_columns = A.rref()

print("The Reduced Row Echelon Form is:")
print(rref)
print("Pivot columns are:")
print(pivot_columns)

# %%
