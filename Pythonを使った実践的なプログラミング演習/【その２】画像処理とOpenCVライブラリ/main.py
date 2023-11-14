import cv2

img = cv2.imread("/home/pi/python/RaspberryPi400_Basic_Exercises/publiic/img/input.jpg")
im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("/home/pi/python/RaspberryPi400_Basic_Exercises/publiic/img/output.jpg", im_gray)
