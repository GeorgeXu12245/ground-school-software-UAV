import cv2
import numpy as np

image = cv2.imread('polka_dots_2.jpg')
grey_scale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grey_scale_image = cv2.GaussianBlur(grey_scale_image, (7, 7), 0)
'''
params_1 = cv2.SimpleBlobDetector_Params()
params_1.minDistBetweenBlobs = 7.0
params_1.minRepeatability = 2

params_1.minThreshold = 0
params_1.maxThreshold = 255
params_1.filterByArea = True
params_1.minArea = 20
params_1.maxArea = 10000
params_1.filterByCircularity = True
params_1.minCircularity = 0.2
params_1.filterByConvexity = True
params_1.minConvexity = 0.2
params_1.filterByInertia = True
params_1.minInertiaRatio = 0.4
params_1.filterByColor = True
params_1.blobColor = 0
'''

params_2_1 = cv2.SimpleBlobDetector_Params()
params_2_1.minThreshold = 0
params_2_1.maxThreshold = 255
params_2_1.thresholdStep = 1
#params_2.filterByArea = True
#params_2.minDistBetweenBlobs = 5
params_2_1.minRepeatability = 2
params_2_1.minArea = 60
params_2_1.maxArea = 10000
params_2_1.filterByColor = True
params_2_1.blobColor = 255
#params_2_1.filterByCircularity = True
#params_2_1.minCircularity = 0.5
#params_2_1.filterByConvexity = True
#params_2_1.minConvexity = 0.7
#params_2.filterByInertia = True
#params_2.minInertiaRatio = 0.3

params_2_2 = cv2.SimpleBlobDetector_Params()
params_2_2.minThreshold = 0
params_2_2.maxThreshold = 255
params_2_2.thresholdStep = 1
params_2_2.minRepeatability = 2
params_2_2.filterByColor = True
params_2_2.blobColor = 0
params_2_2.filterByArea = True
params_2_2.minArea = 60
params_2_2.maxArea = 10000


detector_1 = cv2.SimpleBlobDetector_create(params_2_1)
detector_2 = cv2.SimpleBlobDetector_create(params_2_2)
keypoints_1 = detector_1.detect(grey_scale_image)
keypoints_2 = detector_2.detect(grey_scale_image)
output_image = cv2.drawKeypoints(grey_scale_image, keypoints_1 + keypoints_2, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv2.imshow('Blob Detection', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()