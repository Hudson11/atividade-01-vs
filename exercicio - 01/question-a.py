import cv2 as cv

image = cv.imread('image.jpg')

B, G, R = cv.split(image)

cv.imshow('RED', R)
cv.imshow('GREEN', G)
cv.imshow('BLUE', B)
cv.waitKey(0)
