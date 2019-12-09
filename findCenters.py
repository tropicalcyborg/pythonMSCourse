#Coding = UTF8

import cv2
import numpy as np
import argparse
import imutils
from colorama import init, Fore 

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", help = "Path to the source image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# cv2.imshow("Imagem",image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5,5), 5)
blurred = cv2.blur(gray, (20,20))

thresh = cv2.threshold(blurred, 210,255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Gray", blurred)
# cv2.imshow("Original", image)

cv2.waitKey(0)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

print(len(cnts))

# loop over the contours
for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
 
	# draw the contour and center of the shape on the image
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.circle(image, (cX, cY), 7, (0, 255, 255), -1)
	cv2.putText(image, "center", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
 
	# show the image
	cv2.imshow("Image", image)
	cv2.waitKey(0)


