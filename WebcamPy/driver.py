import cv2
import time


#Declaring global variables
height = 600
width = 600

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

#Variables for FPS calculation
now = time.time()
prev = time.time()

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    #Calculating FPS
    now = time.time()
    fps = 1/(now-prev)
    prev = now

    #Adding FPS on corner
    cv2.putText(frame, str(int(fps)), (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 5, (100, 255, 0), 3, cv2.LINE_AA)

    #Showing frame
    cv2.imshow('Input', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()