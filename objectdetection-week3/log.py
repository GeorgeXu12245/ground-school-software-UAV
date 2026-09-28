from skimage import feature, color, io
import matplotlib.pyplot as plt
import cv2
import numpy as np

image = color.rgb2gray(io.imread("polka_dots_2.jpg"))
image = cv2.GaussianBlur(image, (7, 7), 0)
blobs_log = feature.blob_log(image, max_sigma=100, num_sigma=30, threshold=0.14)

image_inverted = 1 - image
blobs_log_inverted = feature.blob_log(image_inverted, max_sigma=100, num_sigma=30, threshold=0.14)
# Compute radii
all_blobs = np.vstack((blobs_log, blobs_log_inverted))
all_blobs[:, 2] = all_blobs[:, 2] * (2 ** 0.5)
 
# Display
fig, ax = plt.subplots()
ax.imshow(image, cmap='gray')
for y, x, r in all_blobs:
    c = plt.Circle((x, y), r, color='red', linewidth=2, fill=False)
    ax.add_patch(c)
plt.show()