# %% Thiscode exemplifies the Central Limit Theorem (CLT) by generating a
# histogram of mulitple dice thrown
import numpy as np
import matplotlib.pyplot as plt

n = 10 # Number of dices thrown
N = 10000 # Number of times the dice is thrown

rand_values = np.random.randint(1,7,(n,N)) # Generate random values

sum_rand_values = np.sum(rand_values, axis=0)/n # Sum the values of each throw

# %%
plt.hist(sum_rand_values, bins=100, density=True) # Plot histogram
plt.xlabel('Sum of dice values')
plt.ylabel('Probability')
plt.title(f'Central Limit Theorem. Mean: {np.mean(sum_rand_values):.2f} Variance: {np.var(sum_rand_values):.2f}')
plt.show()