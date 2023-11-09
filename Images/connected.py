# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a binary image with some connected components
image = np.zeros((10, 10), dtype=np.uint8)
image[2:5, 2:5] = 1  # Square
image[7:9, 7:9] = 1  # Another square
image[3:6, 7:9] = 1  # Rectangle

# Label connected components
retval, labels, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=8)

# Create an output image to visualize the labels
output_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

# Assign colors to each label (connected component)
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0)]
for i in range(1, retval):  # Skip the background label 0
    output_image[labels == i] = colors[i % len(colors)]

# Plot original and labeled images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Binary Image")
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Labeled Components")
plt.imshow(output_image)

plt.show()

# Output stats and centroids
print("Component statistics: ", stats)
print("Component centroids: ", centroids)

# %%
