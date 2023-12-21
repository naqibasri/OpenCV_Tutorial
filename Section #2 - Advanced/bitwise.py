import cv2 as cv
import numpy as np

blank = np.zeros((500,500),dtype='uint8')
cv.imshow('blank', blank)

rectangle = cv.rectangle(blank.copy(), (30,30), (470,470), color=255 ,thickness=-1)
cv.imshow('rectangle', rectangle)

circle = cv.circle(blank.copy(), (250,250), 250, color=255, thickness=-1)
cv.imshow('circle', circle)

#Bitwise operation AND
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise_and', bitwise_and)

#Bitwise operation OR
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise_or', bitwise_or)

#Bitwise operation XOR
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise_xor', bitwise_xor)

#Bitwise operation NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('bitwise_not', bitwise_not)



cv.waitKey(0)
