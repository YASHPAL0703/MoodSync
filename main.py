import numpy as np
import cv2 as cv
 
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Capture frame-by-frame
ret, frame = cap.read()
# if frame is read correctly ret is True
if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    
# Our operations on the frame come here

# Display the resulting frame
cv.imshow('frame', frame)
 
# When everything done, release the capture
cap.release()
if cv.waitKey(0)==ord('q'):
    cv.destroyAllWindows()
