#   VRMulticopter

Multicopter combined with VR

This project has three parts: Android Server, Raspberry Pi, Pixhawk and Gimbal Controller.

Android server is to send user's head motion and recieve video stream from Raspberry Pi through WIFI.

Raspberry pi get two streams of video from a stereo camera and send data to gimbal controller.

Pixhawk controls the drone's flight and send drone's information to Raspberry Pi.

Gimbal controller decodes messages from Raspberry pi to make sure that the stereo camera on the gimbal keep the same attitude with user's head