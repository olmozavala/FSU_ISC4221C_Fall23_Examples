# %%
import numpy as np
import matplotlib.pyplot as plt

# Similate MCM for solving the integral xsin(x)dx from 0 to pi

# Define the function to be integrated
def myf(x):
    return x*np.sin(x)

# Define the integral limits
a = 0
b = np.pi

# Define the number of points to be used
N = 100000

# Generate random values
rand_values = np.pi*np.random.rand(N)

# Calculate the integral
integral = np.mean(myf(rand_values))*(b-a)

# Print the result
print(f'The integral of xsin(x)dx from {a} to {b:.2f} is {integral:.2f}')
# %%

# --------  Error comparison -------

# Compare MCM with an estimate of equispaced points

N = np.logspace(2,5,100).astype(int) # Number of points to be used

# Generate random values
mcm = []
mcm_u = []
for n in N:
    rand_values = np.pi*np.random.rand(n)
    rand_values_u = np.linspace(a,b,n)

    # Calculate the integral
    mcm.append(np.abs(np.pi - np.mean(myf(rand_values))*(b-a)))
    mcm_u.append(np.abs(np.pi -np.mean(myf(rand_values_u))*(b-a)))

# plot the results
plt.figure(figsize=(8,4))
plt.plot(N, mcm, label='MCM')
plt.plot(N, mcm_u, label='Uniform')
plt.plot(N, N**(-1/2), '--', label='-1/2 Power')
plt.xlabel('Number of points')
plt.ylabel('Absolute error')
# Increase the lines in the grid
plt.legend()
plt.grid()
# Make y axis logarithmic
plt.yscale('log')
plt.xscale('log')
plt.show()


# %% --------  Area on the integral comparison -------
# Here we compute the area inside a circle of radius 1 using MCM

# Define the function to be integrated
def myfcircle(x,y):
    return np.sqrt(x**2+y**2)<1

# Define the integral limits
a = -1
b = 1

# Define the number of points to be used
N = 1000

# Generate random values
rand_values_x = -1 + 2*np.random.rand(N)
rand_values_y = -1 + 2*np.random.rand(N)

integral = np.mean(myfcircle(rand_values_x,rand_values_y))*(b-a)*2

# Print the result
print(f'The area of the circle is {integral:.2f} vs {np.pi:.2f}')

# Plot the values of x and y
plt.scatter(rand_values_x, rand_values_y, marker='.')
idxs = myfcircle(rand_values_x,rand_values_y)
plt.scatter(rand_values_x[idxs], rand_values_y[idxs], c='r', marker='.')
plt.axis('equal')
plt.show()

# %% -------- Simulate Secretary problem -------
# 
# The secretary problem is a problem that demonstrates a scenario involving
# optimal stopping theory. The problem has been studied extensively in the
# fields of applied probability, statistics, and decision theory. It is also
# known as the marriage problem
# 
# Define the number of candidates
N = 10
num_sim = 1000
# Generate random values
# Random permutation
for cur_sim in range(num_sim):
    rand_values = np.random.permutation(np.arange(N))
    # Find the maximum value
    max_value = np.max(rand_values)
    # Find the index of the maximum value
    max_index = np.argmax(rand_values)
    # Print the result
    # print(f'The maximum value is {max_value:.2f} and the index is {max_index}')
    found_max = np.zeros((num_sim,N))
    for look_phase_n in range(1,N):
        # Print the result
        look_max = np.max(rand_values[:look_phase_n])
        # Get the first index with the value above the maximum
        first_index = np.where(rand_values[look_phase_n:]>look_max)[0]
        print(f'Look phase {look_phase_n}: Maximum in LP: {look_max}')
        if len(first_index) == 0:
            first_index = N-1 # Last index
        else:
            first_index = first_index[0]


        # print(f'Found index {first_index} with value {rand_values[first_index]}')
        if first_index == max_index:
            found_max[cur_sim,look_phase_n] = 1
            print(f'Found max: {cur_sim} - {look_phase_n}')

# %% Print the results

fig, axs = plt.subplots(1,2, figsize=(8,4))
axs[0].plot(np.mean(found_max,axis=0))
axs[0].set_xlabel('Look phase')
axs[0].set_ylabel('Probability of finding the maximum')
axs[0].grid()
axs[1].plot(np.cumsum(np.mean(found_max,axis=0)))
axs[1].set_xlabel('Look phase')
axs[1].set_ylabel('Probability of finding the maximum')
axs[1].grid()
plt.show()
