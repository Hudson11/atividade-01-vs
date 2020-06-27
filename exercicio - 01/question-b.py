import cv2 as cv
import numpy as np

image = cv.imread('image.jpg')

inverse = np.flip(image, 0)
print(inverse)

cv.imshow('inverse', inverse)
cv.waitKey(0)