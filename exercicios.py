import numpy as np
import cv2
import argparse
from colorama import init, Fore
init()
import imutils


ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
    help="name of the user")

args = vars(ap.parse_args())

print()
print(Fore.RED, "Hi, there {}, its nice to meet you!...".format(args["name"]))
print()
# print(args)
# print()
Fore.WHITE
print()

image = cv2.imread("TestImages/dog.jpg")
(h, w, d) = image.shape
# print("width={}, height={}, depth={}".format(w, h, d))

# (B, G, R) = image[100, 50]
# print("R={}, G={}, B={}".format(R, G, B))

cv2.imshow("Cachorro", image)
# cv2.waitKey()

# cao = image[498:758, 97:270]
# cv2.imshow("cão", cao)
# cv2.waitKey(0)

# roi = image[0:101, 60:165]
# cv2.imshow("vassoura", roi)
# cv2.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
# resized = cv2.resize(image, (200, 200))
# cv2.imshow("Fixed Resizing", resized)
# cv2.waitKey(0)


# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
# r = 300.0 / w
# dim = (300, int(h * r))
# resized = cv2.resize(image, dim)
# cv2.imshow("Aspect Ratio Resize", resized)
# cv2.waitKey(0)

# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
# resized = imutils.resize(image, width=200)
# cv2.imshow("Imutils Resize", resized)
# cv2.waitKey(0)


# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
#center = (w // 2, h // 2)
center = (0,h)
M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (h,h+w))

# rotatedCroped = rotated[h:h+w, 0:h]
# cv2.imshow("OpenCV Rotation", rotatedCroped)
# cv2.waitKey(0)


# rotation can also be easily accomplished via imutils with less code
# rotated = imutils.rotate(image, -90)
# cv2.imshow("Imutils Rotation", rotated)
# cv2.waitKey(0)


# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help
# us out
# rotated = imutils.rotate_bound(image, 45)
# cv2.imshow("Imutils Bound Rotation", rotated)
# cv2.waitKey(0)


# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
# blurred = cv2.GaussianBlur(rotated, (11, 11), 0)
# cv2.imshow("Blurred", blurred)
# cv2.waitKey(0)


# draw a 2px thick red rectangle surrounding the face
output = image.copy()
cv2.rectangle(output, (97,498), (270, 758,), (0, 0, 255), 2)
# cv2.imshow("Rectangle", output)
# cv2.waitKey(0)

# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
# output = image.copy()
# cv2.circle(output, (178,567), 20, (0, 0, 255), -1)
# cv2.imshow("Circle", output)
# cv2.waitKey(0)


# # draw a 5px thick red line from x=60,y=20 to x=400,y=200
# output = image.copy()
# cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
# cv2.imshow("Line", output)
# cv2.waitKey(0)


# draw green text on the image
# output = image.copy()
cv2.putText(output, "Encontrado", (104, 525), 
cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)