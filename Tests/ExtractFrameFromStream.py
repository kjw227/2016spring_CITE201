import cv2
import time

captureUnit = cv2.VideoCapture(0)

if not captureUnit.isOpened():
	captureUnit.Open(0)

count = 1
while(True):
	play, frame1 = captureUnit.read();
	time.sleep(0.05);
	play, frame2 = captureUnit.read();

	params = list()
	params.append(cv2.IMWRITE_JPEG_QUALITY)
	params.append(70)
	fname1 = "SavedFrames/first" + str(count) + ".jpg"
	fname2 = "SavedFrames/second" + str(count) + ".jpg"
	cv2.imwrite(fname1, frame1, params)
	cv2.imwrite(fname2, frame2, params)

	time.sleep(1);
	count += 1;
	if count == 10:
		break

captureUnit.release()