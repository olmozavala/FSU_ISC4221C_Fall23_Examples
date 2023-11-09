# %%
import imageio
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
import numpy as np
import cv2

# %% Plot together
def myplot(orig, current, title=""):
    fig, axs = plt.subplots(1,2, figsize=(10,5))
    axs[0].imshow(orig)
    axs[1].imshow(current)
    if title != "":
        plt.title(title)
    plt.show()

# Read the image using imageio
img = imageio.imread('figs/ex.png')
myplot(img, img)

# %% Gaussian filter with openCV
blur_size = 11 
blurred_image = cv2.GaussianBlur(img, (blur_size, blur_size), 0)
myplot(img, blurred_image)

# %% Plot histogram of image
plt.hist(blurred_image[:,:,0].flatten(), bins=50)
plt.show()

# %% Thresholding
th_img = blurred_image[:,:,0] < 120
myplot(img, th_img)


# %% Morphological operations
size = 10
kernel = np.ones((size,size), np.uint8)

closed_im = cv2.morphologyEx(th_img.astype(np.uint8), cv2.MORPH_CLOSE, kernel)
myplot(closed_im, img)
# %% Connected components
num_labels, labels = cv2.connectedComponents(closed_im)

myplot(img, labels, f"Number of labels: {num_labels}")
