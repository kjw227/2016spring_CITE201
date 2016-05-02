import cv2
import time

cUnit = cv2.VideoCapture(0)

if not cUnit.isOpened():
	cUnit.Open(0)

while(True):
	play, capframe = cUnit.read()

	akaze_detector = cv2.AKAZE_create()
	akaze_kp, akaze_des = akaze_detector.detectAndCompute(capframe, None)

	print(len(akaze_kp))
	printimg = cv2.drawKeypoints(capframe, akaze_kp, None, (255, 0, 0), 4)

	cv2.imshow('AKAZE_detection', printimg)
	if cv2.waitKey(1000) & 0xFF == ord('q'):
		break

cUnit.release()
cv2.destroyAllWindows()

