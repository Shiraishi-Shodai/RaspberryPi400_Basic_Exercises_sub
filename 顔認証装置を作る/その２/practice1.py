"""画像から顔を切り取り表示する"""

import face_recognition
import cv2

cap = cv2.VideoCapture(0)


# 既知の顔の画像を読み込み、エンコードする
known_image = face_recognition.load_image_file("/home/pi/python/RaspberryPi400_Basic_Exercises/顔認証装置を作る/その２/img/001.jpg")
print(known_image.shape)

 # 顔の位置情報を取得(top, right, bottom, left)
know_location = face_recognition.face_locations(known_image)

for top, right, bottom, left in know_location:
    # 顔の部分を切り取る
    img = known_image[top:bottom, left:right]
    print(img)
    # OpenCVはBGR形式を使用するため、色の順序をRGBからBGRに変換する
    img_2 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imshow("camera", img_2)

# キーボード入力を待つ（例えば、'q'キーで終了）
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
