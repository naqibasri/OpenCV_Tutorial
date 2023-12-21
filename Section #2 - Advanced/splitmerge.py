import cv2 as cv

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('BGR', img)

#1. Split to B, G and R
B,G,R = cv.split(img)

cv.imshow("B", B)
cv.imshow("G", G)
cv.imshow("R", R)

#2. Merge back into BGR
merged = cv.merge([B,G,R])
cv.imshow('merged', merged)

print(img.shape)
print(B.shape)
print(G.shape)
print(R.shape)
print(merged.shape)

cv.waitKey(0)
