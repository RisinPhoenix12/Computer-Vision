import cv2

img2 = cv2.imread("task2.png")

img1 = cv2.GaussianBlur(img2,(31,31),0)
img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold (img,127,255,cv2.THRESH_BINARY_INV)


ret, thresh1 = cv2.threshold (img,0,255,cv2.THRESH_BINARY)   #Blank GRAY image
threshchanged = cv2.cvtColor(thresh1,cv2.COLOR_GRAY2BGR)     #coloured Blank image

_,contours,_ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    #radius = int(radius)
    cv2.circle(threshchanged,center,1,(23,102,61),2)
    
cv2.drawContours(threshchanged,contours,-1,(80,226,151),2)
print(len(contours)) 


cv2.namedWindow('Original',cv2.WINDOW_NORMAL)
cv2.imshow('Original',img2)

cv2.namedWindow('Final1',cv2.WINDOW_NORMAL)
cv2.imshow('Final1',threshchanged)


cv2.waitKey(0)
