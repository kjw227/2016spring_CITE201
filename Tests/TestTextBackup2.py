
import cv2
import time
import random

cap  = cv2.VideoCapture(0)

if not cap.isOpened():
	cap.open(0)

while(True) :
	ret, frame = cap.read()
	
	akaze_detector = cv2.AKAZE_create()
	akaze_kp, akaze_des = akaze_detector.detectAndCompute(frame,None)
	
	printimg = cv2.drawKeypoints(frame, akaze_kp, None, (255,0,0),4)
	dis = 0.0

	if(len(akaze_kp)>0):
		key = []
		d = akaze_kp[0].pt[1]
		for it in akaze_kp:
			if it.pt[1] > d :
				d = it.pt[1]
				key = [it]
		dis = 0.0006*d*d - 0.5969*d+239.83
	
		printimg = cv2.drawKeypoints(printimg, key, None, (0,255,0),4) 

	font = cv2.FONT_HERSHEY_SIMPLEX
	
	for i in range(1,2) :
		sr= "Object "+str(i)+" Distance: "+"{:.0f}".format(dis)+" cm"
		
		cv2.putText(printimg,str(sr),(100,445+(1-i)*45),font,1,(255,255,255),2)
		cv2.imshow('image',printimg)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
