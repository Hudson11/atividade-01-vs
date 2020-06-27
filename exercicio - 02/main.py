import cv2 as cv
import numpy as np

list = []

for a in range(1, 10):
    list.append(cv.imread('a'+str(a)+'.jpg'))

image = np.zeros((1057,1280,3))

for a in range(0, len(list)):
    image = image + list[a]

image = image / len(list)

print(image)

cv.imshow('image', np.array(image, dtype=np.uint8))
cv.waitKey(0)



