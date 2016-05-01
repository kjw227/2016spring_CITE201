import sys
import numpy as np
import cv2

img = cv2.imread("image/target.jpg")
# may resize the image if we need to
# h, w = img,shape()

grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayimg = cv2.bilateralFilter(grayimg, 11, 17, 17)
edge = cv2.Canny(grayimg, 30, 200)

cv2.imshow('Edged_image', edge)
if cv2.waitKey(0):
	cv2.destroyAllWindows()

_, conts, _ = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
conts = sorted(conts, key = cv2.contourArea, reverse = True)[:10]

for c in conts:
	appshape = cv2.arcLength(c, True)
	corners = cv2.approxPolyDP(c, 0.10 * appshape, True)
	if len(corners) == 4:
		target = corners
		break

copyimg = img.copy()
cv2.drawContours(copyimg, target, -1, (255, 0, 0), 3)
cv2.imshow('Found_contour', copyimg)

if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.destroyAllWindows
	sys.exit(0)

points = target.reshape(4, 2)
rect = np.zeros((4, 2), dtype = "float32")

rect[0] = points[np.argmin(points.sum(axis = 1))]
rect[2] = points[np.argmax(points.sum(axis = 1))]

rect[1] = points[np.argmin(np.diff(points, axis = 1))]
rect[3] = points[np.argmax(np.diff(points, axis = 1))]

(tl, tr, br, bl) = rect

widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))

width = max(widthA, widthB)
height = max(heightA, heightB)
width = int(width)
height = int(height)

final = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]], dtype = "float32")
trans = cv2.getPerspectiveTransform(rect, final)
warped = cv2.warpPerspective(img, trans, (width, height))

cv2.imshow('Original', img)
cv2.waitKey(1)
cv2.imshow('Warped', warped)
cv2.waitKey(0)
cv2.destroyAllWindows()