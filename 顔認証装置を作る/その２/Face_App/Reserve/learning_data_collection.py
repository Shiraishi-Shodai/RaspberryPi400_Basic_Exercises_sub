import glob
import cv2

class Reserve:
    
    def __init__(self) -> None:
        pass
    
    def collection(self, path):
        imgs = glob.glob(path + "*.jpg")

r = Reserve()
r.collection("/home/pi/python/RaspberryPi400_Basic_Exercises/顔認証装置を作る/その２/img/")