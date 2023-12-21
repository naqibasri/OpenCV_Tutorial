import cv2 as cv

img = cv.imread("../Resources/Photos/cats.jpg")
cv.imshow("BGR",img)

#1. BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", gray)

#2. BGR to HSV(also known as hue saturation value)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

#3. BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

#4. BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)


cv.waitKey(0)