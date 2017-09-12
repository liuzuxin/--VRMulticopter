import cv2
import numpy as np

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(1) # 0 stands for camera #0
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
        self.merge = np.zeros((480, 1280, 3), np.uint8)
      # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, src = self.video.read()
	
	#print(success)
	while success==False:
	    print 'false'
	    self.video.release()
	    cv2.waitKey(200)
	    self.video = cv2.VideoCapture(1) # 0 stands for camera #0
            self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
            self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
	    success, src = self.video.read()
	
	src[0:src.shape[0], 0:src.shape[1]/2]=src[0:src.shape[0], src.shape[1]/2:src.shape[1]]
	
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg',src)
        return jpeg.tostring()
