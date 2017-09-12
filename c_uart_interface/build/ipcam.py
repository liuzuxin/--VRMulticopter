#!/usr/bin/python
'''
	Author: Igor Maculan - n3wtron@gmail.com
	A Simple mjpg stream http server
'''
import cv2
import Image
import threading
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
import StringIO
import time
import numpy

fps = 30
cam_num = 1
video = None
videoWriter = None
IP_adrress = '192.168.1.104'


class CamHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global videoWriter
        global video
        global IP_adrress
        global cam_num
        global fps
        if self.path.endswith('.mjpg'):
            self.send_response(200)
            self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=--jpgboundary')
            self.end_headers()
            while True:
                try:
                    success, src = video.read()
                    # print(success)
                    if success == False:
                        print 'open false'
                        try :
                            break
                            '''
                            video.release()
                            cv2.waitKey(500)
                            video = cv2.VideoCapture(cam_num)  # 0 stands for camera #0
                            video.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
                            video.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
                            video.set(cv2.CAP_PROP_FPS, fps)
                            success, src = video.read()'''
                        except KeyboardInterrupt:
                            break;
                            return

                    a = numpy.loadtxt("1.txt", dtype='str')
                    if a.shape[0] == 5:
                        pos_x = a[0]
                        pos_y = a[1]
                        pos_z = a[2]
                        yaw__ = a[3]
                        altit = a[4]
                        font = cv2.FONT_HERSHEY_DUPLEX
                        huangse = (85, 142, 235)
                        jinghuang = (0, 215, 255)
                        chengse = (0, 97, 255)
                        bilv = (212, 255, 127)
                        cuilv = (87, 201, 0)
                        zise = (240, 32, 160)
                        xx=170
                        cv2.putText(src, 'pos_x : '+pos_x, (xx, 160), font, 1, huangse, 2)
                        cv2.putText(src, 'pos_y : '+pos_y, (xx, 210), font, 1, jinghuang, 2)
                        cv2.putText(src, 'pos_z : '+pos_z, (xx, 260), font, 1, chengse, 2)
                        cv2.putText(src, 'yaw__ : '+yaw__, (xx, 310), font, 1, bilv, 2)
                        cv2.putText(src, 'height: '+altit, (xx, 360), font, 1, cuilv, 2)
                    black = [0, 0, 0]
                    left = src[0:src.shape[0], 0:src.shape[1] / 2].copy()
                    left = cv2.copyMakeBorder(left, 100, 200, 200, 100, cv2.BORDER_CONSTANT, value=black)
                    left = cv2.copyMakeBorder(left, 0, 0, 0, left.shape[1], cv2.BORDER_CONSTANT, value=black)
                    src=left
                    src[0:src.shape[0], src.shape[1] / 2:src.shape[1]] = src[0:src.shape[0], 0:src.shape[1] / 2]
                    ''' save the video '''
                    videoWriter.write(src)
                    img = src
                    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    jpg = Image.fromarray(imgRGB)
                    tmpFile = StringIO.StringIO()
                    jpg.save(tmpFile, 'JPEG')
                    self.wfile.write("--jpgboundary")
                    self.send_header('Content-type', 'image/jpeg')
                    self.send_header('Content-length', str(tmpFile.len))
                    self.end_headers()
                    jpg.save(self.wfile, 'JPEG')
                    time.sleep(0.8 / fps)
                except KeyboardInterrupt:
                    break

            return


        if self.path.endswith('.html'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write('<html><head></head><body>')
            self.wfile.write('<img src="http://' + IP_adrress + ':5000/cam.mjpg"/>')

            self.wfile.write('</body></html>')
            return
'''
    def get_frame(self):
        success, src = video.read()

        # print(success)
        while success == False:
            print 'false'
            video.release()
            cv2.waitKey(500)
            video = cv2.VideoCapture(cam_num)  # 0 stands for camera #0
            video.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
            video.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
            success, src = video.read()

        src[0:src.shape[0], 0:src.shape[1] / 2] = src[0:src.shape[0], src.shape[1] / 2:src.shape[1]]

        videoWriter.write(src)
        return src
'''


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


def init():
    global video
    global videoWriter
    global cam_num
    global fps
    video = cv2.VideoCapture(cam_num)  # 0 stands for camera #0
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
    video.set(cv2.CAP_PROP_FPS, fps)
    success, src = video.read()
    while not success:
        print 'initial open false'
        video.release()
        cv2.waitKey(1200)
        video = cv2.VideoCapture(cam_num)  # 0 stands for camera #0
        video.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
        video.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)
        success, src = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)
    size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    videoWriter = cv2.VideoWriter('stereo_camera_use_one_img.avi', cv2.VideoWriter_fourcc('M', 'P', '4', '2'),
                                  fps, size)


def main():
    global video
    global cam_num
    global videoWriter
    global IP_adrress
    # video.set(cv2.cv.CV_CAP_PROP_SATURATION,0.2);
    init()
    try:
        server = ThreadedHTTPServer((IP_adrress, 5000), CamHandler)
        print "server started"
        print 'http://' + IP_adrress + ':5000/cam.mjpg'
        server.serve_forever()
    except KeyboardInterrupt:
        video.release()
        videoWriter.release()
        server.socket.close()


if __name__ == '__main__':
    main()
