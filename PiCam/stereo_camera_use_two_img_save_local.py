import cv2
import numpy as np
import threading
import gevent.queue

def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return image

class MyThread(threading.Thread):
    def __init__(self, q):
        super(MyThread, self).__init__()
        self.q = q

    def run(self):
        input_data = 's'
        while input_data != 'q':
            input_data = raw_input('>>>')
            self.q.put(input_data)

class VideoCamera(object):
    def __init__(self):
        self.cam_num=1
        self.video = cv2.VideoCapture(self.cam_num)  # 0 stands for camera #0
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
        self.img_v = 23
        #	self.img_h=57
        self.img_h = -12
        success, src = self.video.read()
        self.q = gevent.queue.Queue()
        print '----input thread start----'
        threads = MyThread(self.q)
        threads.start()
        # print(success)
        while success == False:
            print 'false'
            self.video.release()
            cv2.waitKey(1200)
            self.video = cv2.VideoCapture(self.cam_num)  # 0 stands for camera #0
            self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
            self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
            success, src = self.video.read()

        self.fps = self.video.get(cv2.CAP_PROP_FPS)
        size = (int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        self.videoWriter = cv2.VideoWriter('stereo_camera_use_two_img.avi', cv2.VideoWriter_fourcc('M', 'P', '4', '2'), self.fps,
                                               size)


    def __del__(self):
        self.video.release()
        self.videoWriter.release()
    def get_frame(self):
        success, src = self.video.read()

        if not self.q.empty():
            command = self.q.get()
            if command == 'a':
                self.img_h += 3
                print 'now the horizon bias is ', self.img_h
            elif command == 'd':
                self.img_h -= 3
                print 'now the horizon bias is ', self.img_h
            # print(success)
        while success == False:
            print 'false'
            self.video.release()
            cv2.waitKey(500)
            self.video = cv2.VideoCapture(self.cam_num)  # 0 stands for camera #0
            self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
            self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
            success, src = self.video.read()
        src[0:src.shape[0], 0:src.shape[1] / 2] = translate(src[0:src.shape[0], 0:src.shape[1] / 2], 0, -self.img_v)

        src[0:src.shape[0], src.shape[1] / 2:src.shape[1]] = translate(
            src[0:src.shape[0], src.shape[1] / 2:src.shape[1]], 0, self.img_v)

        left = src[0:src.shape[0], 0:src.shape[1] / 2].copy()
        src[0:src.shape[0], 0:src.shape[1] / 2] = src[0:src.shape[0], src.shape[1] / 2:src.shape[1]]
        src[0:src.shape[0], src.shape[1] / 2:src.shape[1]] = left

        src[0:src.shape[0], 0:src.shape[1] / 2] = translate(src[0:src.shape[0], 0:src.shape[1] / 2], -self.img_h, 0)

        src[0:src.shape[0], src.shape[1] / 2:src.shape[1]] = translate(
            src[0:src.shape[0], src.shape[1] / 2:src.shape[1]], self.img_h, 0)
        ''' save the video '''
        self.videoWriter.write(src)
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', src)
        cv2.waitKey(800/int(self.fps))
        return jpeg.tostring()
