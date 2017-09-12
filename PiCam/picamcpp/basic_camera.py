import numpy as np
import cv2

window_name = "Video #0"

cap = cv2.VideoCapture(0)
cv2.namedWindow(window_name, cv2.CV_WINDOW_AUTOSIZE)

while(True):
    # Capture frame-by-frame
    success, frame = cap.read()
    if not success:
    	print "Error capturing frame"
    	break

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow(window_name, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()