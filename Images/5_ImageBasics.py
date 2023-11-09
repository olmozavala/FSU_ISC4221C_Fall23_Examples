# %%
import imageio
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
import numpy as np

# Read the image using imageio
# img = imageio.imread('figs/snap.png')
img = imageio.imread('figs/noise.png')
img_2d = img[:,:,0]

# %%

ksize = 10
kernel = np.ones((ksize,ksize))/ksize**2

print(kernel.shape)
print(img_2d.shape)
# Convolve the image with the kernel
img_conv = convolve2d(img_2d, kernel, mode='same', boundary='symm')
fig, axs = plt.subplots(1, 2, figsize=(15,15))
axs[0].imshow(img_2d, cmap='gray')
axs[1].imshow(img_conv, cmap='gray')
plt.show()

# %%
ksize = 3
kernel_h = np.array([[-1,0,1],
                   [-1,0,1],
                   [-1,0,1]])

kernel_v = np.array([  [-1,-1,-1],
                       [0,0,0],
                       [1,1,1]])


print(kernel.shape)
print(img_2d.shape)
# Convolve the image with the kernel
img_conv_h = convolve2d(img_2d, kernel_h, mode='same', boundary='symm')
img_conv_v = convolve2d(img_2d, kernel_v, mode='same', boundary='symm')
both = np.sqrt(img_conv_h**2 + img_conv_v**2)

fig, axs = plt.subplots(1, 2, figsize=(15,15))
axs[0].imshow(img_2d, cmap='gray')
axs[1].imshow(both, cmap='gray')
plt.show()

# %%

# plt.imshow(img, cmap='gray')
# plt.show()
# # %% 
# type(img)
# print(img.shape)

# # %% ---- Contrast streching

# # %%
# def contrast_streching(img):
#     min = img.min()
#     max = img.max()
#     range = float(max - min)
#     # new_image = 255 * ((img - min) / range)
#     new_image = 255.0 * (img - min)/range 
#     print(img.min(), img.max())
#     print(new_image.min(), new_image.max())
#     return new_image

# new_image = contrast_streching(img)
# print(new_image.min(), new_image.max())
# print(type(new_image))
# fig, axs = plt.subplots(1, 2)
# axs[0].imshow(img, cmap='gray', vmin=0, vmax=255)
# axs[1].imshow(new_image, cmap='gray', vmin=0, vmax=255)
# plt.show()

# %%
orig_img = imageio.imread('figs/aquabmx1.png')
img = imageio.imread('figs/aquabmx1.png')

dims = img.shape
print(dims)
s = 1.5 # Scale factor
# Iterate over the image with two loops
for i in range(1, dims[0]-1):
    for j in range(1, dims[1]-1):
        cmean_r = img[i-1:i+2, j-1:j+2,0].mean()
        cmean_g = img[i-1:i+2, j-1:j+2,1].mean()
        cmean_b = img[i-1:i+2, j-1:j+2,2].mean()
        dif_r = img[i,j,0] - cmean_r
        dif_g = img[i,j,1] - cmean_g
        dif_b = img[i,j,2] - cmean_b
        # print(dif_r)

        # img[i,j,0] = np.max([255,s*dif_b + img[i,j,0]]).astype(np.uint8)
        # img[i,j,1] = np.max([255,s*dif_b + img[i,j,1]]).astype(np.uint8)
        # img[i,j,2] = np.max([255,s*dif_b + img[i,j,2]]).astype(np.uint8)

        img[i,j,0] = s*dif_r + cmean_r
        img[i,j,1] = s*dif_g + cmean_g
        img[i,j,2] = s*dif_b + cmean_b

fig, axs = plt.subplots(1,2, figsize=(10,10))
axs[0].imshow(orig_img, cmap='gray', vmin=0, vmax=255)
axs[1].imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()


# %%
# Display the image using matplotlib
# The dimentions are 378, 547, 3
# plt.imshow(img)
# Put it in grayscale
gray = img[:,:,0]
invgray = 255 - gray
plt.imshow(invgray, cmap='gray')
temp = img.copy()
# %%
# temp[:,:,1:3] = 0  # We are setting G and B to zero
# temp = 255 - temp
plt.imshow(temp)
plt.axis('off')  # Turn off axis numbers and ticks
plt.show()

# %%
