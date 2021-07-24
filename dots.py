import cv2
import matplotlib.pyplot as plt

def plotImg(img):
    if len(img.shape) == 2:
        plt.imshow(img, cmap='gray')
        plt.show()
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()

t=0
img = cv2.imread('cv.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
binary_img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 131, 15)
plotImg(binary_img)
_, _, boxes, _ = cv2.connectedComponentsWithStats(binary_img)
# first box is the background
boxes = boxes[1:]
filtered_boxes = []
for x,y,w,h,pixels in boxes:
    if  h < 100 and w < 100 and h > 10 and w > 10:
        filtered_boxes.append((x,y,w,h))
        t=t+1

for x,y,w,h in filtered_boxes:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2)
print(t)
plotImg(img)