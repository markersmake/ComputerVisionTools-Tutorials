import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cornField.jpg',0)
edges = cv2.Canny(img, 100, 200)

cv2.imshow('cornField.jpg', img)
cv2.waitKey(0)
cv2.imshow('cornField.jpg', edges)
