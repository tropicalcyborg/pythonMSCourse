import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required = True,
    help="Path to the input image")

args = vars(ap.parse_args())

imagem = cv2.imread(args["image"])
(h,w,d) = imagem.shape

print ("width = {}, heigh = {}, depth = {}".format(h,w,d))

# cv2.imshow("Imagem", imagem)
# cv2.waitKey(0)

imagemCopia = imagem.copy()
gray = cv2.cvtColor(imagemCopia, cv2.COLOR_BGR2GRAY)

# edges = cv2.Canny(gray, 30,150)
# cv2.rectangle(imagemCopia, (107,487), (279,750), (124,165,255), 2)
# cv2.circle(imagemCopia, (107,487), 8, (255,255,0), 2)
# blurred = cv2.GaussianBlur(imagem,(15,15),0)
thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)[1]
mask = thresh.copy()

mask = cv2.erode(mask, None, iterations=5)
# cv2.imshow("Eroded", mask)

# find contours (i.e., outlines) of the foreground objects in the
# thresholded image
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

output = imagem.copy()

# # loop over the contours
for c in cnts:
	# draw each contour on the output image with a 3px thick purple
	# outline, then display the output contours one at a time
	cv2.drawContours(output, [c], -1, (120, 0, 159), 2)
	


text = "I found {} objects!".format(len(cnts))



# cv2.imshow("Contours", output)
print("pode conferir")

output = cv2.bitwise_and(imagem,imagem, mask=mask)
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(255, 255, 255), 1)
cv2.imshow("Output", output)
cv2.waitKey(0)


# cv2.imshow("Thresh", thresh)
# # cv2.imshow("Edges", edges)

# cv2.waitKey(0)



# resized = imutils.resize(image, width = 200)
# cv2.imshow("Cachorrinho", resized)
# cv2.waitKey(0)

# rotated = imutils.rotate_bound(resized, 45)
# cv2.imshow("Rotacionada", rotated)
# cv2.waitKey(0)





