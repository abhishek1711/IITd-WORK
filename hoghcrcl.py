import cv2
import numpy as np
import argparse

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True,
#     help = "Path to the image")
# args = vars(ap.parse_args())
# image = cv2.imread(args["image"])

img = cv2.imread('2018-05-31-113050.jpg',0)

# img = cv2.resize(img,(1440,748))
img = cv2.medianBlur(img,5)

cv2.imshow('hhdf',img)
cv2.waitKey(0)
# blurred = cv2.GaussianBlur(img, (11, 11), 0)
# (T, thresh) = cv2.threshold(img, 35, 255, cv2.THRESH_BINARY)
# cv2.imshow("Threshold Binary", thresh)
# cv2.waitKey(0)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

edimage = cv2.Canny(img, 60,50)
cv2.imshow('ed',edimage)
cv2.waitKey(0)
# bfilterimg = cv2.bilateralFilter(img,5,175,175)
# cv2.imshow('bilateral',bfilterimg)
# cv2.waitKey(0)
circles = cv2.HoughCircles(edimage,cv2.HOUGH_GRADIENT,1,40,param1=10,param2=16,minRadius=5,maxRadius=50)#for webcam image

#circles = cv2.HoughCircles(edimage,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=20,maxRadius=50)#for whatsapp image
# circles = imfindcircles(A,[20,50])
print circles.shape[1]
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

rad = 4
min =circles[0,0,2] / rad

for i in circles[0,:]:
    print i[2]/min



cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
