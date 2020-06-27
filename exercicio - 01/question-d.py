import cv2 as cv
import numpy as np

print(' Digite a quantidade de linhas e colunas da imagem ')
linhas = int(input('linhas: '))
colunas = int(input('colunas: '))

if linhas == 0 or colunas == 0:
    print('as linhas e colunas não podem ser iguais a zero')

image = np.ones((linhas, colunas), dtype=np.uint8)

print(image)

divider = 255 / linhas

for a in range(0, linhas):
    image[a] = a * divider

cv.imshow('image', image)
cv.waitKey(0)
