# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
def plot_line(ax, by, c, figax, xlims=[0, 10], ylims=[0, 10]):
    if by == 0:
        figax.axvline(x=ax, color='black')
    else:
        x = np.linspace(xlims[0], xlims[1], 100)
        y = (c - ax*x)/by
        figax.plot(x, y, color='black')
        # Set x and y limits
        figax.set_xlim(xlims)
        figax.set_ylim(xlims)

def get_Z(xlims, ylims, ax, by, c):
    x = np.linspace(xlims[0], xlims[1], 100)
    y = np.linspace(ylims[0], ylims[1], 100)
    X, Y = np.meshgrid(x, y)
    return  ax*X + by*Y + c

# %% Slide 31
fig, axs = plt.subplots(1, 1, figsize=(10, 10))
xlims = [0, 2]
ylims = [0, 2]
z = get_Z(xlims, ylims, 1, 2, 0)
axs.imshow(z, cmap='gray', extent=[*xlims, *ylims], origin='lower')
plot_line(1, 0, 1, axs, xlims)
plot_line(0, 1, 1, axs, xlims)
plot_line(1, 1, 1.5, axs, xlims)
plt.show()

# %% Slide 33
fig, axs = plt.subplots(1, 1, figsize=(10, 10))
xlims = [0, 6]
ylims = [0, 6]
z = get_Z(xlims, ylims, 2, 3, 0)
axs.imshow(z, cmap='gray', extent=[*xlims, *ylims], origin='lower')
plot_line(3, 1, 6, axs, xlims)
plot_line(1, 1, 4, axs, xlims)
plot_line(1, 2, 6, axs, xlims)
plt.show()

# %% Slide 36
fig, axs = plt.subplots(1, 1, figsize=(10, 10))
xlims = [0, 6]
ylims = [0, 6]
z = get_Z(xlims, ylims, 1, 4, 0)
axs.imshow(z, cmap='gray', extent=[*xlims, *ylims], origin='lower')
plot_line(1, -1, 1, axs, xlims)
plot_line(-2, -1, -8, axs, xlims)
plt.show()