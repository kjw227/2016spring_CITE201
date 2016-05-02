
import cv2
import time
import random

cap  = cv2.VideoCapture(0)

if not cap.isOpened():
	cap.open(0)

num = random.randint(1,3)

while(True) :
	ret, frame = cap.read()
	
	font = cv2.FONT_HERSHEY_SIMPLEX
	
	for i in range(1,num+1) :
		sr= "Object "+str(i)+" Distance: "+str(random.randint(10,100))+" cm"
		
		cv2.putText(frame,str(sr),(115,445+(1-i)*45),font,1,(255,255,255),2)
		cv2.imshow('image',frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
