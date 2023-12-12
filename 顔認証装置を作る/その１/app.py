""" リアルタイムで顔を赤枠で囲う """

import cv2

# カメラを取得
cap = cv2.VideoCapture(0)
# カスケード分類器のパス
cascade_path = "/home/pi/python/RaspberryPi400_Basic_Exercises/顔認証装置を作る/その１/haarcascade_frontalface_default.xml"

# 分類器の読み込み
face_cascade = cv2.CascadeClassifier(cascade_path)

while True:
    ret, frame = cap.read()
    
    if ret:
        # 画像をグレースケールに変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 顔の検出
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(10, 10), maxSize=(300, 300))

        """
        faces = face_cascade.detectMultiScale(image, scaleFactor, minNeighbors, minSize, maxSize)

        
        image: 検出を行うグレースケール画像です。
        scaleFactor: 画像スケールの縮小率を指定します。この値は、画像サイズを減らす際にどれだけの比率で縮小するかを定義します。例えば、1.1は画像を10%縮小することを意味します。小さい値ほど、より多くのスケールで顔を検出しようとしますが、計算時間が増加します。
        minNeighbors: 検出された物体が保持するべき最小近傍数を指定します。この値は、検出された物体の品質を決定します。値が高いほど、より信頼性の高い検出がなされますが、検出される顔の数は減少します。
        minSize: 検出される物体の最小サイズを指定します。これより小さい物体は無視されます。
        maxSize (オプション): 検出される物体の最大サイズを指定します。これより大きい物体は無視されます。
        """
        
        # 顔の周囲に赤枠を描画
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 125, 255), 10)
        
        # フレームを表示
        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()