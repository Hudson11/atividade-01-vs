import cv2 as cv

image1 = cv.imread('image1.png')
image2 = cv.imread('image2.png')

image3 = cv.add(image1, image2)

cv.imshow('image1', image1)
cv.imshow('image2', image2)
cv.imshow('image3', image3)
cv.waitKey(0)
