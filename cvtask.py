import cv2
import numpy as np 

img2 = cv2.imread("task2.png")
img1 = cv2.GaussianBlur(img2,(31,31),0)
img = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold (img,127,255,cv2.THRESH_BINARY_INV)

ret, thresh1 = cv2.threshold (img,0,255,cv2.THRESH_BINARY_INV)

cv2.namedWindow('Original',cv2.WINDOW_NORMAL)
cv2.imshow('Original',img2)


#cv2.namedWindow('Blurred',cv2.WINDOW_NORMAL)
#cv2.imshow('Blurred',img1)


cv2.namedWindow('Threshold',cv2.WINDOW_NORMAL)
cv2.imshow('Threshold',thresh)

############################

_,contours,_ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img2,contours,1,(0,255,0),2)


cv2.drawContours(thresh1,contours,-1,(255,255,255),2)

print(len(contours)) 

###########################

cv2.namedWindow('Final',cv2.WINDOW_NORMAL)
cv2.imshow('Final',img2)


cv2.namedWindow('Final1',cv2.WINDOW_NORMAL)
cv2.imshow('Final1',thresh1)

cv2.waitKey(0)

