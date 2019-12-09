from transform import four_point_transform
import cv2
import numpy as np 
import argparse
from colorama import init, Fore

init()



ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Path to the image File")
ap.add_argument("-c", "--coords", help = "Comma separated list of points")
args = vars(ap.parse_args())

imagem = cv2.imread(args["image"])
pts = np.array(eval(args["coords"]))
warped = four_point_transform(imagem, pts)
coords = args["coords"]


print()
print(Fore.RED, args["coords"])
print()

# cv2.imshow("Original", imagem)
cv2.imshow("Warped", warped)
print(Fore.GREEN, "Imagem distorcida pronta")
print()
Fore.WHITE
cv2.waitKey(0)
