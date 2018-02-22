import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('mathHomework.jpg',0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

cv2.imshow('laplacian', laplacian)
cv2.waitKey(0)
cv2.imshow('sobelx', sobelx)

cv2.imshow('sobely', sobely)
