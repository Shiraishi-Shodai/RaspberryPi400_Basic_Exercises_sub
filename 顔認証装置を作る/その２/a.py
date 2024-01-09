import numpy as np
import face_recognition
import cv2

feature_dict = {}
def make_encode(name_list, path_list):
    """名前とそれに対応するパスを受け取り、特徴量を取得。feature_dictに追加

    Args:
        name_list (list): _description_
        path_list (list): _description_
    """
    for name, path in zip(name_list, path_list):
        # 画像を読み込み
        img = face_recognition.load_image_file(path)
        print(img.shape)
        img2 = cv2.imread(path)
        print(img2.shape)
        g = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        print(g.shape)
        
        feature_dict[name] = face_recognition.face_encodings(g)

make_encode(["shota"], ["/home/pi/python/RaspberryPi400_Basic_Exercises/顔認証装置を作る/その２/img/001.jpg"])
print(feature_dict)