import face_recognition
import cv2

cap = cv2.VideoCapture(0)


# 既知の顔の画像を読み込み、エンコードする
known_image = face_recognition.load_image_file("/home/pi/python/RaspberryPi400_Basic_Exercises/顔認証装置を作る/その２/img/001.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]
know_location = face_recognition.face_locations(known_image)
cv2.imshow(know_location)
print(known_face_encoding)
print(type(known_face_encoding))
print(known_face_encoding.shape)

# while True:
    
#     ret, frame = cap.read()
    
#     if not ret:
#         break
    
#     # 新しい画像を読み込み、エンコードする
#     unknown_image = frame

#     cv2.imshow("camera", frame)

#     unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

#     # 既知の顔と新しい顔を比較する
#     results = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding)

#     if results[0]:
#         print("新しい画像は既知の人物です。")
#     else:
#         print("新しい画像は既知の人物ではありませ")
