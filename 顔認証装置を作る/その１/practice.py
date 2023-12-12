""" 写真に写る顔を検知し、顔を赤枠で囲う """

import face_recognition
from PIL import Image, ImageDraw

load_image = face_recognition.load_image_file('/home/pi/python/RaspberryPi400_Basic_Exercises/顔認証装置を作る/その１/monalisa.jpg')
print(load_image.shape) #RGBのnumpy配列

# 認識させたい画像から顔検出する
face_locations = face_recognition.face_locations(load_image)

pil_image = Image.fromarray(load_image)
# print(pil_image)
# print(type(pil_image))

draw = ImageDraw.Draw(pil_image)

for (top, right, bottom, left) in face_locations:
    draw.rectangle(((left, top), (right, bottom)),
                   outline=(255, 0, 0), width=2)

del draw

pil_image.show()