import cv2

captureUnit = cv2.VideoCapture(0)

if not captureUnit.isOpened():
	captureUnit.open(0)

while(True):
	play, frame = captureUnit.read()

	cv2.imshow('cute_songyw', frame)
	if cv2.waitKey(1) & 0xFF == ord('q') && play :
		break

captureUnit.release()
cv2.destroyAllWindows()