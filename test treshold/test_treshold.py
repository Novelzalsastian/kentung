import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('lenna.png', cv.IMREAD_GRAYSCALE)


#img = cv.imread('lenna.png' , 0 )
ret,thresh1 = cv.threshold(img, 127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img, 127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img, 127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img, 127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img, 127,255,cv.THRESH_TOZERO_INV)

#imwrite nya
cv.imshow('1',thresh1)
cv.imshow('2',thresh2)
cv.imshow('3',thresh3)
cv.imshow('4',thresh4)
cv.imshow('5',thresh5)

cv.waitKey(0)
cv.DestroyAllWindow()