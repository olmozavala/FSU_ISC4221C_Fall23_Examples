# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
npos = 40
d = 100 # Dimension of the embedding

fig, ax = plt.subplots(figsize=(20, 5))
allpos = []
for p in range(0, npos): # p = position

    # sinpos = [np.sin(p/(10000**(2*(i/d)))) if i%2 == 0 else np.cos(p/(10000**(2*(i)/d)))
                # for i in range(1, d+1)]
    sinpos = [np.sin(p/(10000**(2*i/d))) for i in range(1, d+1)]

    start = 10
    end = 20
    # start = 0
    # end = len(sinpos)
    # allpos.append(sinpos)
    ax.scatter(np.arange(start, end), sinpos[start:end], label=f'Position {p}')
    ax.set_xlabel('Embedding dimension', fontsize=20)
    # set the x axis ticks values

# allpos = np.array(allpos)
# ax.imshow(allpos[:,0:30], cmap='hot', interpolation='nearest')
ax.set_title(f'Sinosoidal Positional Encoding d={d} maxp = {npos} ', fontsize=20)
# ax.legend(fontsize=14)
plt.show()
# %%
