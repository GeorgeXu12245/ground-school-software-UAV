'''
import cv2

# 1. Load the original image
image = cv2.imread('objects.jpg')
image = cv2.GaussianBlur(image, (5, 5), 0)
# 2. Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Apply binary thresholding
_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# 4. Find contours
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)

# 5. Draw contours on a copy of the original image
image_contours = image.copy()
cv2.drawContours(image_contours, contours, -1, (0, 255, 0), 2)

# Display the result
cv2.imshow('Contours', image_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
import cv2
import numpy as np

# Load your image
# Make sure your input image matches your HSV color bounds
image = cv2.imread('objects.jpg')
output = image.copy()

# Step 1: Smooth the image to remove background texture/noise
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Step 2: Convert to HSV color space
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

# Step 3: Define color ranges (Example: Tuning for Orange Cones/Objects)
# Note: You can create separate masks for different colors if your objects are different colors!
lower_color = np.array([5, 100, 100])
upper_color = np.array([25, 255, 255])
mask = cv2.inRange(hsv, lower_color, upper_color)

# Clean up the mask using morphology (fills small holes and removes tiny specks)
kernel = np.getStructuringElement(cv2.MORPH_RECT, (5, 5))
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Step 4: Find Contours with RETR_TREE to capture internal structures (crucial for rings)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Ensure hierarchy exists before processing
if hierarchy is not None:
    hierarchy = hierarchy[0]  # Flatten to a 2D array
else:
    hierarchy = []

# Step 5: Loop through each detected contour and classify it
for i, cnt in enumerate(contours):
    # Filter out tiny noise contours based on a minimum pixel area
    area = cv2.contourArea(cnt)
    if area < 500:
        continue

    # Calculate perimeter (arc length) - True means the contour is closed
    perimeter = cv2.arcLength(cnt, True)
    
    # Approximate the shape to simplify its geometry/vertices
    epsilon = 0.03 * perimeter
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    num_vertices = len(approx)

    # Calculate circularity metric
    circularity = 0
    if perimeter > 0:
        circularity = (4 * np.pi * area) / (perimeter ** 2)

    # --- CLASSIFICATION LOGIC ---
    
    # 1. DETECT RINGS (Look for nested contours using Hierarchy)
    # A ring has an outer boundary with a child contour (the hole) inside it
    # hierarchy[i][2] points to the first child index. If it's not -1, this contour has a hole.
    if hierarchy != [] and hierarchy[i][2] != -1:
        child_idx = hierarchy[i][2]
        child_area = cv2.contourArea(contours[child_idx])
        
        # Verify the hole is reasonably sized, and the outer shape is roundish
        if child_area > 100 and circularity > 0.7:
            cv2.drawContours(output, [cnt], -1, (255, 0, 0), 3) # Blue for Ring
            cv2.putText(output, "Ring", (approx[0][0][0], approx[0][0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
            continue # Skip to next shape so we don't double-classify

    # 2. DETECT CUBES / SQUARE FACES (4 Vertices)
    if num_vertices == 4:
        # Check aspect ratio of its bounding box to ensure it looks square/rectangular
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        
        # Cube faces from most angles have an aspect ratio between 0.6 and 1.4
        if 0.6 <= aspect_ratio <= 1.4:
            cv2.drawContours(output, [cnt], -1, (0, 0, 255), 3) # Red for Cube
            cv2.putText(output, "Cube Face", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # 3. DETECT CONES (Side view: 3 Vertices / Triangle)
    elif num_vertices == 3:
        cv2.drawContours(output, [cnt], -1, (0, 255, 0), 3) # Green for Cone
        cv2.putText(output, "Cone (Side)", (approx[0][0][0], approx[0][0][1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # 4. DETECT CONES (Top-down view: High circularity, no inner holes)
    elif circularity > 0.85:
        cv2.drawContours(output, [cnt], -1, (0, 255, 255), 3) # Yellow for Cone Top
        cv2.putText(output, "Cone (Top)", (approx[0][0][0], approx[0][0][1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

# Show results
cv2.imshow("Original Mask", mask)
cv2.imshow("Detected Shapes", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
