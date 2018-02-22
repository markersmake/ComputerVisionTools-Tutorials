import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('farmCircles.jpg')
Z = img.reshape((-1,3))

Z = np.float32(Z)

#define cluster and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 10
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

#convert back into uint8
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
