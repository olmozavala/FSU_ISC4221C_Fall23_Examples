# %%
import numpy as np

# NDarray generation
x = np.array([1,2,3,4,5])
y = np.random.randint(0, 10, size=(10,5))
print(type(x))
# %%
print(x.mean())
print(x.max())
print(x.min())
# %%
print(x*2 + 5)

# %% Indexing
print(y)
# print(y[0,0])
print(f"Third row: {y[2,:]}")
print(f"Third row (middle elements): {y[2,1:3]}")
print(f"Second column : {y[:,1]}")



# %%
