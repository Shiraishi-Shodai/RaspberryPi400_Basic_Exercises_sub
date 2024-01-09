import face_recognition
import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)
# 既知の画像の名前と特徴量を格納
feature_dict = {}

def make_encode(name_list, path_list):
    """名前とそれに対応するパスを受け取り、特徴量を取得。feature_dictに追加

    Args:
        name_list (list): _description_
        path_list (list): _description_
    """
    for name, path in zip(name_list, path_list):
        # 画像を読み込み
        img = cv2.imread(path)
        feature_dict[name] = face_recognition.face_encodings(img)[0]

make_encode(["shota"], ["/home/pi/python/RaspberryPi400_Basic_Exercises/顔認証装置を作る/その２/img/001.jpg"])
# print(feature_dict.values())
# print(type(feature_dict.values()))

while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    judge_names = []
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    print(small_frame)
    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)
    
    for encod_frame in face_encodings:
        
        judge_name = 'Unknown'
        
        matches = face_recognition.compare_faces(list(feature_dict.values()), encod_frame)
        print(matches)
        
        disctances = face_recognition.face_distance(list(feature_dict.values()), encod_frame)
        # print(disctances)
        
        min_index = np.argmin(disctances)

        if matches[min_index]:
            judge_name = list(feature_dict.keys())[min_index]
        print(f"あなたは{judge_name}ですか？")
            
        judge_names.append(judge_name)

    for (top, right, bottom, left), judge_name in zip(face_locations, judge_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 125, 255), 5)
        
        font = cv2.FONT_HERSHEY_TRIPLEX # フォントの種類
    
        # 引数: (画像, テキスト, 長方形の右下頂点の座標, フォントの種類, 文字の縮尺, 色(BGR), 文字の太さ)
        cv2.putText(frame, judge_name, (left + 10, bottom + 35), font, 1.0, (0, 0, 255), 1)
    cv2.imshow("camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
