# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a simple binary image with a white square in the middle
image = np.zeros((100, 100), np.uint8)
image[25:75, 25:75] = 255
image[40:46,40:46] = 0

# Create a kernel for morphological operations
kernel = np.ones((10,10), np.uint8)

fig, axs = plt.subplots(1, 2, figsize=(12, 8))
axs[0].imshow(image, cmap='gray')
axs[0].set_title('Original Image')
axs[1].imshow(kernel, cmap='gray', vmin=0, vmax=1)
axs[1].set_title('Kernel')
plt.show()

# %%


# Apply dilation
dilated = cv2.dilate(image, kernel, iterations=1)

# Apply erosion
eroded = cv2.erode(image, kernel, iterations=1)

# Apply opening (erosion followed by dilation)
opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Apply closing (dilation followed by erosion)
closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Plot the original and processed images
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(2, 3, 2)
plt.title('Dilated Image')
plt.imshow(dilated, cmap='gray')

plt.subplot(2, 3, 3)
plt.title('Eroded Image')
plt.imshow(eroded, cmap='gray')

plt.subplot(2, 3, 4)
plt.title('Opened Image')
plt.imshow(opened, cmap='gray')

plt.subplot(2, 3, 5)
plt.title('Closed Image')
plt.imshow(closed, cmap='gray')

plt.show()

# %%
