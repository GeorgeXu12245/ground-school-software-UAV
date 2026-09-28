from skimage import feature, color, io
import matplotlib.pyplot as plt
 
image = color.rgb2gray(io.imread("polka_dots_2.jpg"))
blobs_dog = feature.blob_dog(image, max_sigma=50, threshold=0.13)
 
# Compute radii
blobs_dog[:, 2] = blobs_dog[:, 2] * (2 ** 0.5)
 
# Display
fig, ax = plt.subplots()
ax.imshow(image, cmap='gray')
for y, x, r in blobs_dog:
    c = plt.Circle((x, y), r, color='lime', linewidth=2, fill=False)
    ax.add_patch(c)
plt.show()