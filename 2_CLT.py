# %% Thiscode exemplifies the Central Limit Theorem (CLT) by generating a
# histogram of mulitple dice thrown
import numpy as np
import matplotlib.pyplot as plt

n = 5# Number of dices thrown
N = 10000 # Number of times the dice is thrown
nbins = 6*n -(n-1)

rand_values = np.random.randint(1,7,(n,N)) # Generate random values

fig, axs = plt.subplots(1,2, figsize=(8,4))
sum_rand_values = np.sum(rand_values, axis=0) # Sum the values of each throw

axs[0].hist(sum_rand_values, bins=nbins) # Plot histogram
axs[0].set_xlabel(f'Sum of dice values (n={n})')
axs[0].set_ylabel('Count')
axs[0].set_title(f'Sum of distributions')

sum_rand_values = np.sum(rand_values, axis=0)/n # Sum the values of each throw
axs[1].hist(sum_rand_values, bins=nbins) # Plot histogram
axs[1].set_xlabel(f'Mean of sum of dice values (n={n})')
axs[1].set_ylabel('Count')
axs[1].set_title(f'CLT. Mean: {np.mean(sum_rand_values):.2f} Variance: {np.var(sum_rand_values):.2f}')
plt.show()
