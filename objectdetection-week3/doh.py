from skimage import feature, color, io
import matplotlib.pyplot as plt
 
image = color.rgb2gray(io.imread("polka_dots_2.jpg"))
blobs_doh = feature.blob_doh(image, max_sigma=30, threshold=0.01)
 
# Display
fig, ax = plt.subplots()
ax.imshow(image, cmap='gray')
for y, x, r in blobs_doh:
    c = plt.Circle((x, y), r, color='blue', linewidth=2, fill=False)
    ax.add_patch(c)
plt.show()