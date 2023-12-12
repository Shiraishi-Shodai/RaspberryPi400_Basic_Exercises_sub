"""プログラムを起動するとRaspberryPi400に、カメラ映像を静止画として保存する"""

import cv2

camera = cv2.VideoCapture(0)

ret, frame = camera.read()
if ret:
    cv2.imwrite("/home/pi/python/RaspberryPi400_Basic_Exercises/監視カメラを作る/その2/Exercise1/captured_img.jpg", frame) # Numpy配列として保存

camera.release()
