import cv2
import time

cUnit = cv2.VideoCapture(0)

if not cUnit.isOpened():
	cUnit.Open(0)

while(True):
	play, capframe = cUnit.read()

	surf_detector = cv2.xfeatures2d.SURF_create()
	surf_kp, surf_des = surf_detector.detectAndCompute(capframe, None)

	print(len(surf_kp))
	printimg = cv2.drawKeypoints(capframe, surf_kp, None, (255, 0, 0), 4)

	cv2.imshow('SURF_detection', printimg)
	if cv2.waitKey(1000) & 0xFF == ord('q'):
		break

cUnit.release()
cv2.destroyAllWindows()