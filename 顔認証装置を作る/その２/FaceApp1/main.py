import face_recognition
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

# 顔を検出し、その顔から得られた特徴を数値に変換
# [0]は画像内の最初の顔（あるいは唯一の顔）のエンコーディングを取得している
obama_image = face_recognition.load_image_file("./data/obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0] # (128,) numpy

biden_image = face_recognition.load_image_file("./data/biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0] # (128,) numpy

shiraishi_image = face_recognition.load_image_file("./data/shiraishi.jpg")
shiraishi_face_encoding = face_recognition.face_encodings(shiraishi_image)[0] # (128,) numpy

known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding,
    shiraishi_face_encoding
]

known_face_names = [
    "Barack Obama",
    "Joe Biden",
    "Shiraishi Shota",
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # 画像を取得
    ret, frame = video_capture.read()

    if process_this_frame:
        # 画像を４分の１のサイズにリサイズ
        # fx: 0.25倍の倍率
        # (0, 0) を新しいサイズとして指定すると、関数はこの値を無視し、代わりに fx と fy パラメーターを使用して画像のサイズを変更します。
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                
        # 画像内に検出された各顔の位置を示すタプルのリストを返す
        face_locations = face_recognition.face_locations(small_frame)
         # 128次元の特徴ベクトルのnumpy配列を画像に映る人数分(n)格納したリストを返す [(128,), (128,) ... n]
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []

        for face_encoding in face_encodings:
            
            # 既知の顔のエンコーディングリストと比較対象のエンコーディングを引数にとる
            # 比較対象の顔が一致するかどうかを示すブール値（True または False）のリストを返す
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # 既知の顔のエンコーディングリストと比較対象のエンコーディングを引数にとる
            # エンコーディングリストのそれぞれの値と比較対象の顔のユークリッド距離のリストを求める: [0.6, 0.5, 0.4]
            # 値が小さいほど顔が似ていることを示す
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            # face_distanceの内、最小値のインデックスを取得
            best_match_index = np.argmin(face_distances)
            
            # 取得した画像とのユーグリッド距離が最も小さいエンコーディング値がcompare_faceメソッドに
            # 顔が一致していると判定されたとき、判定した名前をnameに代入
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 125, 255), 5)

        font = cv2.FONT_HERSHEY_TRIPLEX # フォントの種類
    
        # 引数: (画像, テキスト, 長方形の右下頂点の座標, フォントの種類, 文字の縮尺, 色(BGR), 文字の太さ)
        cv2.putText(frame, name, (left + 10, bottom + 35), font, 1.0, (0, 0, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()