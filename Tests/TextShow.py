import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
	cap.open(0)

while(True) : 
	ret, frame = cap.read()
	font = cv2.FONT_HERSHEY_SIMPLEX

	cv2.putText(frame,"hello",(300,450),font,1,(255,255,255),2)

	cv2.imshow('image',frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllwindow()

