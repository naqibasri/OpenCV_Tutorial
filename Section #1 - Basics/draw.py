import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")
cv.imshow("blank", blank)

#1. Paint the blank with certain colour at certain pixels
blank[100:200] = (0,255,0)
blank[200:300, 100:200] = (0,0,255)
cv.imshow("coloured", blank)

#2. Draw a rectangle
cv.rectangle(blank,(0,0), (100,100), color=(255,0,0), thickness=2)
cv.rectangle(blank,(0,0), (blank.shape[0]//2,blank.shape[1]//2), color=(0,0,255), thickness=2)
cv.imshow("rectangle", blank)

#3. Draw a circle
cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 100, color=(255,255,0), thickness= 2, lineType=2)
cv.imshow("circle", blank)

#4. Draw a line
cv.line(blank, (250,250), (500,500), color=(255,255,255), thickness=2)
cv.imshow("line", blank)

#5. Put Text
cv.putText(blank, "Hello World", (0,500), fontFace= cv.FONT_HERSHEY_TRIPLEX, fontScale= 1, color= (0,255,255), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)