import cv2
import numpy as np

image = cv2.imread('polka_dots_2.jpg')
grey_scale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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

params_2 = cv2.SimpleBlobDetector_Params()
params_2.filterByArea = True
params_2.minArea = 50
params_2.maxArea = 10000
params_2.filterByCircularity = True
params_2.minCircularity = 0.1

detector = cv2.SimpleBlobDetector_create(params_2)
keypoints = detector.detect(image)
output_image = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv2.imshow('Blob Detection', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()