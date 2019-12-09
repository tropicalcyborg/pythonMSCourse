import cv2
import imutils
import numpy as np 
import argparse
from colorama import init, Fore 
init()

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", help = "Path to an image", required = True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(image, (5,5), 0)
gray = cv2.Canny(gray, 50,250)

thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)[1]

cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = imutils.grab_contours(cnts)
print(type(cnts))

# ensure at least one contour was found
if len(cnts) > 0:
	# grab the largest contour, then draw a mask for the pill
	c = max(cnts, key=cv2.contourArea)
	mask = np.zeros(gray.shape, dtype="uint8")
	cv2.drawContours(mask, [c], -1, 255, -1)
 
	# compute its bounding box of pill, then extract the ROI,
	# and apply the mask
	(x, y, w, h) = cv2.boundingRect(c)
	imageROI = image[y:y + h, x:x + w]
	maskROI = mask[y:y + h, x:x + w]
	imageROI = cv2.bitwise_and(imageROI, imageROI,
		mask=maskROI)



print(Fore.YELLOW, len(cnts))

print()
print(Fore.GREEN, "Contour found")

cv2.imshow("Thresh", thresh)
cv2.imshow("Img", imageROI)
cv2.imshow("ROI", mask)


print()
print(Fore. RED, "Image loaded")
Fore.WHITE
print()
cv2.waitKey(0)