import cv2

camera = cv2.VideoCapture(0)

ret, frame = camera.read()
if ret:
    cv2.imwrite("captured_img.jpg", frame) # Numpy配列として保存

camera.release()