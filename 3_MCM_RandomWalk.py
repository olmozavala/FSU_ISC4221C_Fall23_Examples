# %% --------- Random-
import numpy as np
import matplotlib.pyplot as plt

# Initialize parameters
n_steps = 1000  # Number of steps
x = np.zeros(n_steps)  # x-coordinate
y = np.zeros(n_steps)  # y-coordinate

# Initialize random seed for reproducibility
# np.random.seed(0)

# Perform the random walk
for i in range(1, n_steps):
    # theta = 2 * np.pi * np.random.rand()  # Random angle between 0 and 2*pi
    # dx = np.cos(theta)  # Change in x
    # dy = np.sin(theta)  # Change in y

    dx = np.random.randn()  # Change in x
    dy = np.random.randn()  # Change in y

    # dx = np.random.choice([-1, 1])  # Change in x
    # dy = np.random.choice([-1, 1])  # Change in y
    
    x[i] = x[i-1] + dx  # Update x-coordinate
    y[i] = y[i-1] + dy  # Update y-coordinate

# Plotting
plt.figure(figsize=(10, 10))
plt.plot(x, y, marker="o")
plt.plot(x[0], y[0],c='r', marker="o")
plt.title("2D Random Walk")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# %%
