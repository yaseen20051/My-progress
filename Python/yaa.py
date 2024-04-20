import cv2

img=cv2.imread("C:\\Users\\yi340\\OneDrive\\Desktop\\R.png",-1)
img_2=cv2.imread("C:\\Users\\yi340\\OneDrive\\Desktop\\R.png",0)
cv2.imshow("img",img)
cv2.imshow("img_2",img_2)
cv2.waitKry(0)

